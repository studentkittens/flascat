import os
from flask import render_template

# Own modules
import helper

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
                'image_size': helper.get_imagesize_from_cache(item),
                'is_cached':  item.is_cached,
                'provider':   item.provider,
                'source_url_full': item.source_url,
                'source_url_short': helper.get_url_domain(item.source_url)
        })
    return render_template('cover.html', option_list=option_list)
