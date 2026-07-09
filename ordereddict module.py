Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand the OrderDict in python
from collections import OrderDict
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from collections import OrderDict
ImportError: cannot import name 'OrderDict' from 'collections' (C:\Program Files\Python313\Lib\collections\__init__.py). Did you mean: 'OrderedDict'?
from collections import OrderedDict
d = OrderedDict()
d['a']=1
d['e']=5
d['d']=4
d['b']=2
d['c']=3
d
OrderedDict({'a': 1, 'e': 5, 'd': 4, 'b': 2, 'c': 3})
d.move_to_end('e')
d['e']=7
d
OrderedDict({'a': 1, 'd': 4, 'b': 2, 'c': 3, 'e': 7})
d['e']=5
d
OrderedDict({'a': 1, 'd': 4, 'b': 2, 'c': 3, 'e': 5})
d.popitem()
('e', 5)
#Delicious Diners- you have joined as assistant to the head chef in a new restaurant. Write a function that takes a list of orders with the item and their quantities, and informs the chef of the quantity to prepare for each item ordered. Make sure to do this in the order of orders received.
def diner(orders):
    new_orders=OrderedDict()
    for item, quantity in orders:
        if item not in new_orders:
            new_orders[item]=quantity
        else:
            new_orders[item]+=quantity
        for item, quantity in new_orders.items():
            print(item,quantity)

            
diner([('deviled eggs',2),('ham',1),('deviled eggs',1)])
deviled eggs 2
deviled eggs 2
ham 1
deviled eggs 3
ham 1
>>> diner([('ham',1),('deviled eggs',2),('deviled eggs',1)])
ham 1
ham 1
deviled eggs 2
ham 1
deviled eggs 3
