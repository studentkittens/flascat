TODO
====

Python - programmieren kann auch spass machen :)
------------------------------------------------

* Eingesetzt als: 

    * … Wissenschaftlicher Bereich (numpy, scipy bei NASA)
    * … Webprogrammierung (Flask, Zope, Django)
    * … Systemprogrammierung (Admintasks, Networking)
    * … Prototyping Sprache (3-10x schnellerer developement Prozess)
    * … ,,Glue''-Sprache (Compiler für C/++, Java)
    * … integrierte ,,Scriptsprache'' (Blender3D, viele Spiele)
    * … Educationbereich (Primäre Sprache auf dem Raspberry)
    * … öfter als man denkt. -> unicode smiley <-

History!
--------

* Entstanden 1991 (älter als Java, mit 1995)
* Guido van Rossum:

   .. image  (guido.png) ..

* (Ursprüngliche) Designziele:

  * Als Ergänzung zu C++, Ersetzung von Shellscripts
  * Easy-to-write-and-read.
  * Batteries included.

Wiederverwendung
----------------

* Guido's Time Machine

  * *sehr* wenig Boilerplate Code
  * PEP8
   ... Viele coole Datentypen...  <-- KITTEH


   .. image (exhaustion.png) ..



Python2 vs. 3
-------------

Auf Python3 Seite:

* Einfache Unicodeünterstützung.
* Alles leitet von ``object`` ab.
* Syntaxänderungen und Änderungen an der C-API.

* Leider inkompatibel zu Python2.
  
  * Viele Features aber backported.

* Manche externe Libraries noch Python2 basiert (Flask)!

   * Python2 wird noch lange supported.
 

Flask
-----

* Architektur
  Schaubild (Jinja, Werkzeug, SQlite3, Twisted)


-> Unter Weitere Features

   Es zwingt dir nix auf.


return make_xml_response(method apikey)


resp_data = make_xml_response(method, apikey)
return Response(resp_data, mimetype='text/xml')
