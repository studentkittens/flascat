Einführung der Kinder in Schlangen
==================================

Unterschiede Python2 vs. Python3
--------------------------------

* Search the Web, dude.

Die Shell (REPL)
----------------

* Python kann interaktiv ausprobiert werden.
* Mitgeliefert gibt es den ``python`` - die REPL (Read-Eval-Print-Loop) ::

    $ python 
    >>> 1 + 1
    2
    >>> print('Oooh!')

* Leider: Etwas unbequem, da keine Syntaxhighlighting / Autocomplete.
* Wir empfehlen **bpython**.


Datentypen
----------

* Python ist eine untypisierte Sprache. So what?
* Man verlässt sich nicht auf den Typen einer Variable, sondern auf dessen Verhalten.
* Bietet eine Klasse ``Liste`` die gleichen Funktionen wie ``Array`` so lassen sie sich gleich verwenden.

  * Ganz ohne Interfaces wie ``Iterable``.
* Dieses Prinzip nennt sich ``Duck Typing``.
* Zur Laufzeit lassen sich ``Array`` und ``Liste`` mittels ``type()`` auseinanderhalten.
* Viele sehr oft genutzte Datenstrukturen sind in Python bereits implementiert.

  * Die meisten davon kommen in den nächsten Folien.

Strings
-------

.. code-block:: python

    'Hello World' # Ein Stringliteral
    "Hello World" # Vollkommen dasselbe
                  # (Unterschied zu zB Ruby!)

    '''Geht auch
    über mehrere
    Zeilen'''

    s = 'My String' # Zuweisung  

Numbers
-------

.. code-block:: python

    a = 42         # Integer
    b = 23.21      # Floats
    0o777          # Oktalzahlen
    0xDEADBEEF     # Hexzahlen
    a,b = b,a      # Swap a, b
    truth = True   # Auch ein Integer.
    tigges = False # Ebenfalls. 

    # True/False sind globale Variablen.
    # Don't do that. Really.
    True, False = False, True 

    # Wenn es True/False nicht gäbe:
    True, False = not 0, 0

List
----

.. code-block:: python

    mylist = [42, 'Apple', []]
    mylist[2]    # [] 
    mylist[1:]   # 'Apple', [] 
    mylist[:1]   # 42, 'Apple' 
    mylist[::-1] # [], 'Apple', 42

Dictionaries
------------

.. code-block:: python

    mydict = {
        'Apple': ['juicy', 'red', 'healthy'],
        'Orange': ['juicy', 'not red'],
        'Watermelon': 42
    }

    mydict['Apple'] # ['juicy', 'red', 'healthy']
    mydict['Peach'] # throws a ,,KeyError''
    mydict['Peach'] = 'A hairy fruit'
    mydict['Peach'] # 'A hairy fruit'

Java-Äquivalent: ``java.util.HashMap``


Dictionaries werden in Python ständig eingesetzt.


Getting Help
------------

* Use bpython
* Use the ``__doc__`` member
* Use ``dir()``
* Die offziele Referenz. Empfehlenswert:

  http://python.org/doc/

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

Unwahrheitswerte:

.. code-block:: python

    0, 0.0, False, '', [], {}, set()

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
.. code-block:: python
    
    while <expr>: # while(<expr>) {
        pass      #     do_something;
                  # }

Funktionen #1
-------------

Funktionen #1
-------------

Exceptions
----------

Klassen
-------

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
    ├── __init__.py      │ import app.sound.decode as dc
    │                    │
    └── sound            │ ... 
        ├── decode.py    │ dc.some_func()
        └── __init__.py  │
                         │


Module #2
---------

Andere Formen von ``import``:

.. code-block:: python
    
    from app.sound.decode import some_func, some_var

.. code-block:: python

    # Not recommmended:
    from app.sound.decode import * 


Übungen
--------

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

Lösungen
--------

**1x1**:
    ...

**ZooP**:
    ...


λ!
--

Lambdas sind auch nur Funktionen:

.. code-block:: python

    fac = lambda x: 1 if x == 0 else x * fac(x-1)
    fac(23) # 25852016738884976640000

Vergleiche:

.. code-block:: java

    public long fac(long n) {
        if (n == 0)
            return 1;
        else
            return fac(n - 1) * n;
    }

    fac(23); // 8128291617894825984 huh?

 
Python switcht bei Integer Overflows intern auf eine BigInteger Repräsentation.
Das ist zwar weniger performant als good ol' Java, aber einfach bequemer.


Spezielle Features
==================

Python hat einige Features die es von vielen kompilierten und
interpretierten Sprachen abheben.

Higher Order Functions
----------------------

.. code-block:: python

     def greeting_generator(name):
         def greeter():
             print('Hello', name + '!')
         return greeter

     f = greeting_generator('Python')
     f() # Hello Python!


Dekoratoren
-----------
    
.. code-block:: python

     def bold(fn):
        def wrapped():
            return '<b>' + fn() + '</b>'
        return wrapped

     def italic(fn):
         def wrapped():
            return '<i>' + fn() + '</i>'
         return wrapped

     @bold
     @italic
     def hello():
         return 'Hello World'

     print(hello()) # <b><i>Hello World</i></b>
     # Entspricht: bold(italic(hello()))

List Comprehensions
-------------------

Alle 2er Potenzen von 0 - 10:

.. code-block:: python

    mylist = [2**x for x in range(10)]
    # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

Dasselbe, aber nur mit allen ungeraden Exponenten,
und als ``hex`` String repräsentiert:

.. code-block:: python

    mylist = [hex(2**x) for x in range(10) if x % 2]
    # ['0x2', '0x8', '0x20', '0x80', '0x200']

Generatoren
-----------

.. code-block:: python

     def random_generator(max_num):
         for i in range(max_num):
             yield random()
                               
     for i in random_generator(10):
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

Usual way:

.. code-block:: python
    
    try:
        f = open('file.txt','w')
        f.write('hello world')
    finally:
        f.close()

Python way:

.. code-block:: python

    with open('file.txt', 'w') as f:
        f.write('hello world')


Die Philosophie
---------------

* Zen of Python: ``import this``
* Explizit ist besser als Implizit.
* **Batteries included**: Viele Funktionen bereits integriert
* Man liest Code öfters als man ihn schreibt.
* Programming should be fun.


Python ist kurz
---------------

.. code-block:: python

    #!/usr/bin/env python
    # Finde alle Duplikate in einem übergebenen Pfad

    import sys, pprint, os, hashlib

    hashes, dups = {}, {}

    for path, dirs, files in os.walk(sys.argv[1]):
        for filename in files:
            fullname = os.path.join(path, filename)
            with open(fullname, 'r') as f:
                md5 = hashlib.md5(f.read()).hexdigest()
            if hashes.get(md5):
                if not dups.get(md5):
                    dups[md5] = [hashes[md5]]
                dups[md5].append(fullname)
            else:
                hashes[md5] = fullname
    pprint.pprint(dups)
