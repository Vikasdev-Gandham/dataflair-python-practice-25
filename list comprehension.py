Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
[letter for letter in 'anxiety']
['a', 'n', 'x', 'i', 'e', 't', 'y']
[num for num in range(8) if num%3==0]
[0, 3, 6]
[num for num in range(8) if num%2==0 if num%3==3]
[]
[num for num in range(8) if num%2==0 if num%3==0]
[0, 6]
["Even" if num%2==0 else "odd" for num in range(8)]
['Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd']
#Threes- Usa list comprehesion to build a function that returns multiples of 3 that are smaller than the number n.
def threes(n):
    return[item for item in range(n) if item%3==0]

threes(15)
[0, 3, 6, 9, 12]
threes(47)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]
#game of Tuples- write a function that asks the user to input a sting of intergeers separated with spaces. It then returns a tuple from these values.
def game_of_tuples():
    s=input("Enter s string of numbers separated with spaces")
    return tuple([int(item) for item in s.split(' ')])

game_of_tuples()
Enter s string of numbers separated with spaces7 2 7 9 4 3 1 6
(7, 2, 7, 9, 4, 3, 1, 6)
game_of_tuples()
Enter s string of numbers separated with spaces7
(7,)
#Empty Promises- Write a function that takes in a list of integers and shifts all zeros to the end of the list.
>>> def empty_promises(arr):
...     zeros=arr.count(0)
...     arr-[val for val in arr if val!=0]
...     for i in range(zeros): arr.append(0)
...     return arr
... 
>>> empty_promises([2,0,2,4,0,0,4,9])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    empty_promises([2,0,2,4,0,0,4,9])
  File "<pyshell#24>", line 3, in empty_promises
    arr-[val for val in arr if val!=0]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> def empty_promises(arr):
...     zeros=arr.count(0)
...     arr=[val for val in arr if val!=0]
...     for i in range(zeros): arr.append(0)
...     return arr
... 
>>> empty_promises([2,0,2,4,0,0,4,9])
[2, 2, 4, 4, 9, 0, 0, 0]
>>> #Concatenating Lists- Write a function that takes in a list of list and concatenates all the immediate sublists into one.
>>> def concat(*lists):
...     return [i for 1 in lists for i in 1]
SyntaxError: cannot assign to literal
>>> def concat(*lists):
...     return [i for l in lists for i in l]
... 
>>> concat([1,2,3],[4,5,6,7],[8])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> #Stronger lists- write a function that multiplies each value in a list with the length of the list and returns that.
>>> def stronger_list(arr):
...     return [val*len(arr) for val in arr]
... 
>>> stronger_list([1,9,4,7])
[4, 36, 16, 28]
