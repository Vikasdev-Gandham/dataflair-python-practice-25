Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand errors and exceptions in python
if 3>1 print"Hello'
SyntaxError: unterminated string literal (detected at line 1)
def divide(a,b):
    return a/b

divide(2,0)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    divide(2,0)
  File "<pyshell#4>", line 2, in divide
    return a/b
ZeroDivisionError: division by zero
assert 1==2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    assert 1==2
AssertionError
class fruit: pass

fruit.color
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fruit.color
AttributeError: type object 'fruit' has no attribute 'color'
[].sortt
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    [].sortt
AttributeError: 'list' object has no attribute 'sortt'. Did you mean: 'sort'?
from math import square
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    from math import square
ImportError: cannot import name 'square' from 'math' (unknown location)
[1,2,3][3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    [1,2,3][3]
IndexError: list index out of range
{1:'a','b':2}[4]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    {1:'a','b':2}[4]
KeyError: 4
while True: print("True")

True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    while True: print("True")
KeyboardInterrupt
import tensorflow
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    import tensorflow
ModuleNotFoundError: No module named 'tensorflow'
friends
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    friends
NameError: name 'friends' is not defined
def nums():
    for hum in [1,2]: yield num

    
n=nums()
next(n)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    next(n)
  File "<pyshell#20>", line 2, in nums
    for hum in [1,2]: yield num
NameError: name 'num' is not defined. Did you mean: 'hum'?
def show ()
SyntaxError: expected ':'
10+'10'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    10+'10'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def show():
...     cat+=1
... 
...     
>>> show()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    show()
  File "<pyshell#31>", line 2, in show
    cat+=1
UnboundLocalError: cannot access local variable 'cat' where it is not associated with a value
>>> int(3.5)
3
>>> int('3.5')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int('3.5')
ValueError: invalid literal for int() with base 10: '3.5'
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
