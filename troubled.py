Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Troubled Addition- write a function that adds two number without using the + operator or the build-in sum() function.
>>> def add(a,b):
...     return a-~b-1
... 
>>> add(3,7)
10
>>> add(3,-7)
-4
>>> #Bitwise swap- write a function that takes two inegers and swaps them before returning them.
>>> def bitwise_swap(a,b):
...     a^=b
...     b^=a
...     a^=b
...     return a,b
... 
>>> bitwise_swap(4,21)
(21, 4)
