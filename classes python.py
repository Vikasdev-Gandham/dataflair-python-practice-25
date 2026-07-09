Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To explore object-oriented programming with python
class fruit:
    """
    This class creates instances of fruits
    """
    color=''
    def sayhi(self):
        print("Hi")

        
orange=fruit()
orange.shape='Round'
orange.color
''
class fruit:
    def size(self,x):
        print(f"I am size {x}")

        
orange=furit()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    orange=furit()
NameError: name 'furit' is not defined. Did you mean: 'fruit'?
orange=furit()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    orange=furit()
NameError: name 'furit' is not defined. Did you mean: 'fruit'?
class fruit:
    def size(self,x):
        print(f"I am size {x}")

        
orange=fruit()
orange.size(7)
I am size 7
class fruit:
    def __init__(self,color,sizes):
        self.color=color
        self.size=size

        
sdf
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sdf
NameError: name 'sdf' is not defined
class fruit:
    def __init__(self,color,size):
        self.color=color
        self.size=size
    def salutation(self):
        print(f"I am {self.color} and a size {self.size}")

        
orange=fruit('Orange',7)
orange.salutation()
I am Orange and a size 7
class fruit:
    size='Small'
    def __init__(self,color,shape):
        self.color=color
        self.shape=shape
    def salutation():
        print(f"I am happy")

        
del orange.shape
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    del orange.shape
AttributeError: 'fruit' object has no attribute 'shape'
del orange.size
del orange
del fruit
fruit
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    fruit
NameError: name 'fruit' is not defined. Did you mean: 'quit'?
#Candidate- Write a class that evaluates candidates' scores on an exam. A correct answer adds 4 to the score and an incorrect one takes away 1.
class Candidate:
    def __init__(self):
        self.score=0
    def correct(self):
        self.score+=4
    def incorrect(self):
        self.score-=1
    def evaluate(self):
        return f'You scored {self.score}'

    
Riley=Candidate()
Riley=correct()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    Riley=correct()
NameError: name 'correct' is not defined
Riley=correct()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    Riley=correct()
NameError: name 'correct' is not defined
Riley.correct()
Riley.correct()
>>> Riley.incorrect()
>>> Riley.correct()
>>> Riley.incorrect()
>>> Riley.evaluate()
'You scored 10'
>>> #Temperature- Write a class that handles temperature. The absolute zero is -273.15 'C, and the class can convert temperatures between the Celcius and Farenheit formats.
>>> class temp:
...     abs_zero=-273.15
...     def f-to-c(self,temperature):
...         
SyntaxError: expected '('
>>> class temp:
...     abs_zero=273.15
...     def f_to_c(self,temperature):
...         return str((temperature-32)/1.8)+' °c'
...     def c_to_f(self,temperature):
...         return str(temperature*1.8+32)+' °F'
... 
...     
>>> oregon=temp()
>>> oregon.c_to_f(19)
'66.2 °F'
