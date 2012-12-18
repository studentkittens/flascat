#!/usr/bin/env python
# encoding: utf-8

# Standard Modules
import json
import random
import os
import time


from functools import partial

# Flask imports
from flask import Flask, request, render_template, flash, redirect, url_for, Response, g, session, abort, send_from_directory

# Login
from flask.ext.login import login_required

# RST Pages
from flask.ext.rstpages import RSTPages

# Own modules
import helper
import tagcloud
import render
import user_login
import blogdb


# Instance the Flask Application itself
app = Flask(__name__)


# RST Converter
rst_pages = RSTPages(app)


# echo '' | md5sum, actually, a rather bad key :-)
app.secret_key = '68b329da9893e34099c7d8ad5cb9c940'

# database configuration
DATABASE = 'moosr.db'
USERNAME = 'admin'
PASSWORD = 'default'
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

###########################################################################
#                            Routing functions                            #
###########################################################################


def get_html_content(name):
    try:
        with open(os.path.join('pages', name), 'r') as f:
            return unicode(f.read(), 'utf-8')
    except (IOError, OSError):
        return u'<b>Warning:</b> No text found!'


def get_page_content(page, robot_index='all', keywords=[]):
    html = rst_pages.get(page)
    return render_template("staticpage.html",
                           input_text=html.body,
                           input_title=html.title,
                           input_indexing=robot_index,
                           input_keywords=', '.join(keywords))


@app.route('/impressum')
def show_impressum():
    return get_page_content('impressum', robot_index='noindex')


@app.route('/developers')
def show_developers():
    return get_page_content('developers', keywords=['API', 'Manual', 'Reference',
                                                    'Metadata', 'Developer'])


@app.route('/about-us')
def show_aboutus():
    return get_page_content('aboutus', keywords=['About Us', 'Moosr', 'Inide',
                                                 'Music', ''])


@app.route('/help')
def show_help():
    return get_page_content('help')


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
#                               Blog Stuff                                #
###########################################################################


@app.route('/blog')
def show_entries():
    cur = g.db.execute('select title, short_title, text, username, id from entries order by id desc')
    entries = [dict(title=row[0], short_title=row[1], text=row[2], username=row[3])
               for row in cur.fetchall()]

    return render_template('show_entries.html', entries=entries)


@app.route('/blog/archive')
def show_archive():
    cur = g.db.execute('select post_date, short_title from entries order by id desc')
    entries = [dict(post_date=row[0], short_title=row[1]) for row in cur.fetchall()]
    return render_template('archive.html', entries=entries)


@app.route('/blog/entry/<post_short_name>')
def show_blog_entry(post_short_name):
    cur = g.db.execute('select title, short_title, text, username, post_date from entries where short_title = ?;', [post_short_name])
    results = cur.fetchall()
    if len(results) is 0:
        abort(404)

    entry = results[0]
    post_title = entry[0] + ' <small><em>by ' + entry[3] + '</em></small>'
    return render_template('staticpage.html', input_text=entry[2], input_title=post_title)


@app.route('/add', methods=['POST'])
def add_entry():
    userobject = session.get('logged_in')
    if not userobject:
        abort(401)

    with open('pages/last_blog_post.rst', 'w') as f:
        f.write(request.form['text'].encode('utf-8'))

    rst_html = rst_pages.get('last_blog_post')
    g.db.execute('insert into entries (title, short_title, text, username, post_date) values (?, ?, ?, ?, ?)',
                 [request.form['title'], request.form['short_title'],
                  rst_html.body, userobject.name],
                  time.strftime('%d/%m/%Y - %H:%M', time.localtime(time.time())))

    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

###########################################################################
#                               Let it run!                               #
###########################################################################

if __name__ == '__main__':
    app.before_request(blogdb.setup)
    app.teardown_request(blogdb.teardown)

    tagcloud_path = 'tagcloud.pickle'
    tagcloud.tagcloud_load(tagcloud_path)
    user_login.setup(app)

    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print('-- Interrupt.')
    finally:
        tagcloud.tagcloud_save(tagcloud_path)
