Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for item in zip([1,2,3],['red','green','blue']):
    print(item)

    
(1, 'red')
(2, 'green')
(3, 'blue')
set(zip([1,2],[3,4,5]))
{(2, 4), (1, 3)}
pairs=zip([1,2,3],['a','b','c'],['#','*','$'])
nums,letters,chars=zip(*pairs)
nums, letters, chars
((1, 2, 3), ('a', 'b', 'c'), ('#', '*', '$'))
#Groceries- Writee a function that takes in a list of tuples of items and their prices. Make it return a list of items and another of their prices.
def shopping_list(groceries):
    items,prices=zip(*groceries)
    return list(items),list(prices)

shopping_list([('milk',29),('eggs',19),('bananas',19)])
(['milk', 'eggs', 'bananas'], [29, 19, 19])
 #conflicts- A function takes in a list. adjacent numbers don't like to stand together; write a function that creates tuples from alternate numbers iin the list..
def conflicts(list1):
...     return list(zip(list1[:],list1[2:]))
... 
>>> conflicts([1,2,3,4,5,6,7,8,9])
[(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9)]
>>> #miles Apart- Write a function that takees in two integers of qual lengths. return the sum of the distance between its individual digits.
>>> def distance(a,b):
...     assert(len(str(a))==len(str(b)))
...     return sum([abs(int(digit1)-int(digit2)) for digit1,digit2 in zip(list(str(a)),list(str(b)))])
... 
>>> distance(252,371)
4
>>> distance(2,999)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    distance(2,999)
  File "<pyshell#22>", line 2, in distance
    assert(len(str(a))==len(str(b)))
AssertionError
>>> distance(200,999)
25
>>> #Group projects- Write a function that takes in two strings holding names of students in two groups. For a group project, pair the students according to their roll numbers. There may only be two students in one group.
>>> def make_pairs(group1,group2):
...     group1,group2=group1,split(','),group2,split(',')
...     for pair in zip(group1,group2):
...         print("%s is with %s" %(pair[0],pair[1]))
... 
...         
>>> make_pairs('Ayushi,Ruchi,Mikayla,Aaron','Helen,Rebecca,Cassidy,Caleb')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    make_pairs('Ayushi,Ruchi,Mikayla,Aaron','Helen,Rebecca,Cassidy,Caleb')
  File "<pyshell#31>", line 2, in make_pairs
    group1,group2=group1,split(','),group2,split(',')
NameError: name 'split' is not defined
>>> def make_pairs(group1,group2):
...     group1,group2=group1.split(','),group2.split(',')
...     for pair in zip(group1,group2):
...         print("%s is with %s" %(pair[0],pair[1]))
... 
...         
>>> make_pairs('Ayushi,Ruchi,Mikayla,Aaron','Helen,Rebecca,Cassidy,Caleb')
Ayushi is with Helen
Ruchi is with Rebecca
Mikayla is with Cassidy
Aaron is with Caleb
