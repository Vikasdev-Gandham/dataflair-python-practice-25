Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To learn to raise and handle exceptions in python
def divide(a,b):
    return a/b

divide(1,0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    divide(1,0)
  File "<pyshell#3>", line 2, in divide
    return a/b
ZeroDivisionError: division by zero
try:
    for num in range(3):
        print(3/num)
        print("This doesn't print because an exception occurred before it")
except:
    print("You divided by 0")
    print('This prints because the exception was handled')

    
You divided by 0
This prints because the exception was handled
a,b=1,0
try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError:
    print("You added values of imcompatible types")
excep ZeroDivisionError:
    
SyntaxError: invalid syntax
try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError:
    print("You added values of imcompatible types")
except ZeroDivisionError:
    print("you divided by 0")

    
you divided by 0
try:
    print('10'+10)
    print(1/0)
except (TypeError,ZeroDivisionError):
    print("Invalid input")

    
Invalid input
try:
    print('1'+1)
    print(sum)
    print(1/0)
except NameError:
    print("sum does not exist")
except ZeroDivisionZerror:
    print("Cannot divide by 0")
except:
    print("Something went wrong")

    
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    print('1'+1)
TypeError: can only concatenate str (not "int") to str

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#46>", line 7, in <module>
    except ZeroDivisionZerror:
NameError: name 'ZeroDivisionZerror' is not defined. Did you mean: 'ZeroDivisionError'?
try:
    print('1'+1)
    print(sum)
    print(1/0)
except NameError:
    print("sum does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something went wrong")

    
Something went wrong
try:
    print(1/0)
except ValueError:
    print("This is a value error")
finally:
    print("This will print no matter what.")

    
This will print no matter what.
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    print(1/0)
ZeroDivisionError: division by zero
try:
    print(1/0)
except ZeroDivisionError:
    print(2/0)
finally:
    print("Sorry, not happening")

    
Sorry, not happening
Traceback (most recent call last):
  File "<pyshell#62>", line 2, in <module>
    print(1/0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#62>", line 4, in <module>
    print(2/0)
ZeroDivisionError: division by zero
a,b=int(input()),int(input())

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a,b=int(input()),int(input())
ValueError: invalid literal for int() with base 10: ''
>>> a,b=int(input()),int(input())

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a,b=int(input()),int(input())
ValueError: invalid literal for int() with base 10: ''
>>> #error
>>> if b==0: raise ZeroDivisionError
... 
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    if b==0: raise ZeroDivisionError
ZeroDivisionError
>>> try:
...     print('1'+1)
... except:
...     raise
... 
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    print('1'+1)
TypeError: can only concatenate str (not "int") to str
>>> raise ValueError("Inappropriate value")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    raise ValueError("Inappropriate value")
ValueError: Inappropriate value
>>> class MyError(Exception):
...     print("This is a problem")
... 
...     
This is a problem
>>> raise MyError("We experienced a MyError")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    raise MyError("We experienced a MyError")
MyError: We experienced a MyError
