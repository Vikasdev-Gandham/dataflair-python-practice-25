Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def outer(x):
    def inner():
        print(x)
 return inner
SyntaxError: unindent does not match any outer indentation level

def outer(x):
    def inner():
        print(x)
    return inner

func = outer(7)
func()
7
def outer(x):
    result=0
    def inner(n):
        nonlocal result
        whille n>0:
            
SyntaxError: invalid syntax
def outer(x):
    result=0
    def inner(n):
        nonlocal result
        while n>0:
            result+=x*n
            n-=1
            return result
...     return inner
... 
>>> func = outer(7)
>>> func(3)
21
>>> func = outer(7)
>>> func(3)
21
>>> func = outer(3)
>>> func(3)
9
>>> def outer(x):
...     result=0
...     def inner(n):
...         nonlocal result
...         while n>0:
...             result+=x*n
...             n-=1
...         return result
...     return inner
... 
>>> func = outer(7)
>>> func(3)
42
>>> func = outer(3)
>>> func(3)
18
>>> def outer(func):
...     def inner(msg):
...         func(msg)
...     return inner
... 
>>> def sayhi(msg):
...     print(msg)
... 
...     
>>> myfunc = outer(sayhi)
>>> myfunc("hello")
hello
