Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=798.321
721
721
complex(2)
(2+0j)
0xFE
254
float(110)
110.0
#Not Gate- Build a function that simulatee a NOT gate. if the input is 0, it returns 1. And if it is 1, it returns 0. But do this without using logical, ternary, conditional, or bitwise operations.
def not_gate(digit):
    return 1-digit
    #or return [1,0][digit]
not_gate(0)
SyntaxError: invalid syntax
def not_gate(digit):
    return 1-digit
    #or return [1,0][digit]

not_gate(0)
1
not_gate(1)
0
# Expanded- Write a function that expands a number. For instance, 42301 become 40000+2000+300+1
def expanded(num):
    num=str(num)
    return '+'.join([num[index]+'0'*(len(num)-1-index) for index in range(en(num)) if num[index]!='0'])

expanded(429)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    expanded(429)
  File "<pyshell#22>", line 3, in expanded
    return '+'.join([num[index]+'0'*(len(num)-1-index) for index in range(en(num)) if num[index]!='0'])
NameError: name 'en' is not defined
>>> def expanded(num):
...     num=str(num)
...     return '+'.join([num[index]+'0'*(len(num)-1-index) for index in range(len(num)) if num[index]!='0'])
... 
>>> expanded(429)
'400+20+9'
>>> expanded(32401)
'30000+2000+400+1'
>>> 
>>> #Dog Age Calculator- A dog's age, for the first two years, is said to be equal to 10.5 human years for each year. Every consequent year amounts to 4 human years. write a function that takes the human_age from the user and calculates the age in dog years.
>>> def dog_age(human_age):
...     assert(human_age>=0)
...     return str((human_age)*10.5-((human_age-2)>0)*(human_age-2)*6.5)+' years'
... 
>>> dog_age(0)
'0.0 years'
>>> dog_age(1)
'10.5 years'
>>> dog_age(2)
'21.0 years'
>>> dog_age(3)
'25.0 years'
>>> dog_age(4)
'29.0 years'
>>> dog_age(9)
'49.0 years'
>>> #Binary to Decimal- Write a function that takes a number in is and 0s considering it binary, and returns its decimal equivalent.
de
>>> def to_decimal(binary):
...     decimal,mul=0,len(str(binary))-1
...     for digit in str(binary):
...         decimal+=int(digit)*2**mul
...         mul-=1
...     return decimal
... 
>>> to_decimal(111)
7
>>> to_decimal(101)
5
