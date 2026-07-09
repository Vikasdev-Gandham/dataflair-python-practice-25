Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objecting- To implement generators in python
def countdown()
SyntaxError: expected ':'
def countdown():
    second=10
    while(second>=1):
        yield second
        second-=1

        
for second in countdown():
    print(second)

    
10
9
8
7
6
5
4
3
2
1
def power(num):
    while num>=1:
        if num%2==0: yield num**2
        elif num%3==0: yield num**3
        else: yield num
        num-=1

        
>>> for number in power(12):
...     print(number)
... 
...     
144
11
100
729
64
7
36
5
16
27
4
1
>>> def even_squares(num):
...     for index in range(num):
...         if index**2%2==0:
...             yield index**2
... 
...             
>>> list(even_squares(10))
[0, 4, 16, 36, 64]
>>> mylist=[1,3,6,10]
>>> numbers = (num**2 for num in mylist)
>>> next(numbers)
1
>>> next(numbers)
9
>>> next(numbers)
36
>>> next(numbers)
100
>>> next(numbers)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    next(numbers)
StopIteration
