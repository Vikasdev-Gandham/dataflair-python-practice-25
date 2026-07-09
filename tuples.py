Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
(1,)
(1,)
(1,2,3)
(1, 2, 3)
1,
(1,)
1,2,3
(1, 2, 3)
 (1,2,3)[2]
 
SyntaxError: unexpected indent
(1,2,3)[2]
3
 a=(1,2,3)
 
SyntaxError: unexpected indent
a=(1,2,3)
def a[2]
SyntaxError: expected '('
a[2]=7
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[2]=7
TypeError: 'tuple' object does not support item assignment
sum(a)
6
#Apples and Oranges- write a function that takess in a list of fruits holding the number of apples and oranges- tuples of such numbers. apples have 2 points and oranges have 3. Make the function return the total number of points for each case.
def fruits(values):
    results=dict()
...     for point in values:
...         results[point]=2*point[0]+3*point[1]
...         return results
... 
...     
>>> fruits([(2,3),(4,3),(4,7)])
{(2, 3): 13}
>>> fruits([(2,3),(4,3),(4,7)])
{(2, 3): 13}
>>> def fruits(values):
...     results=dict()
...     for point in values:
...         results[point]=2*point[0]+3*point[1]
...         return results
... 
...     
>>> fruits([(2,3),(4,3),(4,7)])
{(2, 3): 13}
>>> # wrong
>>> #Tuple Pyramid-Write a function that create a tuple with s string. adding a counter to it each time until it reaches desired height.
>>> def pyramid(string.height):
...     
SyntaxError: invalid syntax
>>> def pyramid(string,height):
...     tup=(string)
...     for index in range(1,height+1):
...         tup=(tup,index)
...         print(tup)
... 
...         
>>> pyramid('egypt',7)
('egypt', 1)
(('egypt', 1), 2)
((('egypt', 1), 2), 3)
(((('egypt', 1), 2), 3), 4)
((((('egypt', 1), 2), 3), 4), 5)
(((((('egypt', 1), 2), 3), 4), 5), 6)
((((((('egypt', 1), 2), 3), 4), 5), 6), 7)
