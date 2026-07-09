Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
evens=[2,4,6,8,10]
evenIterator=iter(evens)
next(evenIterator)
2
next(evenIterator)
4
#One List- Write a function that takes two lists and concatenates them using an iterator
def one_list(list1,list2):
    nums=iter(list1+list2)
    list3=[]
    try:
        while(True):
            list3.append(next(nums))
        except StopIteration:
            
SyntaxError: invalid syntax
def one_list(list1,list2):
    nums=iter(list1+list2)
    list3=[]
    try:
        while(True):
            list3.append(next(nums))
        except StopIteration:
            
SyntaxError: invalid syntax
def one_list(list1,list2):
    nums=iter(list1+list2)
    list3=[]
    try:
        while(True):
            list3.append(next(nums))
        except StopIteration:
            
SyntaxError: invalid syntax
#wrong
#Sort Nums- Write a function that takes in a list holding only intergers and strings, and returns the list with thee intergers sorted without disturbing the positions of the strings.
def sort_nums(items):
    nums=iter(sorted([num for num in items if str(num).isdigit()]))
    res=[]
    for item in items:
        res.append(item) if str(item).isalpha() else res.append(next(nums))
    return res

>>> sort_nums(['cool'])
['cool']
>>> sort_nums9{2, 1])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> sort_nums([2, 1])
[1, 2]
>>> sort_nums(['a', 4,,1,'c', 3, 'b'])
SyntaxError: invalid syntax
>>> sort_nums(['a', 4, 1,'c', 3, 'b'])
['a', 1, 3, 'c', 4, 'b']
>>> sort_nums([2, 'c', 0, 2, 'c', 3, 'b'])
[0, 'c', 2, 2, 'c', 3, 'b']
