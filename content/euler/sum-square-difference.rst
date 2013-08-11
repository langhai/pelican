Sum Square Difference
#####################################

:date: 29-05-2013
:tags: project euler, python, algorithm, math
:category: Code!
:slug: sum-square-difference
:author: Hai Lang
:status: published

.. epigraph::
    The difference between the sum of the squares of the first ten natural 
    numbers and the square of the sum is 3025  385 = 2640. Find the difference 
    between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Sixth question from `Project Euler`_.

Sum Square Difference (SSD) is commonly used in image processing, but this question is rather simple.

For the sum of squares of the first 100 natural numbers,

.. code-block:: python

    sumsqr = (1 ** 2 + 2 ** 2 + ... 100 **2)

And for the square of the sum,

.. code-block:: python

    sqrsum = (1 + 2 + ... + 100) ** 2

A simple loop will do the job.

.. code-block:: python

    sumsqr, sqrsum = 0

    for i in ((x, x ** 2) for x in xrange(1, 101)):
        sqrsum += i[0]
        sumsqr += i[1]

    print sqrsum ** 2 - sumsqr
    #25164150

The answer is **25164150**. Easy enough.

*<< EOF*

.. _`Project Euler`: http://projecteuler.net/problem=6
