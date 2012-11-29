import pickle

###########################################################################
#                       Tagcloud Related Functions                        #
###########################################################################

TAGCLOUD = {}


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
    global TAGCLOUD
    try:
        TAGCLOUD = pickle.load(open(path, 'rb'))
    except IOError:
        # Some sort of ,,default''
        TAGCLOUD = {
            'cover': [(2, 'Rammstein + Mutter')],
            'lyrics': [(3, 'Farin Urlaub + Lieber Staat')],
            'artistphoto': [(4, 'Avril Lavigne')],
            'artistbio': [(1, 'Knorkator')]
        }
