Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand defaultdict in python
from collections import defaultdict
def default(): return 42

mydict=defaultdict(default)
mydict['a']=1
mydict['b']=2
mydict['c']=3
mydict['d']
42
score=defaultdict(lambda :23)
score['Hannah']=98
score['Lucy']=76
score['Hannah']
98
score['Irena']
23
score.keys()
dict_keys(['Hannah', 'Lucy', 'Irena'])
mylist=[('a',1),('b',2),('c',3)]
newdict=defaultdict(list)
for key,values in mylist:
    newdict[key].append(value)

    
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    newdict[key].append(value)
NameError: name 'value' is not defined. Did you mean: 'values'?
for key,value in mylist:
    newdict[key].append(value)

    
newdict
defaultdict(<class 'list'>, {'a': [1], 'b': [2], 'c': [3]})
newdict['d']
[]
name='Puddle'
mydict=defaultdict(int)
for letter in name:
    mydict[letter]+=1

    
mydict
defaultdict(<class 'int'>, {'P': 1, 'u': 1, 'd': 2, 'l': 1, 'e': 1})
mydict['0']
0
#Switchboard- A switchboard has 6 switches. Write a function that return a string of six 0's and 1's- 0 for the switches that are OFF, and 1 for those that are ON. Only one switch can be On at a time.
def switchboard(switch):
    board=defaultdict(lambda :0)
    board[switch]=1
    return ''.join([str(board[num]) for num in range(1,7)])

switchboard(4)
'000100'
swithcboard(2)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    swithcboard(2)
NameError: name 'swithcboard' is not defined. Did you mean: 'switchboard'?
swithboard(2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    swithboard(2)
NameError: name 'swithboard' is not defined. Did you mean: 'switchboard'?
switchboard(2)
'010000'
Switchboard(6)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    Switchboard(6)
NameError: name 'Switchboard' is not defined. Did you mean: 'switchboard'?
>>> switchboard(6)
'000001'
>>> #Scratchcard- Ten people buy a scratchcard each. Randomly, one of them wins $1000. Everone else wins $1 each. write a function implementing this.
>>> from random import choice
>>> def scratchcard():
...     tickets=[*range(1,11)]
...     results=defaultdict(lambda :'$1')
...     results[choice(tickets)]='$1000'
...     for num in range(1,11): print(num,results[num])
... 
...     
>>> scratchcard()
1 $1
2 $1
3 $1
4 $1
5 $1
6 $1
7 $1
8 $1000
9 $1
10 $1
