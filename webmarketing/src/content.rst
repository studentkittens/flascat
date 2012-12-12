About us
========


Wer oder was ist moosr? 
------------------------

Wir sind eine stätig wachsende Community aus Liedermachern, Musikern und Indie
Musik Liebhabern die nicht nur Musik lieben sondern auch leben! 
Bei uns findest du nicht nur informieren zu den neusten Trends und Künstler in
der Independent Musikszene, sondern auch Gleichgesinnte die diese Passion teilen.
Egal ob Pop, Ska, Indie, Reggae, Liedermaching, Rock, Alternative, Gothic,
Industrial, Bellydance, EBM, Synthpop, Fusion Indie oder andere...wir sind überall dabei! 


Moosr informiert!
-----------------

Möchtest du über Indiefastivals informiert werden oder willst du die neusten
News zu deiner Lieblings Indieband? - dann abonniere unseren Newsletter (link)
oder einen RSS Feed und wir halten dich auf dem Laufenden!


Moosr vermittelt!
-----------------

Tickets zu den Festivals oder Fanartikel findest du in unseren Shop (link)!


Die Moosr Searchengine "moosrsearch"
------------------------------------

Moosrsearch ist eine Metadatensuchmaschine, die verschiedene
Metadatensuchdienste zu einem bündelt. Cover, Artist-Biographien, Songtexte,
Artistphotos. Moosrsearch findet alles für dich!

Moosrsearch bietet für Entwickler von Musikplayern als einziger Dienst die
Möglichkeit auf verschiedene Musikmetadaten zentral zuzugreifen, das sparrt Zeit
und Nerven.


Moosr inside your player!
-------------------------

Möchtest du unsere API als Entwickler nutzen dann schau dich in unserer API
Section (link) um.


You and moosr?
---------------

Neben dieser Spezialisierung berichten wir über die Independent Musik Szene und
stellen euch Künstler die auf verschiendenen Plattformen wie Jamendo, Bandcamp
und auch Last.fm anzutreffen sind vor.

Hast du Lust mitzumachen oder möchtest du deine Band bei uns vorstellen? Dann
schreib uns ne E-Mail oder kontaktiere uns per Facebook!



API
===

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


