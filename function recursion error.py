Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def factorial(num):
    if num==1: return 1
    return num*factorial(num-1)

factorial(5)
120
def num_n(num):
    if num==1: return 1
    return num+sum_n(num-1)

sum_n(7)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sum_n(7)
NameError: name 'sum_n' is not defined. Did you mean: 'num_n'?
def sum_n(num):
    if num==1: return 1
    return num+sum_n(num-1)

sum_n(7)
28
#Fbonacci Series- Write a function that takes, from the user, the number to print, and prints the Fibonacci series upto that length. Make use of recursioin.
a,b=0,1
num=int(input("How many?"))
How many?
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    num=int(input("How many?"))
ValueError: invalid literal for int() with base 10: ''
a,b=0,1
>>> num=int(input("Howw many?"))
Howw many?
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num=int(input("Howw many?"))
ValueError: invalid literal for int() with base 10: ''
>>> print(0,1,end=' ')
0 1 
>>> def fibr(num):
...     if num==2: return
...     global a,b
...     a,b=a+b
...     print(b,end=' ')
...     fibr(num-1)
... 
...     
>>> fibr(num)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    fibr(num)
NameError: name 'num' is not defined. Did you mean: 'sum'?
>>> fibr(bum)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    fibr(bum)
NameError: name 'bum' is not defined. Did you mean: 'sum'?
>>> def fibr(num):
...     if num==2: return
...     global a,b
...     a,b=b,a+b
...     print(b,end=' ')
...     fibr(num-1)
... 
...     
>>> fibr(num)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    fibr(num)
NameError: name 'num' is not defined. Did you mean: 'sum'?
