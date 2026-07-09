Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
range(8)
range(0, 8)
list(range(8))
[0, 1, 2, 3, 4, 5, 6, 7]
list(range(-7,3))
[-7, -6, -5, -4, -3, -2, -1, 0, 1, 2]
list(range(-7,3,2))
[-7, -5, -3, -1, 1]
>>> for item in range(6):
...     print(item*2)
... 
...     
0
2
4
6
8
10
>>> #Mulitples- Write a function that takes a number and another to decide how many mulitple of the first number to print. it should do this with hout using a loop.
>>> def multiples(m,n):
...     muls=range(m,m*n+1,n)
...     print(*muls)
... 
...     
>>> multiples(7,7)
7 14 21 28 35 42 49
>>> #Weird alliteration, as we call it, is when in a string, where one word ends with a certain letter, the next word begings with that letter. list 'when nails shine'. Write a function that takes a string and determines whether it observes weird alliteration.
>>> def weird_alliteration(string):
...     words=string.split(' ')
...     for index in range(len(words)-):
...         
SyntaxError: invalid syntax
>>> 
>>> def weird_alliteration(string):
...     words=string.split(' ')
...     for index in range(len(words)-1):
...         if words[index][len(words[index])-1]!=words[index+1][0]: return False
...         return True
... 
...     
>>> weird_alliteration('When nails shine')
True
>>> weird_alliteration('Are you serious?')
False
