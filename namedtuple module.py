Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Objective- To analyze the namedtuple in python
>>> from collections import namedtuple
>>> colors = namedtuple('colors','red green blue')
>>> red = Colors(red=255, green=0, blue=0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    red = Colors(red=255, green=0, blue=0)
NameError: name 'Colors' is not defined. Did you mean: 'colors'?
>>> Colors = namedtuple('Colors', 'red green blue')
>>> red = Colors(red=255, green=0, blue=0)
>>> green = Colors(red=0, green=255, blue=0)
>>> blue = Colors(red=0, green=0, blue=255)
>>> red
Colors(red=255, green=0, blue=0)
>>> red._fields
('red', 'green', 'blue')
>>> pets = namedtuple('pets' ['name','age'])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pets = namedtuple('pets' ['name','age'])
TypeError: string indices must be integers, not 'tuple'
>>> pets = namedtuple('pets', ['name','age'])
>>> fluffy = pets('Fluffy', 9)
>>> Fluffy
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Fluffy
NameError: name 'Fluffy' is not defined. Did you mean: 'fluffy'?
>>> fluffy
pets(name='Fluffy', age=9)
>>> red.red
255
>>> red.green
0
>>> red[0]
255
>>> getattr(red, 'green')
0
>>> red._asdict()
{'red': 255, 'green': 0, 'blue': 0}
>>> Colors._make(['Purple','Violet','Gold'])
Colors(red='Purple', green='Violet', blue='Gold')
>>> Colors(**{'red':255,'green':0,'blue':0})
Colors(red=255, green=0, blue=0)
>>> red._replace(green=1)
Colors(red=255, green=1, blue=0)
