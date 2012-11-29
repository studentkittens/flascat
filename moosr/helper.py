#!/usr/bin/env python
# encoding: utf-8

import StringIO
import Image
import urllib
import urlparse
import plyr

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
