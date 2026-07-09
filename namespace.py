Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=1
a='One'
b=8
def func():
    a = 7
    print(a)
    print(b)

    
func()
7
8
a
'One'
a=0
def func():
    print(a)
    a = 1
    print(a)

    
func()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    func()
  File "<pyshell#15>", line 2, in func
    print(a)
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
def func(a=0):
    a+=1
    print(a)

    
func()
1
def red():
    a=1
    def blue():
        b=2
        print(a)
        print(b)
    blue()
    print(a)

    
red()
1
2
1
a=1
def func1():
    b=2
    def func2():
...         c=3
... 
...         
>>> a=1
>>> def func1():
...     b=2
...     def func3():
...         a=2
...         b=3
...         c=3
...         print(f"a={a}, b={b}, c={c}")
...     func3
...     print(f"b={b}")
... 
...     
>>> func1()
b=2
>>> func1()
b=2
>>> a
1
>>> def func1():
...     b=2
...     def func3():
...         global a
...         a=2
...         nonlocal b
...         b=3
...         c=3
...         print(f"a={a}, b={b}, c={c}")
...     func3()
...     print(f"b={b}")
... 
...     
>>> func1()
a=2, b=3, c=3
b=3
>>> a
2
