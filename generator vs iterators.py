Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def even(num):
    while(num!=0):
        if num%2==0:
            yield num
        num-=1

        
for item in even(8):
    print(item)

    
8
6
4
2
 (num**2 for num in [1,3,6,10])
 
SyntaxError: unexpected indent
(num**2 for num in [1,3,6,10])
<generator object <genexpr> at 0x000001C2D7F97100>
iter_obj=iter([3,4,5])
next(iter_obj)
3
next(iter_obj)
4
next(iter_obj)
5
next(iter_obj)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    next(iter_obj)
StopIteration
f=even(7)
>>> type(f)
<class 'generator'>
>>> obj=iter({1,3,2})
>>> type(obj)
<class 'set_iterator'>
>>> def func():
...     item=1
...     while item>0:
...         yield item
...         item-=1
... 
...         
>>> for item in func():
...     print(item)
... 
...     
1
>>> func().__sizeof__()
168
>>> iter([1,2]).__sizeof__()
32
