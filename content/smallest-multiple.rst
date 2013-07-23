Smallest Multiple
#####################################

:date: 28-05-2013
:time: 14:30
:tags: project euler, python, algorithm, math
:category: Code!
:slug: smallest-multiple
:author: Hai Lang
:status: published

.. epigraph::
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Fifth question from `Project Euler`_.

Given that 2520 is evenly divisible by numbers from 1 to 10, which means it is always true that 

.. code-block:: python

    2520 % x = 0 (0<x<11)

Now 2520 is called the `Least Common Multiple (LCM)`_ of X = [1, 2, ..., 10]

The most straight forward method to find the LCM for 1 to 20 is to use a loop and check on every stepping 
if the next number can be divided by 1 to 20. But this will probably take too long (The answer is more than 
100 million)

We can try to reduce the size of the set X to speed up the process. 1 for instance, can be removed from the list
since all positive whole numbers are divisible by 1. Furthermore, if a number is divisible by 20, then it must be
divisible by 2, 4, 5, and 10. We'll end up with a list looks like

.. code-block:: python

    X = [11,13,14,16,17,18,19,20]

Now since it is always true that 

.. code-block:: python

    (x1 * x2 * x3 * ... * xn) % x1 = 0

So that if we were to multiply all the numbers in X, we get 3724680960 which is divisible by every number in X.
We can say that 3724680960 is a common multiple, but it is unlikely the least common multiple.

The LCM can be calculated by dividing 3724680960 by the `Greatest Common Divisor (GCD)`_ of X.

For instance 

.. code-block:: python

    Y = [6, 9]
    #Then we have
    multiple = 6 * 9 = 54
    #And
    GCD(Y) = 3
    #Since
    54 = 6 * 9 = 3 * 2 * 3 * 3
    #Then
    LCM(Y) = multiple / GCD(Y) = 3 * 2 * 3 * 3 / 3 = 18 

`Euclidean Algorithm`_ can be used to calculate GCD of two integers very fast.

.. code-block:: python

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

For instance, gcd(6, 9) will have

.. list-table:: Euclidean Algorithm
    :header-rows: 1

    * - a
      - b
      - Result
    * - 6
      - 9
      - 
    * - 9
      - 6 (6 % 9)
      -
    * - 6
      - 3 (9 % 6)
      -
    * - 3
      - 0 (6 % 3)
      - 3 (b = 0)

And since we have

.. code-block:: python

    GCD(a, b, c) = GCD(a, GCD(b, c)) = GCD(GCD(a, b), c) = GCD(GCD(a, c), b)

We can apply gcd and lcm functions to a list of numbers by using `reduce`_

.. code-block:: python

    def _sum(a, b):
        return a + b

    Y = [6, 9, 11]
    reduce(_sum, Y)
    #Is equivalent to
    _sum(_sum(6, 9), 11)

Now putting all together, we have

.. code-block:: python

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b / gcd(a, b)

    x = [11,13,14,16,17,18,19,20]
    print reduce(lcm, x)
    #232792560
    print reduce(xrange(1, 21)
    #232792560

Either way, the answer is **232792560**.

*<< EOF*

.. _`Project Euler`: http://projecteuler.net/problem=5
.. _`Least Common Multiple (LCM)`: http://en.wikipedia.org/wiki/Least_common_multiple
.. _`Greatest Common Divisor (GCD)`: http://en.wikipedia.org/wiki/Greatest_common_divisor
.. _`Euclidean Algorithm`: http://en.wikipedia.org/wiki/Euclidean_algorithm
.. _`reduce`: http://docs.python.org/release/1.4/tut/node83.html
