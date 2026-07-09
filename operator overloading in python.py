Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To overload operator in python
42 + 1
43
'42'+'1'
'421'
'hello'+' '+'world'
'hello world'
[1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
class number:
    def __init__(self,num):
        self.num=num

        
three,four = number(3), number(4)
print(three+four)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(three+four)
TypeError: unsupported operand type(s) for +: 'number' and 'number'
class number:
    def __init__(self,num,fraction):
        self.num=num
        self.fraction=fraction
    def __str__(self):
        return f"{self.num}.{self.fraction}"

    
seven_one=number(7,1)
print(str(seven_one))
7.1
class myufloat:
    def __init__(self,whole,fraction):
        self.whole=whole
        self.fraction=fraction
    def shownumber(self):
        print(f"{self.whole}.{self.fraction}")
    def __add__(self,other):
        if(self.fraction+other.fraction)>9:
            return myfloat(self.whole+other.whole+1,self.fraction+other.fraction-10)
        return myfloat(self.whole+other.whole,self.fraction+other.fraction)

    
num1,num2 = muyfloat(3,7), myfloat(3,4)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    num1,num2 = muyfloat(3,7), myfloat(3,4)
NameError: name 'muyfloat' is not defined. Did you mean: 'myufloat'?
num1,num2 = myfloatclass myufloat:

    
    def __init__(self,whole,fraction):
        self.whole=whole
        self.fraction=fraction
    def shownumber(self):
        print(f"{self.whole}.{self.fraction}")
    def __add__(self,other):
        if(self.fraction+other.fraction)>9:
...             return myfloat(self.whole+other.whole+1,self.fraction+other.fraction-10)
...         return myfloat(self.whole+other.whole,self.fraction+other.fraction)class myufloat:
...             def __init__(self,whole,fraction):
...                 self.whole=whole
...                 self.fraction=fraction
...             def shownumber(self):
...                 print(f"{self.whole}.{self.fraction}")
...             def __add__(self,other):
...                 if(self.fraction+other.fraction)>9:
...                     return myfloat(self.whole+other.whole+1,self.fraction+other.fraction-10)
...                 return myfloat(self.whole+other.whole,self.fraction+other.fraction)
...             
SyntaxError: invalid syntax
>>> class myfloat:
...     def __init__(self,whole,fraction):
...         self.whole=whole
...         self.fraction=fraction
...     def shownumber(self):
...         print(f"{self.whole}.{self.fraction}")
...     def __add__(self,other):
...         if(self.fraction+other.fraction)>9:
...             return myfloat(self.whole+other.whole+1,self.fraction+other.fraction-10)
...         return myfloat(self.whole+other.whole,self.fraction+other.fraction)
... 
...     
>>> num1,num2 = mylfoat(3,7), myfloat(3,4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    num1,num2 = mylfoat(3,7), myfloat(3,4)
NameError: name 'mylfoat' is not defined. Did you mean: 'myufloat'?
>>> num1,num2 = myfloat(3,7), myfloat(3,4)
>>> res=num1+num2
>>> res.shownumber()
7.1
