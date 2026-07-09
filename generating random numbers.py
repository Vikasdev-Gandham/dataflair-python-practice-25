Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import seed, random
seed(8)
random(),random(),random(),random()
(0.2267058593810488, 0.9622950358343828, 0.12633089865085956, 0.7048169228716079)
random()*10+3
3.851852680507527
from random import randint
randint(0,9)
3
list=[3,4,5,6,7]
from random import choice
choice(list)
7
#Dice simulator- Write a function that pretends to rolll a dice and return a number from 1 to 6 every time you call it.
from random import random
def roll_dice():
    return int(random()*6)+1
#or

#import numpy.random
#def roll_dice():
# return int(numpy.random.random()*6)+1
roll_dice()
2
roll_dice()
4
roll_dice()
3
roll_dice()
3
#Five Even randoms- Write a function that takes a start and an end value and generates 5 random numbers in this range. out of these, it picks the even numbers and puts them in a list, and return that. Ultimately, we have anywhere from 0 to 5 random numbers.
import random
def five_even_randoms(start,end):
    return [num from num in random.sample(range(start,end+1),5) if num%2==0]
SyntaxError: invalid syntax
def five_even_randoms(start,end):
    return [num fro num in random.sample(range(start,end+1),5) if num%2==0]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def five_even_randoms(start,end):
...     return [num for num in random.sample(rangle(start,end+1),5) if num%2==0]
... 
>>> five_even_randoms(20,100)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    five_even_randoms(20,100)
  File "<pyshell#37>", line 2, in five_even_randoms
    return [num for num in random.sample(rangle(start,end+1),5) if num%2==0]
NameError: name 'rangle' is not defined. Did you mean: 'range'?
>>> five_even_randoms(20,100)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    five_even_randoms(20,100)
  File "<pyshell#37>", line 2, in five_even_randoms
    return [num for num in random.sample(rangle(start,end+1),5) if num%2==0]
NameError: name 'rangle' is not defined. Did you mean: 'range'?
>>> def five_even_randoms(start,end):
...     return [num for num in random.sample(range(start,end+1),5) if num%2==0]
... 
>>> five_even_randoms(20,100)
[44]
>>> five_even_randoms(20,100)
[82, 22, 54, 86]
>>> five_even_randoms(20,100)
[72, 80, 68, 34]
