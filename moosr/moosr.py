#!/usr/bin/env python
# encoding: utf-8

# Standard Modules
import os
import traceback
import StringIO
import urlparse
import urllib

# Python-Glyr
import plyr

# PIL
import Image

# Flask imports
from flask import Flask, request, render_template, flash, redirect, url_for

# Instance the Flask Application itself
app = Flask(__name__)

# echo '' | md5sum
app.secret_key = '68b329da9893e34099c7d8ad5cb9c940'

# plyr's Database
metadatadb = plyr.Database('.')

###########################################################################
#                            Helper Functions                             #
###########################################################################


def get_imagesize_from_cache(cache):
    '''
    This is silly. Remove it later.
    '''
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
    '''
    Get the domain Part from an url.

    :full_url: A full url e.g. http://www.google.de/?q=lala&b=23
    :returns: www.google.de
    '''
    return urlparse.urlparse(full_url).netloc


def configure_query(get_type, search_str, number=1):
    '''
    Configure a Query from a get_type and a search string.

    :get_type: What type of metadata to search
    :search_str: the content of the search box
    :number: The number of items to search
    :returns: a new, committable plyr.Query
    '''
    # Make sure the search_str is correctly encoded
    if type(search_str) is unicode:
        encoded_search_str = search_str.encode('utf-8')
    else:
        encoded_search_str = search_str

    # Split the search term into artist/(album|title)
    terms = list(map(str.strip, encoded_search_str.split('+')))

    # Build up a plyr.Query to
    qry = plyr.Query(
            number=number,        # Number of items to search
            verbosity=3,          # How verbose the output should be
            do_download=True,     # Download Images or just return the URL?
            timeout=3,            # Timeout in seconds to wait before cancel
            database=metadatadb,  # Database connection.
            get_type=get_type)    # Metadata Type

    qry.artist = unicode(terms[0], 'utf-8')

    if get_type == 'cover':
        qry.album = unicode(terms[1], 'utf-8')
    elif get_type == 'lyrics':
        qry.title = unicode(terms[1], 'utf-8')
        qry.parallel = 3  # Hack to fix silly lyrdb
    elif get_type == 'artistbio':
        qry.artist = search_str
    else:
        raise ValueError('Invalid get_type: ' + get_type)

    return qry

###########################################################################
#                           Rendering Functions                           #
###########################################################################


def render_lyrics(results):
    '''
    Try to render a list of lyrics as textboxes.

    :results: A list of result caches
    :returns: A readily rendered template.
    '''
    lyrics_list = []
    for item in results:
        try:
            encoded_lyrics = unicode(item.data, 'utf-8')
            lyrics_list.append({
                'lyrics_text': encoded_lyrics.replace('\n', '<br />')
            })
        except UnicodeDecodeError as err:
            print('Warning: Cannot render lyrics due to bad encoding: ', err)

    return render_template('lyrics.html', lyrics_list=lyrics_list)


def render_bio(results):
    '''
    Try to render the biographies-list as textboxes.

    :results: A list of result caches
    :returns: A readily rendered template.
    '''
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


def render_cover(results):
    '''
    Try to render the cover-list as list of cover-templates.

    :results: A list of result caches
    :returns: A readily rendered template.
    '''
    option_list = []
    for item in results:
        # Save image in images/
        image_path = os.path.join('images', item.checksum)
        item.write(image_path)

        try:
            os.mkdir('images')
        except OSError:
            pass

        option_list.append({
                'image_path': item.source_url,
                'image_size': get_imagesize_from_cache(item),
                'is_cached':  item.is_cached,
                'provider':   item.provider,
                'source_url_full': item.source_url,
                'source_url_short': get_url_domain(item.source_url)
        })
    return render_template('cover.html', option_list=option_list)


###########################################################################
#                            Routing functions                            #
###########################################################################

@app.route('/do_search', methods=['POST', 'GET'])
def do_search():
    if request.method == 'POST':

        try:
            search_str = request.form['search_term'].strip()
            get_type = request.form['get_type']
            number = int(request.form['number'])

            if len(search_str) is 0:
                flash('Please enter a Query.')
                return redirect(url_for('main_page'))

            qry = configure_query(get_type, search_str, number)
            flash('Searching for items...')
            results = qry.commit()
            flash('Found %d items' % len(results))

            if len(results) > 0:
                render = {
                        'lyrics': render_lyrics,
                        'cover': render_cover,
                        'artistbio':  render_bio
                }

                # Try to render the results.
                return render[get_type](results)
            else:
                flash('Woah! It seems no items were found!')
                return redirect(url_for('main_page'))
        except KeyError as err:
            print('Something unexpected happened: ', err)
        #except UnicodeDecodeError as err:
        #    print('Invalidly encoded search term: ', err)
        #    traceback.print_exc()
        except IndexError as err:
            flash('It seems you also need an artist/album/title.')
            return redirect(url_for('main_page'))
    else:
        return redirect(url_for('main_page'))


@app.route('/')
def main_page():
    faketags = ['Rammstein', 'Farin Urlaub', 'Knorkator', 'Avril Lavigne']
    inval = enumerate(faketags, 1)
    tagvalues = dict()
    for item in inval:
        st = "tag" + str(item[0])
        tagvalues[st] = item[1]

    return render_template('cloud.html', entries=tagvalues)


###########################################################################
#                               Let it run!                               #
###########################################################################

if __name__ == '__main__':
    app.run(debug=True)
