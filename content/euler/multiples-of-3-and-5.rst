Multiples of 3 and 5
###############################################

:date: 31-01-2013
:tags: project euler, python, algorithm, math
:category: Code!
:slug: multiples-of-3-and-5
:author: Hai Lang
:status: published

.. highlights:: 
    So I was extremly bored, to a degree that I started reading new threads on `Hacker News`_ and accidentally saw
    a guy `Failed, Failed, and Finally Succeeded at Learning How to Code`_, the `Project Euler`_ he mentioned saved 
    my day.

Interesting stuff, there are like 400-something computational problems on that site, which according to that guy

.. pull-quote::
    Has trained tens of thousands of new programmers.

I started right away to the first problem, suppose to be a pretty easy one.

.. highlights:: 
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. 
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 10000.

Turns out it is indeed easy. A loop to find all multiples of 3 or 5 that are below 10000, and add them together, kids stuff.

.. code-block:: python

    [$] <git:(master?)> python2
    Python 2.7.3 (default, Dec 22 2012, 21:14:12) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print "The answer is: " + str(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))
    The answer is: 233168
    >>> 

Say x is the multiple of either 3 or 5, at least 1 of the remainder of x % 3 or x % 5 should be 0. 
Then all we have to do is to find x in the range of 1 to 1000, put them in a list and sum these numbers.

Here's an elaborated way to do this

.. code-block:: python

    result = 0
    for x in range(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    print result

That's all for problem 1, easy, but fun. Hopefully I'll keep getting bored and go through all questions from 
Project Euler.

*<< EOF*

.. _`Project Euler`: http://projecteuler.net/problem=1
.. _`Hacker News`: http://news.ycombinator.com
.. _`Failed, Failed, and Finally Succeeded at Learning How to Code`: http://www.theatlantic.com/technology/print/2011/06/how-i-failed-failed-and-finally-succeeded-at-learning-how-to-code/239855/#

