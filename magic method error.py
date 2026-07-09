Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand magic methods in pyhton
class mario:
    def __init__(self,lives):
        self.lives=lives

        
m=mario(7)
print(m+2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(m+2)
TypeError: unsupported operand type(s) for +: 'mario' and 'int'
class mario:
    def __init__(self,lives):
        self.lives=lives
    def __add__(self,other):
        return self.lives+other

    
m=mario(7)
print(m+2)
9
class myclass:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        return self.age+other
    def __radd__(self,other):
        return self.age+other

    
a=myclass(1)
print(a+1)
2
print(2+a)
3
print(a+2)
3
class pow:
    def __init__(self,base):
        self.base=base
    def __ipow__(self,power):
        return self.base**power

    
n=pow(2)
n**=10
print(n)
1024
class complement:
    def __init__(self,num):
        self.num=num
    def __invert__(self):
        return ~self.num

    
two=complement(2)
print(~two)
-3
class lessthan:
    def __init__(self,num):
        self.num=num
    def __it__(self,num2):
        return self.num<num2

    
two=lessthan(2)
print(two<7)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(two<7)
TypeError: '<' not supported between instances of 'lessthan' and 'int'
two=lessthan(2)
print(two<7)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(two<7)
TypeError: '<' not supported between instances of 'lessthan' and 'int'
class lessthan:
    def __init__(self,num):
...         self.num=mum
...         def __it__(self,num2):
...             return self.num<num2
... 
...         
>>> two=lessthan(2)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    two=lessthan(2)
  File "<pyshell#59>", line 3, in __init__
    self.num=mum
NameError: name 'mum' is not defined. Did you mean: 'num'?
>>> class lessthan:
...     def __init__(self,num):
...         self.num=nem
...         def __it__(self,num2):
...             return self.num<num2
... 
...         
>>> two=lessthan(2)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    two=lessthan(2)
  File "<pyshell#62>", line 3, in __init__
    self.num=nem
NameError: name 'nem' is not defined. Did you mean: 'num'?
>>> class lessthan:
...     def __init__(self,num):
...         self.num=num
...         def __it__(self,num2):
...             return self.num<num2
... 
...         
>>> two=lessthan(2)
>>> print(two<7)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(two<7)
TypeError: '<' not supported between instances of 'lessthan' and 'int'
