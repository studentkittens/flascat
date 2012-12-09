Flascat
=======

Description
-----------

A demonstration of Flask, a Python microwebframework.
Also included: 

    * A Python Crashcourse in ``presentation/html/index.html``.
    * The slides rendered as PDF: ``presentation/Flask.pdf``
    * Slides for Introducing Flask in ``presentation/html``.
    * An example app in ``moosr/`` (A music-metadata search website).
      Read here for extended stuff! :-)
    

Structure
---------

``moosr/``
    
    Actual moosr application. To start it use:
    .. code-block:: bash
    
        moosr/ $ python moosr.py
        chromium localhost:5000

    ``moosr/static/``

        Home of CSS.

    ``moosr/templates/`` 

        Jinja2 Templates.

``presentation/``

    Source (``*.rst``) & Rendered Presentation (``html/index.html``)

``webmarketing/``

    Other Stuff. :-)

``practice/``

    The practice we hold for the presentation. Includes a PDF with the
    description. 

    Under ``solution.py`` you'll find a possible solution!
