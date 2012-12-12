Developers
==========

Wie funktioniert moosrsearch? 
------------------------------

Das Moosrsearch Backend greifft im Hintergrund über 40 verscheidene Provider für
für dich zu und sucht die gewünschten Informationen zusammen. Dabei spricht
moosrsearch über 25 Provider an und greift hierfür auf über 40 verscheidene
Implementierungen zu. Die hierzu verwendete library ist libglyr. (Link)


Moosrsearch Metadata Provider
-----------------------------

Folgende Onlineprovider werden von moosrsearch genutzt:

   * bbcmusic 
   * chartlyrics 
   * chordie 
   * discogs 
   * elyrics 
   * flickr 
   * generated 
   * google 
   * htbackdrops 
   * jamendo 
   * lastfm 
   * lipwalk 
   * lyrdb 
   * lyricsreg 
   * lyricstime 
   * lyricsvip 
   * lyricswiki 
   * lyrix 
   * magistrix 
   * metallum 
   * metrolyrics 
   * musicbrainz 
   * picsearch 
   * rhapsody 
   * singerpictures 
   * slothradio 

Lokale Provider:

   * local (sqlcache)    
   * musictree 


Moosrsearch API Usage:
----------------------

Auf die moosrsearch engine kann auf mehrere Varianten angesprochen werden, über eine
ganz normale HTML query oder zur maschinellen Auswertung über unsere API die, die
gewünschten Metadaten im Jason format liefert.


**HTML Version:**

::

    http://www.moosr.org/query/<type>/<number>/<query>



**Json Version:**

::

    http://www.moosr.org/api/<type>/<number>/<query>


