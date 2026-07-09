Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5 and 7
7
5&7
5
0&1
0
0|1
1
1&1
1
0| True
1
4<<1
8
 #Toggle Digits- write a function that takes a number, toggles the digit at a specified postion in its binary form, and returns the number that results.
def toggle(num,pos):
    num^=(1<<pos)
...     return num
... 
>>> toggle(4,1)
6
>>> toggle(4,2)
0
>>> toggle(7,2)
3
>>> #Doubles-write a function that prints n number of items in a series- this series begins at 3 and doubles the number each time.
>>> def doubles(n):
...     num=3
...     for index in range(n):
...         num=eval(bin(num))<<1
...         print(num)
... 
...         
>>> doubles(3)
6
12
24
>>> doubles(6)
6
12
24
48
96
192
>>> doubles(10)
6
12
24
48
96
192
384
768
1536
3072
