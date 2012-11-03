#!/usr/bin/env python
# encoding: utf-8

import plyr
from flask import Flask, request, url_for, render_template

app = Flask(__name__)

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


@app.route('/do_search', methods=['POST', 'GET'])
def do_search():
    if request.method == 'POST':
        searchstr = request.form['search_term']
        artist, album = searchstr.split('+')
        qry = plyr.Query(artist=artist, album=album, get_type='cover', database=plyr.Database('.'))
        qry.verbosity = 4
        results = qry.commit()

        if len(results) > 0:
            img_name = artist + '_' + album + '.png'
            image_path = url_for('static', filename='image/' + img_name)
            results[0].write('static/image/' + img_name)
        else:
            image_path = None

        print("pfad", image_path)
        return render_template('cover.html', image_path=image_path)
    else:
        return 'Uh.'

if __name__ == '__main__':
    app.run()
