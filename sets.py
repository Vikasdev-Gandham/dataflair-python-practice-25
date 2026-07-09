Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={3,1,1,2}
a
{1, 2, 3}
a={[1,2,3],4}
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a={[1,2,3],4}
TypeError: unhashable type: 'list'
a[1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[1]
TypeError: 'set' object is not subscriptable
>>> a.discard(1)
>>> a
{2, 3}
>>> a.add(1)
>>> a
{1, 2, 3}
>>> set1,set2,set3={1,2,3),{3,4,5},{5,6,7}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> set1,set2,set3={1,2,3},{3,4,5},{5,6,7}
>>> set1.union(set2,set3)
{1, 2, 3, 4, 5, 6, 7}
>>> #The commns- Write a function that takes two lists and from that, gets the values common in the two lists.  Do  this without making an interse
>>> #The commns- Write a function that takes two lists and from that, gets the values common in the two lists.  Do  this without making an intersein
>>> 
>>> #The commns- Write a function that takes two lists and from that, gets the values common in the two lists.  Do  this without making an intersection on the two sets.
>>> def the_commons(list1,list2):
...     return set([num for num in list2 if num  in list1])
... 
>>> the_commons([2,9,7],[3,4,1])
set()
>>> the_commons([1,4,3,2,5],[2,4,2,7,9])
{2, 4}
>>> the_commons([1,4,3,2,5,8,6],[2,8,4,2,7,9])
{8, 2, 4}
>>> #Subscribers- Write a function that takes in the ID's of the people who subscribed to netflix, and of those who subscribed to hotstar.  make it return the number of people that have at least one subscription.
>>> def subscribers(netflix.hotstar):
...     
SyntaxError: invalid syntax
>>> def subscribers(netflix.hotstar):
...     
SyntaxError: invalid syntax
>>> def subscribers(netflix,hotstar):
...     return len(set(netflix).union(set(hotstar)))
... 
>>> subscribers([22,759,232,476,449,34,55,593],[759,33,311,34,29,23,4442])
13
