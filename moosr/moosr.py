#!/usr/bin/env python
# encoding: utf-8

import plyr
import Image
import StringIO
import urlparse
import urllib

from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)

# echo '' | md5sum
app.secret_key = '68b329da9893e34099c7d8ad5cb9c940'

faketags = ['Rammstein', 'Farin Urlaub', 'Knorkator', 'Avril Lavigne']


@app.route('/')
def main_page():
    inval = enumerate(faketags, 1)
    tagvalues = dict()
    for item in inval:
        st = "tag" + str(item[0])
        tagvalues[st] = item[1]
    print(tagvalues)

    return render_template('cloud.html', entries=tagvalues)


def render_lyrics(results):
    lyrics_list = []
    for item in results:
        try:
            encoded_lyrics = unicode(item.data, 'utf-8')
            lyrics_list.append({
                'lyrics_text': encoded_lyrics.replace('\n', '<br />')
            })
        except UnicodeDecodeError as err:
            print('Cannot render lyrics due to bad encoding: ', err)

    return render_template('lyrics.html', lyrics_list=lyrics_list)


def render_bio(results):
    bio_list = []
    for item in results:
        try:
            encoded_bio = unicode(item.data, 'utf-8')
            bio_list.append({
                'bio_text': encoded_bio.replace('\n', '<br /><br />')
            })
        except UnicodeDecodeError as err:
            print('Cannot render bio due to bad encoding: ', err)

    print(bio_list)
    return render_template('bio.html', bio_list=bio_list)


def get_imagesize_from_cache(cache):
    try:
        if cache.is_image is False:
            data = urllib.urlopen(cache.data).read()
        else:
            data = cache.data

        stream = StringIO.StringIO(data)
        img = Image.open(stream)
        return 'x'.join(map(str, img.size))
    except:
        # Be nice if something fails.
        return 'N/A'


def get_url_domain(full_url):
    return urlparse.urlparse(full_url).netloc


def render_cover(results):
    option_list = []
    for item in results:
        option_list.append({
                'image_path': item.data,
                'image_size': 'N/A', #get_imagesize_from_cache(item),
                'is_cached':  item.is_cached,
                'provider':   item.provider,
                'source_url_full': item.source_url,
                'source_url_short': get_url_domain(item.source_url)
        })
    return render_template('cover.html', option_list=option_list)


@app.route('/do_search', methods=['POST', 'GET'])
def do_search():
    if request.method == 'POST':

        try:
            search_str = request.form['search_term']
            get_type = request.form['get_type']

            qry = configure_query(get_type, search_str)
            flash('Searching for items...')
            results = qry.commit()
            flash('Found %d items' % len(results))

            if len(results) > 0:
                meta = {
                        'lyrics': render_lyrics,
                        'cover': render_cover,
                        'artistbio':  render_bio
                }

                return meta[get_type](results)
            else:
                # Flash message
                flash('Woah! It seems no items were found!')
                return redirect(url_for('main_page'))
        except KeyError as err:
            print('Something unexpected happened: ', err)
        except UnicodeDecodeError as err:
            print('Invalidly encoded search term: ', err)
    else:
        return 'This site should not be used from a GET.'


def configure_query(get_type, search_str):
    print(search_str, type(search_str))
    if type(search_str) is unicode:
        encoded_search_str = search_str.encode('utf-8')
    else:
        encoded_search_str = search_str

    terms = list(map(str.strip, encoded_search_str.split('+')))
    qry = plyr.Query(number=2,
            verbosity=3,
            do_download=False,
            get_type=get_type)

    qry.artist = terms[0]

    if get_type == 'cover':
        qry.album = unicode(terms[1], 'utf-8')
    elif get_type == 'lyrics':
        qry.title = unicode(terms[1], 'utf-8')
    elif get_type == 'artistbio':
        qry.artist = search_str
    else:
        raise ValueError('Invalid get_type: ' + get_type)

    return qry


if __name__ == '__main__':
    app.run(debug=True)
