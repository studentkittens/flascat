.. impress::
   :hide-title: True
   :data-scale: 1

==============
My fisrt slide
==============

.. slide::
   :class: first

Einführung der Kinder in Schlangen
==================================

test

Basics
------

* Bedingungen
* Datentypen
* Schleifen 
* Iteratoren
* Klassen
* Module

λ!
--

Lambdas sind auch nur Funktionen:

.. code-block:: python

    fact = lambda x: 1 if x == 0 else x * fact(x-1)
    fact(23) # 25852016738884976640000

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

Python hat ein paar Features die es von den allermeisten
kompilierten Sprachen hervorheben. 

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

List Comprehensions
-------------------

Alle 2er Potenzen von 0 - 10:

.. code-block:: python

    mylist = [2**x for x in range(10)]
    # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

Dasselbe, aber nur alle ungeraden 2er Potenzen,
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
    for i in (x**2 for x in range(10) if x % 2):
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


``import this``
---------------
Zen of Python +  **Batteries included** 

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
            print 'Sieht nicht aus wie ne Ente:', duck

    #

How short Python can be
-----------------------

XML Zeugs ( kitteh ).
