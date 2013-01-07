.. impress::
   :func: square

.. _python-part:

=============================================
``Ein Hochgeschwindigkeitskurs durch Python``
=============================================

.. step::
   :class: center
   :data-x: 3500
   :data-y: -1000


.. image:: static/xkcd.png
   :align: center


Vorwort
-------

.. slide::
   :data-y: 0

* Eine Stunde ist wenig Zeit um eine ganze, umfangreiche Sprache zu vermitteln, 
  geschweige denn mehr als Grundlagen zu vermitteln.
* Deshalb soll der Vortrag eher dazu dienen euren Appetit zu wecken, und euch
  ein gewisses Gefühl für die Sprache geben.
  Wenn jemand später Lust verspürt mit Python zu spielen haben wir unser Ziel erreicht.

* Hier sollen nur Grundbegriffe vermittelt und ein Ausblick gegeben werden.
  Speziell auch ein paar von Python's coolen Features.

* Falls jemand Fragen hat: einfach reinbrüllen.

* Wer dazu Lust verspürt kann auch die Beispiele selbst ausprobieren, 
  siehe nächste Folie.

* Kurzbeschreibung von Python: 

    | *Python is a general-purpose, interpreted, (optionally-),*
    | *garbage-collected, typeless high-level programming language*
    | *whose design philosophy emphasizes code readability.*

* **Paradigmen:** Object-Oriented, Imperative, Funktional, Prozedual, Reflektiv


Wozu überhaupt?
---------------

* Einsatzzwecke: 

    * … Wissenschaftlichen Bereich (``numpy``, ``SciPy`` bei NASA)
    * … Webprogrammierung (``Flask``, ``Zope``, ``Django``)
    * … Systemprogrammierung (**Admintasks**, **Networking**)
    * … Prototyping (**3-10x** Entwicklungsgeschwindigkeit)
    * … als ,,Glue'' (Compiler für C/++, Java verfügbar)
    * … integrierte ,,Scriptsprache'' (``Blender3D``, viele Spiele)
    * … Educationbereich (Primäre Sprache auf dem Raspberry)
    * … öfter als man denkt. ☻

* Andere Gründe:

    * Einfach erlernbar (Ehrlich!)
    * Meist schnell genug.
    * Plattformunabhängig.
    * … 


History!
--------

* Entstanden 1991 (älter als Java, mit 1995)

.. image:: static/guido_our_god.png
    :align: center
    :scale: 35%

* (Ursprüngliche) Designziele:

  * Als Ergänzung zu C++, Ersetzung von Shellscripts.
  * Code der sich wie einfaches Englisch liest.
  * Kurze Entwicklungszeiträume.

Wiederverwendung
----------------

  * Guido's Time Machine

    * Batteries included

  * sehr wenig Boilerplate Code
  * PEP8

| 

  **Vermeidet:**

.. image:: static/exhaustion.png
    :align: center
    :scale: 70%

Die Shell (REPL)
----------------

* Python kann interaktiv ausprobiert werden.
* Mitgeliefert gibt es die ``python`` Shell
* Auch ,,REPL'' (Read-Eval-Print-Loop) genannt:

    .. code-block:: bash
        
        $ python

    ::

        >>> a = 1 + 1
        2
        >>> print('1 + 1 =', a)
        1 + 1 = 2

* Leider: Etwas unbequem, da keine Syntaxhighlighting / Autocomplete.
* Wir empfehlen/verwenden daher **bpython**.
* Unheimlich praktisch um sich mit der Sprache vertraut zu machen.

Datentypen?
-----------

Gibts nicht. Waren zu teuer.

* Python ist eine dynamisch typisierte Sprache.
* Man verlässt sich nicht auf den Typen einer Variable, sondern auf dessen Verhalten.
* Bietet eine Klasse ``Liste`` die gleichen Funktionen wie ``Array`` so lassen sie sich gleich verwenden.

  * Ganz ohne Interfaces wie ``Iterable`` oder ``List``.
* Dieses Prinzip nennt sich ``Duck Typing``.
* Zur Laufzeit lassen sich ``Array`` und ``Liste`` mittels ``type()`` auseinanderhalten.
  
  * Aber für gewöhnlich braucht man das nicht, da sich viele Klassen ähnlich verhalten: ::

        >>> a, b = [1, 2, 3], (4, 5, 5)
        >>> print(a.count(1), b.count(5))
        1 2


Literale
--------

Strings (immer Immutable): ::

    >>> 'Hello World' # Ein Stringliteral
    >>> "Hello World" # Dasselbe (Anders als in Ruby!)
    >>> '''Geht auch  # Das ist kein Kommentar.
    ... über mehrere
    ... Zeilen'''

Numbers (auch Immutable): ::

    >>> a, b = 42, 42.21 # Ganzzahlen, Floats + Zuweisung.
    >>> a, b = 0o777, 0xDEADBEEF  # Hex/Oktal-zahlen

Zuweisungen: ::

    >>> a,b = b,a      # Swap a, b

Listen
------

Listen werden wie Arrays in anderen Sprachen genutzt: ::

    >>> pointless_list = [7, 'Apple', []]

Zugriff auf Elemente und ,,Slicing'' (wie ``subList()``):

Im Allgemeinen: ``liste[start{:end{:step}}]`` ::
    
    >>> pointless_list[0] = 42
    >>> pointless_list[0] 
    42
    >>> pointless_list[0:2]
    [42, 'Apple']
    >>> pointless_list[:-1]
    [42, 'Apple']
    >>> pointless_list[0:3:2]
    [42, []]


(In Etwa) Java-Äquivalent: ``java.util.ArrayList``

Tupel
-----

* Tupel sind wie Listen, nur mit runden Klammern + Immutable

    >>> pointless_tuple = (1, 2, 3)
    >>> pointless_tuple = 1, 2, 3
    >>> pointless_tuple[0] = 2 # Nope, TypeError.

* Tupel werden immer dann verwendet wenn man Dinge in einer bestimmten Reihenfolge packen muss.
 
  * Beispielsweise einen Vertex mit 3 Koordianten: ``(1, 0, 42)``

* Ein Tupel mit einem Element wird mit folgender Syntax deklariert: ::

    >>> one_elem_tuple = (1,) # Sieht seltsam aus
    >>> one_elem_tuple = tuple([1]) # Alternative

* Tuple Zuweisung (**wichtig!**): ::

    >>> a, b = (42, 21)

Dictionaries
------------

.. code-block:: python

    >>> pointless_dict = {
    ...  'Apple': ['juicy', 'red', 'healthy'],
    ...  'Orange': ['juicy', 'not red'],
    ...  'Watermelon': 42
    }
    >>> pointless_dict['Apple']
    ['juicy', 'red', 'healthy']
    >>> pointless_dict['Peach'] 
    <KeyError>
    >>> pointless_dict['Peach'] = 'A hairy fruit'
    >>> pointless_dict['Peach']
    'A hairy fruit'
    >>> del pointless_dict['Peach']

* Java-Äquivalent: ``java.util.HashMap``
* Dictionaries werden in Python ständig eingesetzt.


Bedingungen
-----------

.. code-block:: python

    # Beachte Einrückung statt {}!
    if 'cow' == 'dog':
        pass
    elif 1 == 2:
        pass
    else: pass

Bedingte Zuweisung:

.. code-block:: python

    >>> a = 21 if not truth else 42 # a = (truth) ? 21:42;
    42

Unwahrheitswerte (unvollständig):

.. code-block:: python

    0, 0.0, False, None, '', [], {}, set()

Sonst gilt für gewöhnlich alles als ``True``.

Schleifen 
---------

.. code-block:: python
   
    # 1,3,5,7,9            # Ungeraden Zahlen von 1-10
    for i in range(1,10,2):#
        print(i)           # 1  = Start (optional) 
                           # 10 = End 
                           # 2  = Step (optional)

    for idx, chr in enumerate('Hello'):
        print(idx, chr)    # In C-Ähnlichen Sprachen:
        if chr == 'l':     # char * s = "Hello"
            break          # for(int i=1; i<10; i+=2) {
        else:              #   printf("s[%d]=%d\n",s[i],i)
            continue       # }

* → ``range()`` und ``enumerate()`` geben Iteratoren zurück. 

.. code-block:: python
    
    while metal is True:   # while(<expression>) {
        do_something       #     do_something;
                           # }

Funktionen #1
-------------

::

    >>> # Defintion
    >>> def hello():
    ...     print('Hello')
    ...
    >>> # Redefinition
    >>> def hello():
    ...     return 'Hello'
    ...
    >>> print(hello())

    >>> # Parametrisierte Funktionen 
    >>> def doublegreet(message):
    ...     return message * 2
    ...
    >>> print(doublegreet('Hello'))
    HelloHello
    >>> print(doublegreet(message='Hello'))
    HelloHello

Funktionen #2
-------------

* **\*args** - Variable Argumentlisten ::

    def print_bracketed(*args):
        for i in args: print('[%d] ' % i)

    print_bracketed(1, 2, 3) # Prints: [1] [2] [3]
    
* **\*\*kwargs** - Variable KeyWord Paramter ::

    def print_params(**kwargs):
        for key, value in kwargs.items():
            print(key, '=>', value)

    print_params(name='Paul', job='Hauskatze')

* Alle möglichen Mischformen möglich. 
* ``kwargs`` muss als letztes stehen.
* ``args`` mindestens als vorletztes.

Exceptions
----------

Fangen: ::

    try:
        a = b
    except NameError:
        print('Du hast vergessen b zu definieren.')
    finally:
        print('Wird immer ausgeführt.')

Werfen: ::

    raise AttributeError('Keine Kuscheldecke gefunden.')

Eigene Wurfgeschosse erstellen: ::

    class OnSuccessError(Exception):
        pass

Hilfe? (…Don't Panic!)
----------------------

* Python setzt auf Selbstdokumentation, sprich auslesbare Kommentare: ::

    def make_money(papier, tinte, schein):
        '''
        Erzeugt Geld aus Papier und Tinte.

        :papier: Eine Instanz der Klasse Papier
        :tinte: Die Helligkeit der Tinte von 0-100.
        :returns: Eine neue Schein Instanz
        '''
        return Schein(papier, tinte)
    print(make_money.__doc__)


* ``RestructuredText`` ist dabei das gängige Dokumentationsformat.

   * Diese Folien sind zum Beispiel darin verfasst.
* Die offizielle Referenz/Tutorial: http://python.org/doc/
* Auch nützlich: die ``dir()`` Funktion, zum Auflisten von Membern.

Klassen #1
----------

**Überraschung**: Es gibt keine ``private`` / ``protected`` Variablen:

.. code-block:: python

    class Mom:
        def __init__(self, name):
            self.name = name
       
        def call_me_please(self):
            print('<Mom>:', self.name)

    class Son(Mom):
        def __init__(self, name):
            Mom.__init__(self, name + "'s Son")

        def call_me_please(self):
            Mom.call_me_please(self)
            print('<Son>:', self.name)

    son = Son('Peter')
    son.call_me_please() # same as: Son.call_me_please(son)

Klassen #2
----------

Properties machen das Ersetzen von Attributen mit Gettern/Settern einfach,
**ohne** dabei die Schnittstelle seiner Klasse zu ändern: :: 

    class Coffee:
        def __init__(self, vol=1):
            self._vol = vol

        def set_vol(self, new_vol): self._vol = new_vol * 3

        def get_vol(self): return self._vol

        vol = property(get_vol, set_vol)

::

    >>> mocka = Coffee()
    >>> mocka.vol = 3    # Setter Aufruf
    >>> print(mocka.vol) # Getter Afuruf
    9

Duck Typing
-----------

| „When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I **call** that bird a duck.“
| – James Whitcomb Riley

.. code-block:: python
    
    class Bird(object):
        def peep(self): print('Peep?')

    class Duck(object):
        def quak(self): print('Quak!')

    for duck in [Duck(), Bird(), dict()]:
        if hasattr(duck, 'quak'):
            duck.quak()
        else:
            print('Sieht nicht aus wie ne Ente:', duck)

Module #1
---------

Beispiel-Layout:

::

    app                  │ Import Beispiel:
    │                    │
    ├── effects          │ 
    │   ├── __init__.py  │ # In app/logic/run.py
    │   ├── sinus.py     │ >>> import app.sound.decode
    │   └── warp.py      │ ...
    │                    │
    ├── logic            │ # Use the Force:
    │   ├── __init__.py  │ >>> app.sound.decode.some_func()
    │   └── run.py       │ 
    │                    │
    ├── __main__.py      │ # Alternativ:
    ├── __init__.py      │ >>> import app.sound.decode as d 
    │                    │ >>> d.some_func()
    └── sound            │  
        ├── decode.py    │ 
        └── __init__.py  │
                         │


Module #2
---------

Andere Formen von ``import``: ::

    >>> from app.sound.decode import some_func, some_var
    >>> some_func(some_var)

Unqualifizierter Import (**Don't do it**): ::

    >>> # Bitte nicht tun da Namenskonflikte möglich:
    >>> from app.sound.decode import * 
    >>> some_func(some_var)

Lange Modulnamen können abekürzt werden: ::

    >>> import app.sounde.decode as asd
    >>> asd.some_func(asd.some_var)


Übungen
--------

**EinMalEins**:
    Schreibe ein Programm dass das 1x1 ausgibt (Formatierung egal): ::

      1x1 = 1, 1x2 = 2, ...
      2x1 = 2, 2x2 = 4, ...

**SortedList**:

    Implementiere eine Collection die sich wie eine Liste verhält,
    nur dass ``append()`` Elemente sortiert hinzufügt. 

        * Die Oberklasse sollte ``list`` sein.
        * Methoden der Oberklasse können mit ``list.obermethode(self, argumente)`` angesprochen werden.
        * Nützliche Funktionen: ``list.insert(idx, obj)``, ``list.sort()``, ``enumerate(iterable)``.

Diese Folie soll Spicken verhindern
-----------------------------------


.. image:: static/nfrench_cat.png
   :width: 550
   :align: center

----

Siehe auch: http://codingbat.com/python wer mehr Üben will ☻


``EinMalEins`` - Lösung
-----------------------

Die einfache, klare Lösung:

::

    >>> for x in range(1,11):
    ...     for y  in range(1,11):
    ...         print('%dx%d = %d' % (x, y, x * y))

Die Elegante und das Biest:

::
    
    >>> from itertools import product
    >>> ten = range(1,11)
    >>> for x,y in product(ten, ten):
    ...     print('%dx%d = %d' % (x, y, x * y))
        
::

    >>> from itertools import product
    >>> ten = range(1,11)
    >>> ['%dx%d=%d'%(x,y,x*y) for x,y in product(ten,ten)]


Diese Folie auch
----------------

.. image:: static/nmcdonald.png
    :width: 500
    :align: center

----

Für harte Männer: http://learnpythonthehardway.org/book/ (Empfehlung!) ☻

``SortedList`` - Lösung
-----------------------

::

    class SortedList(list):
        def __init__(self, iterable=[]):
            iterable.sort()
            list.__init__(self, iterable)

        def append(self, obj):
            'Append obj sorted to list'
            for i, elem in enumerate(self):
                if elem >= obj:
                    self.insert(i, obj)
                    break
            else:
                list.append(self, obj)

    sl = SortedList([3,4,8,9])
    sl.append(5)
    sl.append(0)
    sl.append(42)
    print(sl)

Operatorüberladung
------------------

Auf Wunsch von Thomas:

::

<<<<<<< HEAD
    class SimpleVec(object):
        def __init__(self, *coord):
=======
    class SillyVec(object):
        def __init__(self, coord=(0, 0, 0)):
>>>>>>> alois
            self._coord = coord

        def __iter__(self):
            return iter(self._coord)

        def __add__(self, rhs):
            self._coord = tuple(map(lambda x, y: x + y,
                                      self._coord, rhs))
            return self

<<<<<<< HEAD
        def __repr__(self):
            return repr(self._coord)
=======
        def __str__(self):
            return str(self._coord)
>>>>>>> alois

::

    __contains__, __eq__, __getitem__, __len__, __getattr__

<<<<<<< HEAD
=======

Multiple Inheritance
--------------------

Auf Wunsch von Herrn Schaible:

::

    class Base(A, B, C):
        pass

Methodenauflösung nach …

    * … Depth First.
    * … links nach rechts.
    * … Rekursiv.
    * … immer eine Instanz.
    * … Erst A rekursiv, dann B rekursiv, dann C.


|

Siehe auch Tafelbild.

>>>>>>> alois
λ!
--

Lambdas sind auch nur Funktionen:

.. code-block:: python

    fac = lambda x: 1 if x == 0 else x * fac(x-1)
    fac(23) # 25852016738884976640000

Vergleiche:

.. code-block:: java

    public long fac(long n) {
        if (n == 0) return 1;
        else        return fac(n - 1) * n;
    }

    fac(23); // 8128291617894825984 huh?

 
Python switcht bei Integer Overflows intern auf eine BigInteger Repräsentation.
Das ist zwar weniger performant als good ol' Java, aber einfach bequemer.

Multiple Inheritance
--------------------

Auf Wunsch von Herrn Schaible:

::

    class Base(A, B, C):
        pass

Methodenauflösung nach …

    * … Depth First.
    * … links nach rechts.
    * … Rekursiv.
    * … immer eine Instanz.
    * … Erst A rekursiv, dann B rekursiv, dann C.


|

Siehe auch Tafelbild.

Higher Order Functions (aka Closures)
------------------------------------------------------------

* In Python können Funktionen Funktionen zurückgeben.
* Da Funktionen auch nur Objekte sind können "spezialisierte" Funktionen auch zur Laufzeit instanziert werden.

*Beispiel*: Eine Funktion die einen speziellen Greeter zurückgibt. ::

    def greeting_generator(name):
         def greeter():
             print('Hello', name + '!')
         return greeter

::

     >>> f = greeting_generator('Python')
     >>> f()
     Hello Python!

Eine Art ``Factory`` Pattern für Funktionen.


Dekoratoren
-----------

Funktionen/Klassen können "dekoriert" werden, *ähnlich* dem aus Java bekannten Decorator-Pattern. 
Nur weitaus einfacher zu nutzen: ::

     def bold(fn):
        def wrapped(): return '<b>' + fn() + '</b>'
        return wrapped

     def italic(fn):
         def wrapped(): return '<i>' + fn() + '</i>'
         return wrapped

     @bold
     @italic
     def hello(): return 'Hello World'

::
     
     >>> hello() # Im Hintergrund: bold(italic(hello))()
     '<b><i>Hello World</i></b>'

List Comprehensions
-------------------

Wie kann man alle y in einem Intervall für eine
bestimmte Funktion berechnen? ::

    [f(x) for x in interval] # f(x) für x ∈ interval

*Beispiel*: Die Funktion 2**x im Definitionsbereich 0-9: ::

    >>> [2**x for x in range(10)]
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

Oft nutzt man Comprehensions auch für das Filtern von Listen.

*Beispiel*: Wie oben, aber nur alle ungeraden Exponenten, und als String formattiert:

.. code-block:: python

    >>> ['f(%d)=%d' %(x,2**x) for x in range(10) if x%2]
    ['f(1)=2','f(3)=8','f(5)=32','f(7)=128','f(9)=512']

Generatoren
-----------

``yield`` macht eine Funktion zum Generator:

.. code-block:: python

    # Ein erbärmlicher Random Generator
    def random42(max_num):
        for i in range(max_num):
            yield 42 ** i
    
    # Printe 10 ,,Zufallszahlen''             
    for i in random42(10):
        print(i)
 
Generator Expressions nutzen die von LH bekannten Syntax,
erzeugen die Werte aber erst beim Iterieren:

.. code-block:: python

    # Zeige alle Quadratzahlen mit ungerader Wurzel
    odd_quads = (x**2 for x in range(10) if x % 2)
    for i in odd_quads:
        print(i)

``with`` - Context Management
-----------------------------

::

    try:
        f = open('file.txt','w')
        f.write('hello world')
    finally:
        f.close()

Python way (Strichwort **RAII** in C++): ::

    with open('file.txt', 'w') as f:
        f.write('hello world')

Es lassen sich eigene Funktionen/Klassen definieren die das ``with`` Statement nutzen. 
Als Beispiel könnte man eine Mutex-Klasse implementieren: ::

    with locked(some_mutex):
        do_something_while_locked()

Die Philosophie
---------------

|

**Pragma statt Dogma!**
    Es gibt keinen ,,goldenen Hammer''.
**Zen of Python:**
    In der Python-Shell abrufbar als: ``import this``
**Explizit ist besser als Implizit**
    Siehe beispielsweise explitizes ``self`` statt implizites ``this``.
**Batteries included**
    Große Standardbibliothek mit vielen Funktionen.
**Man liest Code öfters als man ihn schreibt.**
    Und man sollte ihn nicht widerwillig lesen müssen.
**Programmieren sollte Spass machen.**
    Gegen Compiler/Sprache/Konfiguration kämpfen macht wenig Spaß.
    


It's short!
-----------

.. code-block:: python

    #!/usr/bin/env python
    # encoding: utf-8
    import sys, pprint, os, hashlib

    def find_dups(path):
      hashes, dups = {}, {}
      for path, dirs, files in os.walk(path):
        abspathes = (os.path.join(path, n) for n in files)
        for fpath in filter(os.path.isfile, abspathes):
          with open(fpath, 'r') as f:
            md5 = hashlib.md5(f.read()).hexdigest()

          if hashes.setdefault(md5, fpath) is not fpath:
            at = dups.setdefault(md5, [hashes[md5]])
            at.append(fpath)
      return dups
    
    if __name__ == '__main__':
        pprint.pprint(find_dups(sys.argv[1]))


Unit-Testing
------------

Das Testframework ist mit dem Modul ``unittest`` in die Sprache eingebaut: ::

    import unittest

    def greeter(name): return 'Hello ' + name + '!'

    class TestGreeter(unittest.TestCase):
        def setUp(self):
            self.test_name = 'Workshop'

        def test_greeter(self):
            self.assertEqual(greeter(self._test_name),
                       'Hello ' + self.test_name + '!')

        def tearDown(self):
            self.test_name = ''

    if __name__ == '__main__':
        unittest.main()

Python2 vs. Python3
-------------------

Auf Python3 Seite:

    * Einfache Unicodeünterstützung.
    * Alles leitet von ``object`` ab.
    * Syntaxänderungen und Änderungen an der C-API.

    * Leider **inkompatibel** zu Python2.
      
      * Viele Features aber backported.

    * Manche externe Libraries **noch** Python2 basiert (Flask)!

       * Python2 wird allerdings noch lange supported.

* Oft noch Python 2 per Default installiert (Debian, Mac OS X).
* Für die Übungen / Flask wird Python2 verwendet!
* (Fast) Alle Beispiele liefen in beiden Versionen.

.. raw:: html

    <h2>Python2 is the present, Python3 the future.</h2>

Interpreter / Compiler
----------------------

|
|

Es gibt eine Reihe verschiedener Intepreter / Compiler für Python:

* ``CPython`` - Der *Referenz* Interpreter. 
* ``Jython`` - Ein ByteCode Compiler für die JVM. **\***
* ``IronPython`` - Die .Net Variante von ``Jython``.
* ``Cython`` - Übersetzt Python zu C-Code. **\***
* ``PyPy`` - Ein Interpreter/JIT Compiler in Python.
* ``Stackless Python`` - Interpreter; Verbesserter Threadingsupport.

----

|

**\*** Es handelt sich um Spracherweiterungen.

Fragen?
-------

*Beispielsfrage #1*: **Mit was wurde die Präsentation gemacht?**

----

    Blut, Spucke, Python und HTML.

    Genau genommen mit ``python-impress`` gerendert:  http://www.github.com/gawell/impress

----

*Beispielsfrage #2*: **Machen wir 5 Minuten Pause?**

    Ja.

----

*Beispielfrage #3*: **Wo gibts die Folien und den Rest des Workshops?**

    Folien/Übungen sind verfügbar unter: http://www.github.com/studentkittens/flascat
