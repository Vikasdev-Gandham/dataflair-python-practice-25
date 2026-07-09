Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from pprint import pprint
data=[(1,{'a':'A','b':'B','c':'C','d':'D'}),(2,{'e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L'}),(3,['m','n']),(4,['o','p','q','r','s','t','u','v','w']),(5,['x','y','z']),]
print(date)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(date)
NameError: name 'date' is not defined. Did you mean: 'data'?
print(data)
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}), (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}), (3, ['m', 'n']), (4, ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']), (5, ['x', 'y', 'z'])]
pprint(data)
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']),
 (5, ['x', 'y', 'z'])]
class Color:
    def __init__(self,name,hex_value):
        self.name=name
        self.hex_value=hex_value
    def __repr__(self):
        return(
                'I am '+self.name+' and you can find me at '+self.hex_value)

    
colors=[Color('salmon','#FA8072'),Color('olive','#808000'),Color('purple','#800080')]
print(colors)
[I am salmon and you can find me at #FA8072, I am olive and you can find me at #808000, I am purple and you can find me at #800080]
pprint(colors)
 
[I am salmon and you can find me at #FA8072,
 I am olive and you can find me at #808000,
 I am purple and you can find me at #800080]
pprint(data,depth=3)
 
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']),
 (5, ['x', 'y', 'z'])]
>>> mylist=[1,2,'c','d']
...  
>>> pprint(mylist)
...  
[1, 2, 'c', 'd']
>>> pprint(mylist,width=-1)
...  
[1,
 2,
 'c',
 'd']
