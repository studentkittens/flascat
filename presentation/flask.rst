.. impress::
   :func: square

======================
**Eine Einführung in**
======================

.. step::
   :class: center
   :data-x: 7500
   :data-y: -1000
   :data-scale: 5

.. image:: static/flask_logo.png
    :width: 500
    :align: center

|

``http://flask.pocoo.org/``

Vorwort
-------

.. slide::
   :data-x: 0
   :data-y: 0


Präsentation angelehnt an:
    
    http://flask.pocoo.org/docs/quickstart/

What?
-----
* Flask ist ein **Microwebframework**.
* Fokus: Erweiterbarkeit + gute Dokumentation.
* Abhängigkeiten:

    * ``Werkzeug``: WSGI Middleware.
    * ``Jinja2``: Eine Template Engine.

* BSD Lizenz → Kommerzielle Projekte möglich.

-----

**Warum denn "micro"?**
    |
    | *Flask aims to keep the core simple but extensible.*
    | *Flask won’t make many decisions for you, such as what database to use.*

**Statistiken:**

    800 LOC Code, 1500 LOC Testcases, 200 A4 Seiten Dokumentation.

How?
----

Python2 only. Python 3 Port in ferner Zukunft.


Im Vergleich zu Django:

    * Beschränkung auf Kernfunktionalität.
    * don't reinvent the wheel.
    * Modular, Erweiterung durch Plugins.
    * zB.: Datenbank und Templateengine austauschbar. 


Features
--------

* Handhabung von Authentifizierung, Cookies, Sessions
* konfigurierbares Caching
* Internationalisierung
* eine Abstraktionsschicht für Datenbanken, die dynamisch SQL erzeugt (ORM, Object-Relational-Mapper)
* Kompatibilität zu vielen Datenbankmanagementsystemen 


Hello World!
------------

Die folgende Anwendung wird auf ``localhost:5000`` 
horchen und bei einem ``GET``
einem unformattieren **Hallo Welt** ausgeben.

::

    # Importiere die Flask Libraries, 
    # und instanziere eine Flask-Anwendung.
    from flask import Flask
    app = Flask(__name__)
     
    # hello() soll für ein Zugriff auf 
    # die root-url aufgerufen werden.
    @app.route("/")
    def hello():
        return "Hallo Welt"
    
    # Falls das Skript direkt ausgeführt wird,
    # so lasse die Anwendung laufen.
    if __name__ == "__main__":
        app.run(debug=True)


Und nun... Python!
------------------

|
|
|
|

Say Hello to a new language.


Routing & Troubleshooting #1
----------------------------

**Routing**:

    ::

        def compose_hello(name):
            return '<b>Hello ' + name + '!</b>'

        @app.route('/hello')
        def hello():
            return compose_hello('Workshop')
      
-----

<Hier Bild einfügen>


Routing & Troubleshooting #2
----------------------------

**Redirects**:
  
  * http://www.domain.de/newest_article → 
    http://www.domain.de/article/month/week/day/blah.html

  * Realisierbar mit ``redirect(url)`` ::

     from flask import redirect
     @app.route('/redirect_to_google')
     def hello():
        return redirect('www.google.de')
    
  * Würde bei einem GET von ``localhost:5000/redirect_to_google`` ``www.google.de``
    mittels eines HTTP Redirects aufrufen.


Routing & Troubleshooting #3
----------------------------

**HTTP Verben**:

    * ``GET``, ``POST``, ``PUT``, ``HEAD``, ``OPTIONS``

**URLs konstruieren**:

    * Vermeidung von hardgecodeten URLs im Programm:

        ``url_for('a_name_of_a_view_function')`` 

**Statische Komponenten**:

    * Werden in einem ``static/`` folder abgelegt (CSS, Bilder).
    * Templates gehen per default nach ``template/``.
    * Holen eines Images: ::

        url_for('static/', filename='cover.png')

Templates & How to render them
------------------------------

**Templates**

    * Mit ``render_template('hello.html)`` wird über Jinja die Seite
      ``hello.html`` gerendert ::

        @app.route('/<n>')
        def hello(n):
            return render_template('hello.html',n=n)

    * .. code-block:: html

        <!-- hello.html -->
        <html>
            <body>
                <h1>Hello {{ n }}!</h1>
            </body>
        </html>

Request Data
------------

request.from etc
POST 

Sessions
--------

login beispiel

Debugging
---------

Show the Debugger

``moosr``
---------

Unsere kleine Beispielseite mit Flask.

Übung
-----
