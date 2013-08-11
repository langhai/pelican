10001st Prime Number
#####################################

:date: 22-07-2013
:tags: project euler, python, algorithm, math
:category: Code!
:slug: 10001st-prime-number
:author: Hai Lang
:status: published

.. highlights::
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?

This is the seventh question from `Project Euler`_. Getting the 10001st prime number. 

Well, the most staright forward method to solve this is to iterate through all nummbers greater than 
2 and check their primality one by one until we reach the 10001st prime.

To check a number's primality, we can simply try to divide the number by every number less than it.
With the computational power that everyone has nowadays, even a simple solution as such can effectively
give an answer within seconds or even fractions of seconds. But what if we need the 10000001st prime number?

As the counter grows, it is awkward to stick with a brute-force algorithm. We need to optimize it, and make
it variable for reasonable large numbers.

A simple optimization is that, if a number can be divided by an even number, it is not a prime number, and it
can be divided by 2. For instance,

.. code-block:: python

    12 / 4 = 3
    
    and
    
    12 / 2 = 6 Since 12 = 2 * 2 * 3

As shown above, when testing a number's primality, we don't need to divide the number by even numbers that
are less than it, we only need to test odd numbers. For instance,

.. code-block:: python

    13 % 2 != 0
    13 % 3 != 0
    13 % 5 != 0
    13 % 7 != 0
    13 % 9 != 0
    13 % 11 != 0
    
    Thus, 13 is a prime number

Any number that can be divided by an even number can also be divided by 2, it'll fail the first checking so
we don't have to worry about even numbers at all.

Since we cut off all the even number checkings except for 2, it is nearly half of the original cost.

Yet we can further improve this simple primality checking algorithm.

.. code-block:: python

    Since for any number, we have
    x = a * b
    
    If a > sqrt(x) and b > sqrt(x)
    then a * b > x
    
    Thus, only one of a, b can be greater than sqrt(x)

This means when checking a numbers primality, not all the odd numbers less than it need to be checked, only
for those that are also less than the square root of the number. For insance,

.. code-block:: python

    sqrt(13) = 3.60
    13 % 2 != 0
    13 % 3 ! = 0

    Thus, 13 is a prime number

Looks like we just effectively reduced the cost by half again. To implement this idea to get the 10001st
prime number,

.. code-block:: python

    import math
    def isPrime(num):
        if num == 2:
            return True
        if num % 2 == 0 or num < 2:
            return False
        #Start from 3, until its square root, with stepping 2
        for x in xrange(3, int(math.sqrt(num)) + 1, 2):
            if num % x == 0:
                return False
        return True
    
    if __name__ == '__main__':
        num = counter = 1
        while (counter < 10001):
            num += 2 #Only test odd numbers
            if isPrime(num):
                counter += 1
        print "The 10001st prime number is: " + str(num)

Note that,

.. code-block:: python

    for x in xrange(3, int(math.sqrt(num)) + 1, 2):

    Is equivalent to 

    for (int x = 3; x <= sqrt(num); x += 2)

    In some other programming languages.

The answer is **104743**

*<< EOF*

.. _`Project Euler`: http://projecteuler.net/problem=7
.. _`Python Docs`: http://docs.python.org/2/tutorial/controlflow.html#defining-functions

