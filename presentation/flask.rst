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

.. image:: static/pycake.png
    :width: 500
    :align: center

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
        return redirect('http://www.google.de')
    
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

Request Object 
--------------

**Login Funktion**

.. code-block:: python

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':  
            if valid_login(request.form['user'],  
                           request.form['pass']): 
                return log_the_user_in(request.form['user'])
            else:
                error = 'Invalid user/pass'
        return render_template('login.html', error=error)

**Anmerkung**

    * über ``request.method`` wird die HTTP Methode geprüft
    * über ``request.form`` können Formulare ausgelesen werden




Session Object #1
-----------------

**Codeblock um Login zu realisieren**

.. code-block:: python

    @app.route('/')
    def index():
        if 'user' in session:
            return 'Logged in as %s' % escape(session['user'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['user'] = request.form['user']
            return redirect(url_for('index'))
        return '''


Session Object #2
-----------------

**Session Management**

.. code-block:: python

    @app.route('/login', methods=['GET', 'POST'])
            session['user'] = request.form['user']
            return redirect(url_for('index'))
        return '''


**HTML Formular**

.. code-block:: html
    
        <form action="" method="post">
            <p><input type=text name=user>
            <p><input type=submit value=Login>
        </form>
        


Debugging Inside
----------------

**Live debugging flask applications**

.. code-block:: python

    app.debug = True
    app.run()

* wird eine Flask Applikation mit ``debug = True`` gestartet, so wird im
  Browser bei Fehlern der Traceback geprintet. Dieser ist interaktiv, es
  können Variablen ausgelesen und Kommandos interaktiv abgesetzt werden
* Demo


Server Inside *
---------------

**\*kind of**

    * Flask startet beim Starten der Applikation einen Server der Standardmäßig
      auf localhost:5000 horcht
    
    * Server Parameter änderbar

        .. code-block:: python

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



moosr - music metadata search engine
------------------------------------

.. image:: static/moosr.png
    :height: 400
    :align: center

Unsere kleine Beispielseite mit Flask.


Übung
-----
