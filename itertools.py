Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import itertools
for num in itertools.count(2,2):
    if num>12: break
    print(num)

    
2
4
6
8
10
12
count =0
for item in itertools.cycle(['blue','green']):
    if count>7:break
    count+=1

    

for item in itertools.cycle(['blue','green']):
    if count>7:break
    print(item)
    count+=1

    

count=0
for item in itertools.cycle(['blue','green']):
    if count>7: break
    print(item)
    count+=1

    
blue
green
blue
green
blue
green
blue
green
count=0
for itemin itertools.repeat(7):
    
SyntaxError: invalid syntax
for item in itertools.repeat(7):
    if count>5: break
    print(item)
    count+=1

    
7
7
7
7
7
7
for item in itertools.repeat(7,6):
    print(item)

    
7
7
7
7
7
7
#Quarters- Write a function that display amounts from one quarter to two dollars.
from itertools import count
def quarters():
    evens=count(start=0.25, step=0.25)
    return list(next(evens) for _ range(8))
SyntaxError: 'in' expected after for-loop variables
return list(next(evens) for _ range(8))
SyntaxError: 'in' expected after for-loop variables
return list(next(evens) for _ in range(8))
SyntaxError: 'return' outside function
from itertools import count
def quarters():
...     evens=count(start=0.25,step=0.25)
...     return list(next(evens) for _ in range(8))
... 
>>> quarters()
[0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
>>> #Prems- write a function that takes a word and a size, and returns permutations of given size from the characters of the word.
>>> from itertools import permutations
>>> def perms(word,size):
...     print('\n'.join(sorted(''.join(p) for p in permutations(word,size))))
... 
...     
>>> perms('HAIR',2)
AH
AI
AR
HA
HI
HR
IA
IH
IR
RA
RH
RI
>>> perms('123',2)
12
13
21
23
31
32
>>> perms('AIR',3)
AIR
ARI
IAR
IRA
RAI
RIA
