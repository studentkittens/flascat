#!/usr/bin/env python
# encoding: utf-8

# Standard Modules
import os
import StringIO
import urlparse
import urllib
import json
import pickle
import random

# This is great.
from functools import partial

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

# tagcloud
tagcloud = {}

# plyr's Database
metadatadb = plyr.Database('.')

###########################################################################
#                            Helper Functions                             #
###########################################################################


def get_imagesize_from_cache(cache):
    '''
    Determine the size of an image by loading it via PIL.
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
    elif get_type in ('artistbio', 'artistphoto'):
        qry.artist = search_str
    else:
        raise ValueError('Invalid get_type: ' + get_type)

    return qry


###########################################################################
#                       Tagcloud Related Functions                        #
###########################################################################

def tagcloud_save(path):
    'Save the tagcloud to path'
    pickle.dump(tagcloud, open(path, 'wb'))


def tagcloud_add(get_type, search_str):
    'Add the search node defined by get_type and search_str to tagcloud'
    taglist = tagcloud.setdefault(get_type, [])

    # See if it is already in the list,
    # if so we increment the tag_size
    for idx, prio_tag in enumerate(taglist):
        if prio_tag[1] == search_str:
            taglist[idx] = (max(prio_tag[0] + 1, 4), search_str)
            break
    else:
        # This search_str was not yet in.
        taglist.append((2, search_str))


def tagcloud_load(path):
    'Load tagcloud from disk'
    global tagcloud
    try:
        tagcloud = pickle.load(open(path, 'rb'))
    except IOError:
        # Some sort of ,,default''
        tagcloud = {
            'cover': [(2, 'Rammstein + Mutter')],
            'lyrics': [(3, 'Farin Urlaub + Lieber Staat')],
            'artistphoto': [(4, 'Avril Lavigne')],
            'artistbio': [(1, 'Knorkator')]
        }

###########################################################################
#                           Rendering Functions                           #
###########################################################################


def render_lyrics(results, newlines=1):
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
                'lyrics_text': encoded_lyrics.replace('\n', '<br />' * newlines)
            })
        except UnicodeDecodeError as err:
            print('Warning: Cannot render lyrics due to bad encoding: ', err)

    return render_template('lyrics.html', lyrics_list=lyrics_list)


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
    '''
    Redirect to the Query Page.
    '''
    if request.method == 'POST':
        search_str = request.form['search_term'].strip()
        number = int(request.form['number'])
        get_type = request.form['get_type']

        if len(search_str) is 0:
            flash('Please enter a Query.')
            return redirect(url_for('main_page'))
        else:
            tagcloud_add(get_type, search_str)
            return redirect(url_for('do_query',
                    search_str=search_str,
                    number=number,
                    get_type=get_type))
    else:
        return redirect(url_for('main_page'))


@app.route('/query/<get_type>/<int:number>/<search_str>')
def do_query(get_type, number=1, search_str=''):
    '''
    Actual drawing of the results.
    '''
    try:

        qry = configure_query(get_type, search_str, number)
        flash('Searching for items...')
        results = qry.commit()
        flash('Found %d items' % len(results))

        if len(results) > 0:
            render = {
                    'lyrics': render_lyrics,
                    'cover': render_cover,
                    'artistbio':  partial(render_lyrics, newlines=2),
                    'artistphoto': render_cover
            }

            # Try to render the results.
            return render[get_type](results)
        else:
            flash('Woah! It seems no items were found!')
            return redirect(url_for('main_page'))
    except IndexError:
        flash('It seems you also need an artist/album/title.')
        return redirect(url_for('main_page'))


@app.route('/api/<get_type>/<int:number>/<search_str>')
def api_root(get_type, search_str, number=1):
    '''
    Very simple JSON API
    '''
    try:
        response = []
        qry = configure_query(get_type, search_str, number)
        for item in qry.commit():
            response.append({
                'size': item.size,
                'provider': item.provider,
                'url': item.source_url,
                'md5sum': item.checksum,
                'image_format': item.image_format,
                'is_cached': item.is_cached
                })
    except (IndexError):
        return 'Search Query does not contain a "+"'
    except (ValueError):
        return render_template('404.html'), 404
    else:
        return json.dumps({
            'get_type': get_type,
            'artist': qry.artist,
            'album': qry.album,
            'title': qry.title,
            'number': qry.number,
            'results': response
            }, indent=4, sort_keys=True)


@app.route('/home')
def home_page():
    '''
    A Todo point...
    '''
    return 'No content here yet.', 404


@app.errorhandler(404)
def page_not_found(e):
    '''
    Dead link handler :-)
    '''
    return render_template('404.html'), 404


@app.route('/')
def main_page():
    '''
    The mainpage seen on localhost:5000
    '''
    tags = []
    for get_type, sublist in tagcloud.items():
        # The size of a tag is 75% the amount of searchings, 25% random
        calc_size = lambda x: int((x * 3 + random.randrange(1, 5)) / 4)

        # Convert the dictionary to a template usable taglist
        tags += map(lambda x: (get_type, x[1], calc_size(x[0])), sublist)

    return render_template('cloud.html', tags=tags)


###########################################################################
#                               Let it run!                               #
###########################################################################

if __name__ == '__main__':
    tagcloud_path = 'tagcloud.pickle'
    tagcloud_load(tagcloud_path)
    app.run(debug=True)
    tagcloud_save(tagcloud_path)
