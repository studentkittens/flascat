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

.. image:: http://flask.pocoo.org/static/logo/flask.png
    :width: 500
    :align: center

|

``http://flask.pocoo.org/``

What?
-----

.. slide::
   :data-x: 0
   :data-y: 0

* Flask ist ein **Microwebframework**.
* Fokus: Erweiterbarkeit + gute Dokumentation.
* Abhängigkeiten:

    * ``Werkzeug``:
    * ``Jinja2``: Eine Template Engine

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

Python2 only :-(

Vergleich zu Django

Austauschbare Template engine, DB

Features
--------

list features, schön erklären und soweiter.

Hello World!
------------

Die folgende Anwendung wird auf ``localhost:5000`` 
horchen und bei einem ``GET``
einem unformattieren **Hallo Welt** ausgeben.

::

    # Importiere die Flask Libraries, 
    # und instanziere eine Flask-Anwendung.
    import flask
    app = flask.Flask(__name__)
     
    # hello() soll für ein Zugriff auf 
    # die root-url aufgerufen werden.
    @app.route("/")
    def hello():
        return "Hallo Welt"
    
    # Falls das Skript direkt ausgeführt wird,
    # so lasse die Anwendung laufen.
    if __name__ == "__main__":
        app.run(debug=True)

Routing & Troubleshooting
-------------------------

app.route etc.

http verben

url_for

static files

Templates & How to render them
------------------------------

render_template()

Jinja templates

Request Data
------------

POST 

Sessions
--------

login beispiel

Debugging
---------

Show the Debugger
