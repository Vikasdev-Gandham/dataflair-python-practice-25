Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=3
while(num>0):
    print(num)
    num-=1

    
3
2
1
while(true):print("Hi")

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    while(true):print("Hi")
NameError: name 'true' is not defined. Did you mean: 'True'?
while(True):
    print("Hi")

    
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print("Hi")
KeyboardInterrupt
for item in [1,2,3]: print(item)

1
2
3
num=2
while(num>0):
    print(num)
    num-=1
else:print("Done")

2
1
Done
for letter in 'break'
SyntaxError: expected ':'
for letter in 'break':
    print(letter)
    if letter=='a': break;

    
b
r
e
a
# Star Diamond- write a function that prints out a diamond of stars, length 7.

def star_diamond():
    for row in range (4):
        for space in range (3-row):
            print(' ',end='')
        for start in range(row+1):
            print('*',end='')
        for star in range(row):
            print('*',end='')
        print()
    for row in range(3):
        for space in range(row+1):
            print(' ',end='')
        for star in range(3-row):
            print('*',end='')
        for star in range(2-row):
            print('*',end='')
        print()

        

star_diamond()
   *
  ***
 *****
*******
 *****
  ***
   *
#Matrix Multiplication- Write a functin that takes in two mulitplication matries, multiplies them, and returns the resulting matrix. if the matrices cannot be multiplied, declare so.
   
def mm(m1,m2):
    if len(m1[0]!=len(m2):
           
SyntaxError: invalid syntax
def mm(m1,m2):
    if len(m1[0])!=len(m2):
        print("Matrices not compatible for multiplicatoin")
        return
    result=[[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for row in range (len(m1)):
        for col in range(len(m2)):
            for temp in range(len(m2)):
                result[row][col]+=m1[row][temp]*m2[temp][col]
    return result


#Number Pyramid- Write a function that prints out the following pyramid of numbers making use of loops
def num_pyramid(n):
    num=1
    for rows in range(n):
        for row in range(rows+1):
            print(num, end=' ')
        print()

num_pyramid(5)
1 
1 1 
1 1 1 
1 1 1 1 
1 1 1 1 1 
def num_pyramid(n):
    num=1
    for rows in range(n):
        for row in range(rows+1):
            print(num, end=' ')
            num+=1
        print()

        
num_pyramid(5)
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
num_pyramid(10)
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 32 33 34 35 36 
37 38 39 40 41 42 43 44 45 
46 47 48 49 50 51 52 53 54 55 
#Number Diagonal- Write a function that prints out the following square with numbers in the diagonal.
def num_diagonal():
...     for row in range(1,6):
...         for col in range(1,6):
...             if row==col: print(row,end='')
...             else: print(0,end='')
...         print()
... 
>>> num_diagona()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    num_diagona()
NameError: name 'num_diagona' is not defined. Did you mean: 'num_diagonal'?
>>> num_diagonal()
10000
02000
00300
00040
00005
>>> #High Low- Write a function that takes an integer n and prints out a receding pyramid where each row first rises up to n, and then decreases.
>>> def high_low(n):
...     for row in range(1,n+1):
...         for col in range(row,n+1):
...             print(col,end=' ')
...         for col in range(n-1, row-1,-1):
...             print(col,end=' ')
...         print()
... 
...     
>>> high_low(5)
1 2 3 4 5 4 3 2 1 
2 3 4 5 4 3 2 
3 4 5 4 3 
4 5 4 
5 
>>> high_low(4)
1 2 3 4 3 2 1 
2 3 4 3 2 
3 4 3 
4 
