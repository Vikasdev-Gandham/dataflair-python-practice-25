Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand inheritance and its types
class Person:
            pass

        
class Student(Person):
    pass

issubclass(Student,person)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    issubclass(Student,person)
NameError: name 'person' is not defined. Did you mean: 'Person'?
issubclass(Student,person)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    issubclass(Student,person)
NameError: name 'person' is not defined. Did you mean: 'Person'?
class Person:
            pass

        
class Student(Person):
                pass

            
issubclass(Student,Person)
True
x=0
class fruit:
        def __init__(self):
                    global x
                    x+=1
                    print("I'm fruit")

                    
class citrus(fruit):
            def __init__(self):
                            super().__init__()
                            global x
                            x+=2
                            print("I'm citrus")

                            
lime=citrus()
I'm fruit
I'm citrus
print(x)
3
class Color:
            pass

        
class Fruit:
            pass

        
class Orange(Color,Fruit):
            pass

        
class accessories:
            size=7

            
class footwear(footwear):
            pass

        
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    class footwear(footwear):
NameError: name 'footwear' is not defined
class footwear(accessories):
    pass

class stilettos(footwear):
    pass

Giuseppe_Zanotti=stilettos()

Giuseappe_Zanotti.size
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Giuseappe_Zanotti.size
NameError: name 'Giuseappe_Zanotti' is not defined. Did you mean: 'Giuseppe_Zanotti'?
Giuseappe_Zanotti.size
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    Giuseappe_Zanotti.size
NameError: name 'Giuseappe_Zanotti' is not defined. Did you mean: 'Giuseppe_Zanotti'?
Giuseppe_Zanotti=stilettos()

Giuseppe_Zanotti.size
7
class clothing:
        pass

    
class winterwear(clothing):
            pass

        
class socks(clothing):
            pass

        
class parent:
        eyes='hazel'

        
class mother(parent):
                pass

            
class father(parents):
    pass

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    class father(parents):
NameError: name 'parents' is not defined. Did you mean: 'parent'?
class father(parent):
            pass

        
class child(mother,father):
            pass

        
Rowan=child()
>>> Rowan.eyes
'hazel'
>>> class Athlete:
...     def warning_up(self):
...         print("I am warning up")
...     def sprining(self):
...         print("I am sprinting")
... 
...         
>>> class Champion(Athlete):
...     def gloat(self):
...         super().warning_up()
...         print("I am a champion")
...         super().sprnting()
... 
...         
>>> Bolt=Champion()
>>> Bolt.gloat()
I am warning up
I am a champion
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    Bolt.gloat()
  File "<pyshell#97>", line 5, in gloat
    super().sprnting()
AttributeError: 'super' object has no attribute 'sprnting'
>>> class alice:
...     def sayhi(self):
...         print("I'm Alice")
... 
...         
>>> class bob(alice):
...                 def sayhi(self):
...                     print("I'm Bob")
... 
...                     
>>> bob1=bob()
>>> bob1.sayhi()
I'm Bob
