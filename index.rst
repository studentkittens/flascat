.. impress::
   :hide-title: True
   :data-scale: 1

Einführung der Kinder in Schlangen
==================================

Unterschiede Python2 vs. Python3
--------------------------------

* Search the Web.

Datentypen
----------

* strings
* numbers
* list

    .. code-block:: python
        
        mylist = [1, 42, 23]
        mylist[2]    # 23
        mylist[1:]   # 42, 23
        mylist[:1]   # 1, 42
        mylist[::-1] # 23, 42, 1

* dict
* set


Getting Help
------------

* Use bpython
* Use the ``__doc__`` member
* Use ``dir()``

Bedingungen
-----------

.. code-block:: python
    
    if <expr>:
        pass
    elif <expr>:
        pass
    else:
        pass


Schleifen und Iteratoren
------------------------

.. code-block:: python
    
    for i in range(1,10,2):
        print(i)

    # Alle ungeraden Zahlen von 1-10
    # range([Anfang, ] Ende [, Step])
    # 1  = Anfang (optional)
    # 10 = Ende 
    # 2  = Step (optional)
    # 
    # In C-Ähnlichen Sprachen:
    # for(int i = 1; i < 10; i += 2) {
    #   printf("%d\n", i)
    # }

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
    ├── effects          │ 
    │   ├── __init__.py  │ # In app/logic/run.py
    │   ├── sinus.py     │ import app.sound.decode
    │   └── warp.py      │ ...
    ├── __init__.py      │
    ├── logic            │ # Use the Force:
    │   ├── __init__.py  │ app.sound.decode.some_func()
    │   └── run.py       │ 
    ├── __main__.py      │ # Alternativ:
    ├── __init__.py      │ import app.sound.decode as dc
    └── sound            │ ... 
        ├── decode.py    │ dc.some_func()
        └── __init__.py  │


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


How short Python can be
-----------------------

Finde alle Duplikate in einem übergebenen Pfad:

.. code-block:: python

    #!/usr/bin/env python
    # encoding: utf-8

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
