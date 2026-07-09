Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=7
eval('num**3')
343
expr=input('Enter an expression in terms of x')
Enter an expression in terms of x3*x**4+4*x**2+2*x+6
x=int(input('Enter the value of x')
Enter the value of x7
      
SyntaxError: '(' was never closed
x=int(input('Enter the value of x'))
      
Enter the value of x7
eval(expr)
      
7419
def double(n): return n*2
def triple(n): return n*3
SyntaxError: invalid syntax
def triple(n): return n*3

choice=input('What shalll we do?')
What shalll we do?tiple
num=input('what number?')
what number?8
choice+='('+num+')'
eval(choice)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    eval(choice)
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'tiple' is not defined. Did you mean: 'triple'?
choice=input('What shall we do?')
What shall we do?triple
num=input('what number?')
what number?8
choice+='('+num+')'
eval(choice)
24
#Best Complements- Write a function that takes a binary string, adds 1 to it, then returns its 1's complement.
def complement(binary):
    return ~eval(str(eval('0b'+binary if binary[:2]!='0b' else binary)+1))

complement('0b111')
-9
complement('111')
-9
complement('0')
-2
>>> #Pocket Interpreter- Write a function that acts as an interpreter that quits on feeding 'bye' to it.
>>> def interpreter():
...     print('>>> ',end='')
...     expression=input()
...     if expression=='bye': return
...     print(eval(expression))
...     interpreter()
... 
...     
>>> interpreter()
>>> 2+3
5
>>> 5%3
2
>>> nye
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    interpreter()
  File "<pyshell#36>", line 6, in interpreter
    interpreter()
  File "<pyshell#36>", line 6, in interpreter
    interpreter()
  File "<pyshell#36>", line 5, in interpreter
    print(eval(expression))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'nye' is not defined
>>> nye
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    nye
NameError: name 'nye' is not defined
>>> bye
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    bye
NameError: name 'bye' is not defined
