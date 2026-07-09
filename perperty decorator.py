Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand property in python
class Movie:
    def __init__(self,title):
            self.title=title
        def show_title(self):
            
SyntaxError: unindent does not match any outer indentation level
class Movie:
...     def __init__(self,title):
...             self.title=title
...     def show_title(self):
...         print("I'm watching {0}".format(self.title))
... 
...         
>>> seven_pounds=Movie('Seven Pounds')
>>> seven_pounds.show_title()
I'm watching Seven Pounds
>>> seven_pounds.title
'Seven Pounds'
>>> seven_pounds.title='SEVEN POUNDS'
>>> seven_pounds.title
'SEVEN POUNDS'
>>> class Movie:
...     def __init__(self,title):
...         self.__title=title
...     def show_title(self):
...             print("I'm watching {0}".format(self._title))
...     def get_title(self):
...         return self._title
...     def set_title(self,title):
...         self._title=title.upper()
...     title=property(get_title,set_title)
... 
...     
>>> class Movie:
...     def __init__(self,title):
...         self. _title=title
...     def show_title(self):
...         print("I'm watching {0}".format(self._title))
...     @property
...     def title(self):
...         return self._title
...     @title.setter
...     def title(self,title):
...         self._title=title.upper()
... 
...         
