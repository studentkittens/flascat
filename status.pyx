cimport moose as c

cdef status_from_ptr(c.mpd_song * ptr):
    'Instance a new Status() with the underlying mpd_status ptr'
    if ptr != NULL:
        return Song()._init(ptr)
    else:
        return None

cdef class Status:
    # Actual c-level struct
    cdef c.mpd_status * _status

    ################
    #  Allocation  #
    ################

    def __cinit__(self):
        self._status = NULL

    cdef c.mpd_status * _p(self):
        return self._status

    cdef object _init(self, c.mpd_status * status):
        self._status = status
        return self

    ################
    #  Properties  #
    ################

    '''
    int mpd_status_get_volume(mpd_status *)
    bool mpd_status_get_repeat(mpd_status *)
    bool mpd_status_get_random(mpd_status *)
    bool mpd_status_get_single(mpd_status *)
    bool mpd_status_get_consume(mpd_status *)
    unsigned mpd_status_get_queue_length(mpd_status *)
    unsigned mpd_status_get_queue_version(mpd_status *)
    mpd_state mpd_status_get_state(mpd_status *)
    unsigned mpd_status_get_crossfade(mpd_status *)
    float mpd_status_get_mixrampdb(mpd_status *)
    float mpd_status_get_mixrampdelay(mpd_status *)
    int mpd_status_get_song_pos(mpd_status *)
    int mpd_status_get_song_id(mpd_status *)
    int mpd_status_get_next_song_pos(mpd_status *)
    int mpd_status_get_next_song_id(mpd_status *)
    unsigned mpd_status_get_elapsed_time(mpd_status *)
    unsigned mpd_status_get_elapsed_ms(mpd_status *)
    unsigned mpd_status_get_total_time(mpd_status *)
    unsigned mpd_status_get_kbit_rate(mpd_status *)
    mpd_audio_format * mpd_status_get_audio_format(mpd_status *)
    unsigned mpd_status_get_update_id(mpd_status *)
    char * mpd_status_get_error(mpd_status *)
    '''

    property volume:
        def __get__(self):
            c.mpd_status_get_volume(self._p())


