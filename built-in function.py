Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(-7)
7
any((0,0))
False
chr(65)
'A'
int('7')
7
max(2,4,3.3)
4
#Ones and Zeroes- Write a function that takes in a binary number and determines whether it can arrange it in an alternating pattern of 0's and 1's.
def ones_and_zeroes(binary):
    return abs(str(binary).count('0')-str(binary).count('1'))<2

ones_and_zeroes('0110110')
True
ones_and_zeroes('01101101')
False
ones_and_zeroes('01100')
True
>>> ones_and_zeroes('011000')
False
>>> #Easy Lists- Can you write a function to create a list from a string without using the list() build-in function?
>>> def string_to_list(string):
...     mylist=[]
...     mylist[:]=string
...     return muylist
... 
>>> string_to_list('orange')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    string_to_list('orange')
  File "<pyshell#18>", line 4, in string_to_list
    return muylist
NameError: name 'muylist' is not defined. Did you mean: 'mylist'?
>>> def string_to_list(string):
...     mylist=[]
...     mylist[:]=string
...     return mylist
... 
>>> string_to_list('orange')
['o', 'r', 'a', 'n', 'g', 'e']
>>> #Exisodes- Write a function that takes a list of episode numbers, removes duplicates, and sorts them in an ascending order before returning the same.
>>> def show(episodes):
...     return sorted(list(set(episodes)))
... 
>>> show([131,137,131,134,130,125,134,131])
[125, 130, 131, 134, 137]
>>> #A numbers's Rank- Write a function that counts the number of digits in an integer.
>>> def number_rank(num):
...     return len(str(num))
... 
>>> number_rank(731)
3
>>> number_rank(7313)
4
>>> number_rank(7)
1
