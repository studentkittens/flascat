.. impress::
   :func: square2

=============================================
Ein **Hochgeschwindigkeitskurs** durch Python
=============================================

.. step::
   :class: center
   :data-x: 3500
   :data-y: -1000

.. image:: http://abstrusegoose.com/strips/batteries_included.PNG
   :height: 300
   :align: left

Vorwort
-------

.. slide::
   :data-x: 0
   :data-y: 0

* Eine Stunde ist wenig Zeit um eine ganze, umfangreiche Sprache zu vermitteln, 
  geschweige denn sie auch nur im Ansatz zu verstehen.
* Deshalb soll der Vortrag eher dazu dienen euren Appetit zu wecken, und euch
  ein gewisses Gefühl für die Sprache geben.

  * Wenn jemand später Lust verspürt mit Python zu spielen haben wir unser Ziel erreicht.

* Hier sollen nur Grundbegriffe vermittelt und ein Ausblick gegeben werden.

  * Speziell auch ein paar von Python's coolen Features.

* Falls jemand Fragen hat: einfach reinbrüllen.

* Wer dazu Lust verspürt kann auch die Beispiele selbst ausprobieren, 
  siehe nächste Folie.

Die Shell (REPL)
----------------

* Python kann interaktiv ausprobiert werden.
* Mitgeliefert gibt es die ``python`` Shell
* Auch ,,REPL'' (Read-Eval-Print-Loop) genannt: ::

    $ python 
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

* Python ist eine untypisierte Sprache.
* Man verlässt sich nicht auf den Typen einer Variable, sondern auf dessen Verhalten.
* Bietet eine Klasse ``Liste`` die gleichen Funktionen wie ``Array`` so lassen sie sich gleich verwenden.

  * Ganz ohne Interfaces wie ``Iterable`` oder ``List``.
* Dieses Prinzip nennt sich ``Duck Typing``.
* Zur Laufzeit lassen sich ``Array`` und ``Liste`` mittels ``type()`` auseinanderhalten.
  
  * Aber für gewöhnlich braucht man das nicht.

::

    a = []


Literale
--------

Strings: ::

    'Hello World' # Ein Stringliteral
    "Hello World" # Dasselb (Anders als in Ruby!)

    '''Geht auch  # Das ist kein Kommentar.
    über mehrere
    Zeilen'''

Numbers: ::

    a, b = 42, 42.21 # Ganzzahlen, Floats + Zuweisung.
    a, b = 0o777, 0xDEADBEEF  # Hex/Oktal-zahlen

Zuweisungen: ::

    a,b = b,a      # Swap a, b

List
----

Listen werden wie Arrays in anderen Sprachen genutzt:

.. code-block:: python

    pointless_list = [42, 'Apple', []]

Zugriff auf Elemente und ,,Slicing'' (wie ``subList()``).

Im Allgemeinen: ``liste[start{:end{:step}}]`` ::
    
    pointless_list[0]     # 42
    pointless_list[0:1]   # 42, 'Apple'
    pointless_list[1:]    # 'Apple', [] 
    pointless_list[:1]    # 42, 'Apple' 
    pointless_list[0:3:2] # 42, []
    pointless_list[::-1]  # [], 'Apple', 42


(In Etwa) Java-Äquivalent: ``java.util.ArrayList``

Tupel
-----

* Tupel sind wie Listen, nur dass sie Immutable sind. 
* Statt mit eckigen Klammern werden sie mit runden Klammern definiert: ::

    pointless_tuple = (1, 2, 3)
    pointless_tuple[0] = 2 # Nope, TypeError.

* Tupel werden immer dann verwedent wenn man Dinge in einer bestimmten Reihenfolge packen muss.
 
  * Beispielsweise einen Vertex mit 3 Koordianten: ``(1, 0, 42)``

* Ein Tupel mit einem Element wird mit folgender Syntax deklariert: ::

    one_elem_tuple = (1,) # Sieht seltsam aus

    # Alternativ:
    one_elem_tuple = tuple([1])

Dictionaries
------------

.. code-block:: python

    pointless_dict = {
        'Apple': ['juicy', 'red', 'healthy'],
        'Orange': ['juicy', 'not red'],
        'Watermelon': 42
    }

    pointless_dict['Apple'] # ['juicy', 'red', 'healthy']
    
    # throws a ,,KeyError''
    pointless_dict['Peach'] 

    pointless_dict['Peach'] = 'A hairy fruit'
    pointless_dict['Peach']  # => liefert 'A hairy fruit'

* Java-Äquivalent: ``java.util.HashMap``
* Dictionaries werden in Python ständig eingesetzt.


Bedingungen
-----------

.. code-block:: python
    
    if <expr>:
        pass
    elif <expr>:
        pass
    else:
        pass

Bedingte Zuweisung:

.. code-block:: python

    a = <val_on_truth> if <expr> else <val_on_untrue>

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
    # 0-9                 # 2  = Step (optional)
    for i in range(10):   # 
         print(i)         # In C-Ähnlichen Sprachen:
                          # for(int i=1; i<10; i+=2) {
                          #   printf("%d\n", i)
                          # }

* → ``range(10)`` gibt ein Iterator zurück. 

.. code-block:: python
    
    while <expr>: # while(<expr>) {
        pass      #     do_something;
                  # }

Funktionen #1
-------------

::

    # Defintion
    def hello():
        print('Hello')

    # Redefinition
    def hello():
        return 'Hello'

    # Aufruf
    print(hello())

    def doublegreet(message):
        return message * 2

    # Parametrisierter Aufruf
    print(doublegreet('Hello')) # HelloHello

    # Benannte Parameter:
    print(doublegreet(message='Hello')) # -"-

Funktionen #2
-------------

* **\*args** - Variable Argumentlisten ::

    def print_bracketed(*args):
        for i in args: print('[%d] ' % i)

    print_bracketed(1, 2, 3) # Prints: [1] [2] [3]
    
* **\*kwargs** - Variable Paramter ::

    def print_params(**kwargs):
        for key, value in kwargs.items():
            print(key, '=>', value)

    print_params(name='Paul', job='Hauskatze')

* Alle möglichen Mischformen möglich. 
* ``kwargs`` muss als letztes stehen
* ``args`` mindestens als vorletztes

Exceptions
----------

Fangen: ::

    try:
        a = b
    except NameError:
        print('Du hast vergessen b zu definieren.')
    finally:
        print('Wird immer ausgeführt')

Werfen: ::

    raise AttributeError('Kein Pelz.')

Wurfeschosse erstellen: ::

    class OnSuccessError(Exception):
        pass

Getting Help
------------

* Use bpython
* Use the ``__doc__`` member
* Use ``dir()``
* Die offziele Referenz. Empfehlenswert:

  http://python.org/doc/


TODO

Klassen
-------

TODO

.. code-block:: python

    class A(object):
        def __init__(self, name):
            self.name = name
       
        def call_me_please(self):
            print('Mom:', self.name)

    class B(A):
        def __init__(self, name):
            A.__init__(name)    

        def call_me_please(self):
            print('Son:', self.name)

    son = B('Peter')
    son.call_me_please() # same as: B.call_me_please(son)

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
    │   ├── sinus.py     │ import app.sound.decode
    │   └── warp.py      │ ...
    │                    │
    ├── logic            │ # Use the Force:
    │   ├── __init__.py  │ app.sound.decode.some_func()
    │   └── run.py       │ 
    │                    │
    ├── __main__.py      │ # Alternativ:
    ├── __init__.py      │ import app.sound.decode as adc
    │                    │
    └── sound            │ ... 
        ├── decode.py    │ adc.some_func()
        └── __init__.py  │
                         │


Module #2
---------

Andere Formen von ``import``:

.. code-block:: python
    
    from app.sound.decode import some_func, some_var

    some_func(some_var)

.. code-block:: python

    # Not recommmended:
    from app.sound.decode import * 

    some_func(some_var)

Lange Modulnamen können abekürzt werden:

.. code-block:: python

    import app.sounde.decode as asd

    asd.some_func(asd.some_var)


Übungen
--------

TODO

**1x1**:
    Schreibe ein Programm dass das 1x1 zeilenweise ausgibt: ::

      1x1 = 1, 1x2 = 2, ...
      2x1 = 2, 2x2 = 4, ...

**ZooP**:
    Schreibe eine Klasse Tier die eine Methode ``make_loud`` 
    bereitstellt. Leite von dieser eine Klasse ``Katze`` ab,
    und überschreibe die ``make_loud`` Methode. 

    Stecke Instanzen der Objekte in eine Liste ``Zoo``.
    Durchlaufe diese Liste und stelle fest ob es sich beim Objekt 
    um eine Katze handelt.

----

Siehe auch: http://codingbat.com/python

1x1 Lösung
----------

.. code-block:: python

    # The clear one.
    for x in range(1,10):
        for y  in range(1,10):
            print('%dx%d = %d' % (x, y, x * y))
        print()

.. code-block:: python
    
    # The cool/performant one. 
    from itertools import product

    ten = range(1,10)
    for x,y in product(ten, ten):
        print('%dx%d = %d' % (x, y, x * y))
        
.. code-block:: python

    # The oblivious one-liner.
    from itertools import product
    ten = range(1,10)
    ['%dx%d=%d'%(x,y,x*y) for x,y in product(ten,ten)]


Zoo OOP
-------

TODO

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


Spezielle Features
==================

.. step::
   :class: center
   :data-x: 3500
   :data-y: -1000

Python hat einige Features die es von vielen kompilierten und
interpretierten Sprachen abheben.

Higher Order Functions (aka FunktionenDieFunktionenReturnen)
------------------------------------------------------------

* In Python können Funktionen Funktionen zurückgeben.
* Da Funktionen auch nur Objekte sind können "speziliasierte" Funktionen auch zur Laufzeit instanziert werden.

*Beispiel*: Eine Funktion die einen speziellen Greeter zurückgibt. 

.. code-block:: python

     def greeting_generator(name):
         def greeter():
             print('Hello', name + '!')
         return greeter

     f = greeting_generator('Python')
     f() # Hello Python!

in Java vielleicht am ehesten vergleichbar mit dem ``Factory`` Pattern.


Dekoratoren
-----------

Funktionen/Klassen können "dekoriert" werden, ähnlich dem aus Java bekannten Decorator-Pattern. 
Nur weitaus einfacher zu nutzen:

.. code-block:: python

     def bold(fn):
        def wrapped(): return '<b>' + fn() + '</b>'
        return wrapped

     def italic(fn):
         def wrapped(): return '<i>' + fn() + '</i>'
         return wrapped

     @bold
     @italic
     def hello():
         return 'Hello World'

     # Entspricht: bold(italic(hello()))
     print(hello()) # => <b><i>Hello World</i></b>

List Comprehensions
-------------------

Wie kann man alle y in einem Intervall für eine
bestimmte Funktion berechnen? ::

    [f(x) for x in interval] # f(x) für x ∈ interval

*Beispiel*: Die Funktion 2**x im Definitionsbereich 0-9:

.. code-block:: python

    print([2**x for x in range(10)])
    # = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

Oft nutzt man Comprehensions auch für das Filtern von Listen.

*Beispiel*: Wie oben, aber nur alle ungeraden Exponenten, und als String formattiert:

.. code-block:: python

    print(['f(%d)=%d' %(x,2**x) for x in range(10) if x%2])
    # = ['f(1)=2','f(3)=8','f(5)=32','f(7)=128','f(9)=512']

Generatoren
-----------

``yield`` macht eine Funktion zum Generator:

.. code-block:: python

    # Ein mieser Random Generator
    def random42(max_num):
        for i in range(max_num):
            yield 42 ** i
    
    # Printe 10 ,,Zufallszahlen''             
    for i in random42(10):
        print(i)
 
Überfordert? Dann jetzt was einfaches:

.. code-block:: python

    # Zeige alle Quadratzahlen,
    # deren Wurzel ungerade ist:
    odd_quads = (x**2 for x in range(10) if x % 2)
    for i in odd_quads:
        print(i)

``with`` 
--------

Usual way: ::

    try:
        f = open('file.txt','w')
        f.write('hello world')
    finally:
        f.close()

Python way: ::

    with open('file.txt', 'w') as f:
        f.write('hello world')

Es lassen sich eigene Funktionen/Klassen definieren die das ``with`` Statement nutzen. 
Als Beispiel könnte man eine Mutex-Klasse implementieren: ::

    with locked(some_mutex):
        do_something_while_locked

Die Philosophie
---------------

**Zen of Python:**
    In der Python-Shell abrufbar als: ``import this``
**Explizit ist besser als Implizit**
    Siehe beispielsweise explitizes ``self`` statt implizites ``this``.
**Batteries included**
    Große Standardbibliothek mit vielen Funktionen.
**Man liest Code öfters als man ihn schreibt.**
    Und man sollte ihn nicht widerwillig lesen müssen.
**Programmieren sollte Spass machen.**
    Gegen Compiler/Sprache kämpfen macht wenig Spaß.


Python ist sehr kurz
--------------------

.. code-block:: python

    #!/usr/bin/env python
    # encoding: utf-8
    import sys, pprint, os, hashlib
    hashes, dups = {}, {}

    for path, dirs, files in os.walk(sys.argv[1]):
        # Make path absolute, filter by regular files
        abspathes = (os.path.join(path, n) for n in files)
        for fpath in filter(os.path.isfile, abspathes):
            # Compute a md5sum of the file content
            with open(fpath, 'r') as f:
                md5 = hashlib.md5(f.read()).hexdigest()

            # Remember this hash, and if there, add as dup
            if hashes.setdefault(md5, fpath) is not fpath:
                at = dups.setdefault(md5, [hashes[md5]])
                at.append(fpath)

    pprint.pprint(dups)


Sonstiges
---------

Mit ``python-impress`` gerendert:  http://www.github.com/gawell/impress
