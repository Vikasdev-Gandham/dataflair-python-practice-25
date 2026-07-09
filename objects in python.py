Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objects- To create objects for classes in python
class fruit:
    def __init__(self,color,shape):
        self.color=color
        self.shape=shape
    def sayhi(self):
        print(f"Hi..\nI am {self.color}and{self.shape}")

        
orange = fruit('Orange','Round')
orange.sayhi()
Hi..
I am OrangeandRound
class Person:
    def sayhi(self):
        print("Hi")

        
Maddie=Person()
Maddie.sayhi()
Hi
Liv = Maddie
Liv.sayhi()
Hi
del Maddie
Li
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Li
NameError: name 'Li' is not defined
Liv
<__main__.Person object at 0x000001D698752F90>
orange.size=7
del orange
orange
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    orange
NameError: name 'orange' is not defined. Did you mean: 'range'?
#Queen of Hearts- Write a class dealing with a deck of cards of only hearts. Implement functionality to shuffle, deal a card, and show the cards in the current sequence.
import random
class Deck:
    def __init__(self):
        self.cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.shuffle()
    def deal(self):
        card=random.choice(self.cards)
        self.cards.remove(card)
        return f'You got {card}'
    def shuffle(self):
        random.shuffle(self.cards)
    def show(self):
        return self.cards

    
>>> d=Deck()
>>> d.show()
[5, 'Q', 2, 9, 7, 'J', 3, 6, 'A', 10, 'K', 8, 4]
>>> d.deal()
'You got 3'
>>> d.show()
[5, 'Q', 2, 9, 7, 'J', 6, 'A', 10, 'K', 8, 4]
>>> d.shuffle()
>>> d.show()
[2, 'A', 9, 8, 'Q', 'J', 5, 'K', 6, 7, 10, 4]
