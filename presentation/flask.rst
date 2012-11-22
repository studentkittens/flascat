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

**Präsentation angelehnt an den** `Flask Quickstart <http://flask.pocoo.org/docs/quickstart>`_


Um was geht's?
--------------

.. slide::
   :data-x: 0
   :data-y: 0

* Flask ist ein **Microwebframework**.
* **Fokus:** Erweiterbarkeit + gute Dokumentation.
* Abhängigkeiten:

    * `Werkzeug <http://werkzeug.pocoo.org/>`_: WSGI Middleware.
    * `Jinja2 <http://jinja.pocoo.org/`Jinja2>`_: Eine Template Engine.

* BSD Lizenz → Kommerzielle Projekte möglich.

-----

**Warum denn "micro"?**
    |
    | *Flask aims to keep the core simple but extensible.*
    | *Flask won’t make many decisions for you, such as what database to use.*

**Anderer Grund:**

    800 LOC Code, 1500 LOC Testcases, 200 A4 Seiten Dokumentation.

Architektur
-----------


.. image:: static/schaubild.png
    :align: center
    :width: 85%

Warum nicht Django?
-------------------


**Im Vergleich zu Django**:

    * Beschränkung auf Kernfunktionalität.
    * don't reinvent the wheel.
    * Modular, Erweiterung durch Plugins.
    * zB.: Datenbank und Templateengine austauschbar. 
    * Sehr viel kleiner / handlicher.
    * Skalierbarkeit.

**Anmerkung**: 

    * Flask läuft momentan nur mit Python 2.x.
    * Python 3.x Port ist in Arbeit.
    * Django läuft bereits auf Python 3.x.
    * Admin Funktionalität.

Weitere Features
----------------

|
|

    * Handhabung von Authentifizierung, Cookies, Sessions
    * Konfigurierbares Caching
    * Internationalisierung
    * Abstraktionsschicht für Datenbanken, die dynamisch SQL erzeugt

      * ORM (Object-Relational-Mapper) als Plugin.
    * Kompatibilität zu vielen Datenbankmanagementsystemen.
    * Kein Zwang bestimmte Software zu nutzen,
      →  Wiederverwendung anderer Frameworks! 


Hello World!
------------

Die folgende Anwendung wird auf ``localhost:5000`` 
horchen und bei einem ``GET``
einem unformattieren **Hallo Welt** ausgeben.

::

    # Importiere die Flask Libraries, 
    # und instanziere eine Flask-Anwendung.
    from flask import Flask
    app = Flask('MyFirstFlaskApp')
     
    # hello() soll für ein Zugriff auf 
    # die root-url aufgerufen werden.
    @app.route("/")
    def hello():
        return "Hallo Welt"
    
    # Falls das Skript direkt ausgeführt wird,
    # so lasse die Anwendung laufen.
    if __name__ == "__main__":
        app.run(debug=True)


Und nun…  Schlangen!
---------------------

.. image:: static/pycake.png
    :width: 500
    :align: center

|
|

:ref:`python-part`

View Functions
--------------

**Gute Tiere anzeigen:**

.. code-block:: python

    @app.route('/')
    def show_good_ones():
        # Fake-Daten aus der Datenbank
        db = ['turtle', 'owl',   'dog',
              'kitteh', 'koala', 'moose']

        # Tue etwas mit den Daten
        good = [y for x, y in enumerate(db) if x % 2 != 0]

        # Visualisiere sie (hier einfach "raw")
        return str(good)

    if __name__ == '__main__':
        app.run(debug=True)

* *View Funktionen* dienen zum Visualisieren von Daten

Routing & Troubleshooting #1
----------------------------

**Routing**:

    ::

        def compose_hello(name):
            return '<h1><b>Hello ' + name + '!</b></h1>'

        @app.route('/hello')
        def hello():
            return compose_hello('Workshop'), 200
      

**Gerendertes HTML im Browser (localhost:5000):**

-----


.. raw:: html

    <h1><b>Hello Workshop</b></h1> 

:: 
    
    <h1><b>Hello Workshop</b></h1> 
    



Routing & Troubleshooting #2
----------------------------

**Redirects**:
  
  * http://www.domain.de/newest_article → 
    http://www.domain.de/article/month/week/day/blah.html

  * Realisierbar mit ``redirect(url)`` ::

     from flask import redirect
     @app.route('/redirect_to_google')
     def hello():
        return redirect('http://www.google.de')
    
  * Würde bei einem GET von ``localhost:5000/redirect_to_google`` ``www.google.de``
    mittels eines HTTP Redirects aufrufen.
  * Lässt man das Protokoll (``http://``) weg, so wird innerhalb der Seitengrenzen redirected,
    also zu ``localhost:5000/www.google.de``.

    


Routing & Troubleshooting #3
----------------------------

**HTTP Verben:**

    * ``GET``, ``POST``, ``PUT``, ``HEAD``, ``OPTIONS``

**URL Building:**

    * Vermeidung von hardgecodeten URLs im Programm: ::

        url_for('a_name_of_a_view_function') 

**Statische Komponenten:**

    * … werden in einem ``static/`` folder abgelegt (CSS, Bilder).
    * Templates gehen per default nach ``templates/``. ::

        url_for('static/', filename='cover.png')

Templates & How to render them
------------------------------

**Templates**

    * Mit ``render_template('hello.html)`` wird über Jinja2 die Seite
      ``hi.html`` gerendert ::

        @app.route('/greet/<name>')
        def hello(name):
           return render_template('hi.html',you=name)

    * .. code-block:: html

        <!-- hi.html -->
        <html>
            <body>
                <h1>Hello {{ you }}!</h1>
            </body>
        </html>


Templates #2
------------

.. code-block:: html

    <!-- userlist.html -->
    <!doctype html>
    <title>Userlist</title>

    <ul>
    {% for user in users %}
        {% if user != 'admin' %}
            <li>{{ user }}</li>
        {% endif %}
    {% endfor %}
    </ul>


**Rendern des Templates aus einer View Funtkion:**

::

    users = ['admin', 'sam', 'phil']
    return render_template('userlist.html', users=users)

    


Templates #3
------------

**parent.html:**

.. code-block:: html 

    <html>
        <title>Flaskr</title>
        <h1>Flaskr Headline</h1>
        <body>
            {% block body %}{% endblock %}
        </body>
    </html>


**child.html:**

.. code-block:: html 

    {% extends "parent.html" %}
    {% block body %}
        <p>Hello I am a child</p>
    {% endblock %}

* Nützlich zur Realisierung verschachtelter Layouts.



Request Object 
--------------

Das **Request Object** dient u.a. dazu POST Daten auszulesen.

::

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':  
            return '<b>' + request.form['text'] + '</b>'
        else:
            return '''<form action="" method="post">
                        <p><input type=text name=text></p>
                        <p><input type=submit value=Sub></p>
                      </form>'''

**Anmerkung:**

    * Über ``request.method`` (String) wird die HTTP Methode geprüft
    * Über ``request.form`` (Dictionary) können Formulare ausgelesen werden




Session Object #1
-----------------

**Codeblock um Login zu realisieren:**

::

    from flask import Flask, session, redirect
    from flask import escape, request, url_for

    app = Flask(__name__)

    @app.route('/')
    def index():
        if 'user' in session:
            return 'You are: ' + escape(session['user'])
        return 'You are not logged in!'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['user'] = request.form['user']
            return redirect(url_for('index'))
        return render_template('login.html')


Session Object #2
-----------------

**Logout:**

::

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('index'))


**Secret Key:** ::

    app.secret_key = '68b329da9893e34099c7d8ad5cb9c940'

**HTML Formular (login.html):**

.. code-block:: html
    
        <form action="" method="post">
            <p><input type=text name=user></p>
            <p><input type=submit value=Login></p>
        </form>
        

URL Parameter
-------------

* Im Web/RESTful APIs sieht man oft sowas wie: 

    http://www.lastfm.com/api/?method=artist.getSimilar&apikey=xyz

* →    Einfacher Weg um optionale Parameter zu realisieren (wie ``**kwargs``)
* Flask legt diese Parameter als Dictionary im Request Objekt ab: ::

        @app.route('/api')
        def api_root():
            method = request.args.get('method')
            apikey = request.args.get('apikey')

            if apikey == 'xyz':
                xml_data = make_xml_response(method, apikey)
                return Response(xml_data, mimetype='text/xml')
            else:
                return 'Access Denied', 404
       


Debugging Inside #1
-------------------

**Live debugging flask applications**

::

    app.debug = True
    app.run()

|

* wird eine Flask Applikation mit ``debug = True`` gestartet, so wird im
  Browser bei Fehlern der Traceback geprintet. Dieser ist interaktiv, es
  können Variablen ausgelesen und Kommandos interaktiv abgesetzt werden.
* Da man willkürlich Code im Browser eintippen kann empfiehlt sich dieser
  Switch nicht sonderlich auf Produktivsystemen.
* Aber das war euch ja klar.



Debugging Inside #2
-------------------

**Let's demo!**

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)


    @app.route('/<name>')
    def hello(name):
        answer = 42
        if name == 'lybrial':
            raise Exception('Clitical Error.')
        else:
           return "Hello {0}," \
                  "the answer is {1}!".format(name, answer)

    if __name__ == '__main__':
        app.run(debug=True)


Server Inside *
---------------

**\*kind of**

    * Flask startet beim Starten der Applikation einen Server der Standardmäßig
      auf localhost:5000 horcht.
    
    * Server Parameter änderbar: ::

            if __name__ == '__main__':
                app.run(debug=True,
                        host='0.0.0.0',
                        port=4242)

    * ``debug`` aktiviert den live debugger über den Browser
    * ``host`` definiert die IP-Adresse auf der gelauscht werden soll
    * ``port`` definiert den Port auf dem gelauscht werden soll


Deployment Options
------------------

**Do it yourself - Deploying Flask**

* mod_wsgi (Apache) 
* Standalone WSGI Containers (Gunicorn Python WSGI HTTP Server)
* uWSGI
* FastCGI
* CGI


**Deploying Flask on Business Enterprise Platforms**

* Flask on Heroku
* Deploying WSGI on dotCloud
* Flask on Webfaction
* Google App Engine


Ausblick
--------

**Also known as**: Wozu wir keine Zeit mehr hatten:

    * Datenbankintegration. (Das ``g`` Objekt)
    * File Uploads (``request.files``)
    * Logging (``app.logger.warning(msg)``)
    * Message Flashing (``flash``)
    * Blueprints (verschiedene Seiten für Admin/User zB.)
    * Extensions (wie SQL Object Mapper)
    * Caching
    * …

Wir empfehlen auch das ausführliche Tutorial auf der Flaskseite: 

    http://flask.pocoo.org/docs/tutorial/


``moosr`` - Ein Beispielprojekt 
-------------------------------

.. image:: static/moosr.png
    :height: 500
    :align: center



Practice!
---------

|

.. raw:: html

    <h1>→ Ihr seid dran!</h1>

* Bitte die VM starten.
* Auf dem Desktop findet ihr eine ``Excercise.pdf``.
* Im Homedirectory findet ihr unter ``flascat/practice`` die Dateien.
* Unter Chromium ist ``localhost:5000`` die Startseite.
* Der Vortag ist auch auf dem Desktop verlinkt.
* Zusätzlich findet ihr den Flask Userguide dort.

.. code-block:: bash

    $ cd ~/flascat/practice
    $ gedit app.py    # Übungsdatei öffnen
    $ python app.py   # Flask Server starten
    $ python test.py  # Eure Bemühungen testen

