Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #volume of a shpere- write a function that takes in a shere's radius and calculates its volume rounded to two decimal places. you can import the value of pi from the math module for this.
>>> import math
>>> def sphere_volume(radius):
...     return round(4/3*math.pi*radius**3,2)
... 
>>> sphere_volume(6)
904.78
>>> sphere_volume(12.2)
7606.21
>>> #valid password- write a function that determine where a string make for a valid password. For this, it must be at lest 6_characters long and at most 12-characters long. it also must have at least one letter, one digit, and one character from s, #, and 0.
>>> #valid password- Write a function that determines whether a string for a valid password. For this, it must be at least 6-characters long and at most 12-characters long. It also must have at least one letter, one digit, and one character from $, #, and @.
>>> def valid_password(password):
...     p=list(password)
...     if len(password)<6 or len(password)>12: return False
...     if not(any(i.isdigit() for i in p)): return False
...     if not(any(i in '$#@' for i in p)): return False
...     if not(any(i.isalpha() for i in p)): return False
...     return True
... 
>>> valid_password('abc')
False
>>> valid_password('ab6c')
False
>>> valid_password('ab6c!@')
True
