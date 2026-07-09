Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+3
5
3>=3
True
a=7
a**=3
a
343
7>7 and 2>-1
False
'me' in 'disappintment'
True
'2' is "2"
True
2^3
1
#Next perfect square- A perfect square is an integer, the square root of which is also an interger.write a function  that in a non-negative integer and returns the next perfect square. if the integer, however, is not a perfect square itself, it makes it known.
import math
def next_perfect_square(num):
    return(int(math.sqrt(num))+1+**2 if math.squrt(num)%1==0 else ""Not a perfect square itselft"
           
SyntaxError: unterminated string literal (detected at line 2)
dev next_perfect_square(num):
           
SyntaxError: invalid syntax
def next_perfect_square(num:
    return (int(math.sqrt(num))+1)**2 if math.sqrt(num)%1==0 else "Not a perfect square itself"
SyntaxError: '(' was never closed
def next_perfect_square(num):
...     return (int(math.sqrt(num))+1)**2 if math.sqrt(num)%1==0 else "Not a perfect square itselft"
... 
>>> next_perfect_square(0)
1
>>> next_perfect_square(1)
4
>>> next_perfect_square(3)
'Not a perfect square itselft'
>>> next_perfect_square(4)
9
>>> #remove Vowels- Write a function that takes a string and removes any vowels in it.
>>> def remove_vowels(string):
...     s=''
...     for letter in string:
...         if letter not in ['a','e','i','o','u']: s+=letter;
...         return s
... 
...     
>>> remove_vowels('She was a pyramid')
'S'
>>> remove_vowels("hello, welcome home')
...               
SyntaxError: unterminated string literal (detected at line 1)
>>> remove_vowels('Hello, welcome home')
...               
'H'
>>> def remove_vowels(string):
...     s=''
...     for letter in string:
...         if letter not in ['a','e','i','o','u']: s+=letter;
...         return s
... 
...     
>>> remove_vowels('She was a pyramid')
'S'
>>> remove_vowels('Hello, welocme home')
'H'
