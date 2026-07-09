Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lingo={'PB&J':'Peanut Butter and Jelly','PJ':'Pyjamas'}
{x*x:x for x in range(8)}
{0: 0, 1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7}
animals={}
animals[1]='dog'
animals[2]='cat'
animals[3]='ferret'
animals
{1: 'dog', 2: 'cat', 3: 'ferret'}
animals[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    animals[4]
KeyError: 4
sorted(animals)
[1, 2, 3]
animals.keys()
dict_keys([1, 2, 3])
animals.get(2,0)
'cat'
#The Costliest Three- You are given a dictionary holding items a store, and their prices. write a function that returns the items with the highest price, the second-heighest, and the third-highest. if two items cost the same, include both.
def the_costliest_three(items):
    for item in [(item,price) for (item,price) in items.items() if price in sorted(items.values())[-3:]]:
        print(item)

        
the_costliest_three({'shoes': 79, 'scarves': 29, 'berets': 39, 'bodysuits': 59, 'leggings': 39})
('shoes', 79)
('berets', 39)
('bodysuits', 59)
('leggings', 39)
>>> the_costliest_three({'shoes': 79, 'scarves': 29, 'berets': 39, 'bodysuits': 59, 'leggings': 39, 'sweaters':129})
('shoes', 79)
('bodysuits', 59)
('sweaters', 129)
>>> #Roll Numbers- Write a function that takes a list of the names of students and assigns roll numbers to first names in a lexicographic order, then prints them out.
>>> def rolls(names):
...     roll_nums={sorted(names).index(name)+1:name.split(' ')[0] for name in sorted(names)}
...     for roll in sorted(roll_nums): print (roll,roll_nums[rool])
... 
...     
>>> rolls(['Ayushi Sharma', 'Anjali Raizada', 'Zoya Khan', 'Rinu Srivastava'])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    rolls(['Ayushi Sharma', 'Anjali Raizada', 'Zoya Khan', 'Rinu Srivastava'])
  File "<pyshell#22>", line 3, in rolls
    for roll in sorted(roll_nums): print (roll,roll_nums[rool])
NameError: name 'rool' is not defined. Did you mean: 'roll'?
>>> rollls(['Ayushi Sharma', 'Anjali Raizada', 'Zoya khan', 'Ritu Srivastava'])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    rollls(['Ayushi Sharma', 'Anjali Raizada', 'Zoya khan', 'Ritu Srivastava'])
NameError: name 'rollls' is not defined. Did you mean: 'rolls'?
>>> def rolls(names):
...     roll_nums={sorted(names).index(name)+1:name.split(' ')[0] for name in sorted(names)}
...     for roll in sorted(roll_nums): print (roll,roll_nums[roll])
... 
...     
>>> roll(['Ayushi Sharma', 'Anjali Raizada', 'Zoya khan', 'Ritu Srivastava'])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    roll(['Ayushi Sharma', 'Anjali Raizada', 'Zoya khan', 'Ritu Srivastava'])
NameError: name 'roll' is not defined. Did you mean: 'rolls'?
>>> rolls(['Ayushi Sharma', 'Anjali Raizada', 'Zoya khan', 'Ritu Srivastava'])
1 Anjali
2 Ayushi
3 Ritu
4 Zoya
