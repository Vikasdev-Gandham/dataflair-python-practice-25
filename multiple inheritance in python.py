Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To observe mulitple inheritance in python
class breakfast:
    pass

class lunch:
    pass

class brunch(breakfast, lunch):
    pass

class red: pass

classs yellow: pass
SyntaxError: invalid syntax
class yellow:pass

class blue: pass

class orange(red, yellow): pass

class green(yellow, blue): pass

class slate_grey(green, orange, blue): pass

slate_grey.mro()
[<class '__main__.slate_grey'>, <class '__main__.green'>, <class '__main__.orange'>, <class '__main__.red'>, <class '__main__.yellow'>, <class '__main__.blue'>, <class 'object'>]
class physics: id=1

>>> class chemistry: id=2
... 
>>> class maths: id=3
... 
>>> class student(physics, chemistry, maths): pass
... 
>>> print(student.id)
1
