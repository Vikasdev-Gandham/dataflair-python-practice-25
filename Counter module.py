Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import Counter
c=Counter(['a','b','c','a','b','a'])
c
Counter({'a': 3, 'b': 2, 'c': 1})
Counter("hello")
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
for item in c.elements(): print(item,end='')

aaabbc
c.most_common(2)
[('a', 3), ('b', 2)]
c+c
Counter({'a': 6, 'b': 4, 'c': 2})
#String Compression- Write a function that takes a string and returns a compressed version of it. compress mulitple occurrences of a letter to hold the letter andd its count. Assume that duplicates only exist together.
def compress(string):
    s=''
    count=Counter(string)
    for letter in count:
        s+=letter+str(count[letter])
    return s

compress("AAAAaaBCCCSDDe")
'A4a2B1C3S1D2e1'
#Top Search- Write a function that takes a history of searched keywords and declares tha most-searched keywords along with the number of searches.
>>> def top_searh(keywords):
...     counter=Counter(keywords)
...     return f'{counter.most_common(1)[0][0]} was searched {counter.most_common(1)[0][1]} times'
... 
>>> keywords['Python','Java','Python','c','Lisp','JavaScript','Java','C++','C++','C#','Swift','C++','Python','Java']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    keywords['Python','Java','Python','c','Lisp','JavaScript','Java','C++','C++','C#','Swift','C++','Python','Java']
NameError: name 'keywords' is not defined
>>> def top_search(keywords):
...     counter=Counter(keywords)
...     return f'{counter.most_common(1)[0][0]} was searched {counter.most_common(1)[0][1]} times'
... 
>>> keywords['Python','Java','Python','c','Lisp','JavaScript','Java','C++','C++','C#','Swift','C++','Python','Java']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    keywords['Python','Java','Python','c','Lisp','JavaScript','Java','C++','C++','C#','Swift','C++','Python','Java']
NameError: name 'keywords' is not defined
>>> def top_search(keywords):
...     counter=Counter(keywords)
...     return f'{counter.most_common(1)[0][0]} was searched {counter.most_common(1)[0][1]} times'
... 
>>> keywords=['Python','Java','Python','c','Lisp','JavaScript','Java','C++','C++','C#','Swift','C++','Python','Java']
>>> top_search(keywords)
'Python was searched 3 times'
