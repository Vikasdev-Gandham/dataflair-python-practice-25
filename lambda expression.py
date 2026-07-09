Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lambda :print("Goodbye.")
<function <lambda> at 0x00000197C14013A0>
>>>  (lambda :print("Goodbye."))()
...  
SyntaxError: unexpected indent
>>> (lambda :print("Goodbye."))()
Goodbye.
>>> lambda a,b:a+b
<function <lambda> at 0x00000197C1402FC0>
>>> list(filter(lambda x:x%2==0, [1, 2, 3, 4, 5, 6]))
[2, 4, 6]
>>> #Double Triple- Write a function that takes a list and double each value. It triples all other values.
>>> def double_triple(mylist):
...     return list(map(lambda x:x*2 if x%2==0 else x*3,mylist))
... 
>>> double_triple([4,5,4,2,8,5,9])
[8, 15, 8, 4, 16, 15, 27]
>>> #Add All- Write a function that takes an integer and return the sum of intergers starting from 1, up to this number.
>>> from functools import reduce
>>> def add_all(num):
...     return reduce(lambda a,b:a+b,range(num+1))
...     #Or return sum(range(1,num+1))
... 
>>> add_all(4)
10
>>> add_all(8)
36
>>> add_all(12)
78
