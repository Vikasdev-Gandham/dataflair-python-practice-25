Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To explore the numeric modules- math, decimal, random, fractions
import math
math.ceil(3.4)
4
math.factorial(5)
120
sum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])
1.0
sum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])
1.0
#wrong
math.fsum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])
1.0
math.gcd(12,18)
6
math.exp(7)
1096.6331584284585
math.log2(2)
1.0
math.sqrt(9)
3.0
math.sin(90)
0.8939966636005579
math.pi
3.141592653589793
from decimal import
SyntaxError: Expected one or more names after 'import'
from decimal import
SyntaxError: Expected one or more names after 'import'
from decimal import *
gercontext().prec=4
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    gercontext().prec=4
NameError: name 'gercontext' is not defined. Did you mean: 'getcontext'?
getcontext().prec=4
decimal(1)/decimal(7)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    decimal(1)/decimal(7)
NameError: name 'decimal' is not defined. Did you mean: 'Decimal'? Or did you forget to import 'decimal'?
decimal(1)/decimal(7)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    decimal(1)/decimal(7)
NameError: name 'decimal' is not defined. Did you mean: 'Decimal'? Or did you forget to import 'decimal'?
decimal(1)/decimal(7)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    decimal(1)/decimal(7)
NameError: name 'decimal' is not defined. Did you mean: 'Decimal'? Or did you forget to import 'decimal'?
Decimal(1)/Decimal(7)
Decimal('0.1429')
Decimal(math.pi)
Decimal('3.141592653589793115997963468544185161590576171875')
Decimal(math.pi)+1
Decimal('4.142')
-7//4
-2
Decimal(-7)//Decimal(4)
Decimal('-1')
1/Decimal('Infinity')
Decimal('0E-1000002')
from random import *
int(random()*10)
6
int(random()*10)
0
int (random()*10)
9
randrange(1,11,2)
9
randrange(1,11,2)
5
choic(['April','Anne','Leslie'])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    choic(['April','Anne','Leslie'])
NameError: name 'choic' is not defined. Did you mean: 'choice'?
>>> choice(['April','Anne','Leslie'])
'Anne'
>>> sample([1,3,2,5,6,2,7],k=4)
[7, 2, 3, 1]
>>> from fractions import *
>>> Fraction(18,-14)
Fraction(-9, 7)
>>> Fraction('0.00007')
Fraction(7, 100000)
>>> #Lottery- Write a function that takes in a list of names of those who have purchased a lottery ticket. Unbiasedly, pick a lottery winner. The number of tickets purchased does not affect the probability of being picked.
>>> import random
>>> def lottery(names):
...     return random.choice(list(set(names)))
... 
>>> lottery(['Aaron','Ryan','Hugh','Jake','Aaron','Riley','Aaron'])
'Hugh'
