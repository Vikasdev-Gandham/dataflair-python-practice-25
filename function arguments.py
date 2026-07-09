Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sum(a,b):
    return a+b

sum(2,3)
5
sum(2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sum(2)
TypeError: sum() missing 1 required positional argument: 'b'
>>> sum(3,b=4)
7
>>> def sum(a,b=3):
...     return a+b
... 
>>> sum(2)
5
>>> def add_all(*args):
...     return sum([arg for arg in args])
... 
>>> del sum
>>> 
>>> add_all(3,4,5)
12
>>> #Counting Arguments- Write a function of variable arity- one that takes any number of arguments. make it return the number of arguments it receiveds in a call.
>>> def count(*args):
...     return len(args)
... 
>>> count()
0
>>> count(4,5)
2
>>> count('a',2,7.7)
3
>>> #Joining Path- Write a function that takes parts of a path and joins them using forward slashes.
>>> def join_path(*paths):
...     return '/'.join([path.lstrip('/').rstrip('/') for path in paths])+'/'
... 
>>> join_path('Users/')
'Users/'
>>> join_path('/Users','Ayushi')
'Users/Ayushi/'
>>> join_path('Users/','Ayushi/Desktop')
'Users/Ayushi/Desktop/'
