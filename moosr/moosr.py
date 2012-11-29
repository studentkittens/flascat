#!/usr/bin/env python
# encoding: utf-8

# Standard Modules
import json
import random

# This is great.
from functools import partial

# Flask imports
from flask import Flask, request, render_template, flash, redirect, url_for, Response

# Login
from flask.ext.login import login_required

# Own modules
import helper
import tagcloud
import render
import user_login
import database


# Instance the Flask Application itself
app = Flask(__name__)


# echo '' | md5sum, actually, a rather bad key :-)
app.secret_key = '68b329da9893e34099c7d8ad5cb9c940'


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
            tagcloud.tagcloud_add(get_type, search_str)
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
        qry = helper.configure_query(get_type, search_str, number)
    except IndexError:
        flash('It seems you also need an artist/album/title.')
        return redirect(url_for('main_page'))
    else:
        flash('Searching for items...')
        results = qry.commit()
        flash('Found %d items' % len(results))

        if len(results) > 0:
            render_dict = {
                    'lyrics': render.render_lyrics,
                    'cover': render.render_cover,
                    'artistbio':  partial(render.render_lyrics, newlines=2),
                    'artistphoto': render.render_cover
            }

            # Try to render the results.
            return render_dict[get_type](results)
        else:
            flash('Woah! It seems no items were found!')
            return redirect(url_for('main_page'))


@app.route('/api/<get_type>/<int:number>/<search_str>')
def api_root(get_type, search_str, number=1):
    '''
    Very simple JSON API
    '''
    try:
        response = []
        qry = helper.configure_query(get_type, search_str, number)
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
        data = json.dumps({
            'get_type': get_type,
            'artist': qry.artist,
            'album': qry.album,
            'title': qry.title,
            'number': qry.number,
            'results': response
            }, indent=4, sort_keys=True)

    return Response(data, mimetype='application/json')


@app.route("/login", methods=["GET", "POST"])
def login():
    return user_login.do_login(request)


@app.route("/logout")
@login_required
def logout():
    return user_login.do_logout(request)


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


@app.route('/blog')
def blog_page():
    database.connect_db()


@app.route('/')
def main_page():
    '''
    The mainpage seen on localhost:5000
    '''
    tags = []
    for get_type, sublist in tagcloud.TAGCLOUD.items():
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
    tagcloud.tagcloud_load(tagcloud_path)
    user_login.setup(app)
    app.run(debug=True)
    tagcloud.tagcloud_save(tagcloud_path)
