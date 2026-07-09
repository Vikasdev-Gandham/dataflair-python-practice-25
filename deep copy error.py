Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import copy
help(copy.copy)
Help on function copy in module copy:

copy(x)
    Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.

help(copy.deepcopy)
Help on function deepcopy in module copy:

deepcopy(x, memo=None, _nil=[])
    Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.

raise copy.error
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    raise copy.error
copy.Error
from copy import copy
list1=[1,[2,3]]
list2=copy(list)
list2
<class 'list'>
list1
[1, [2, 3]]
list[1][1]=4
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list[1][1]=4
TypeError: 'types.GenericAlias' object does not support item assignment
li
list2[1][1]=4
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list2[1][1]=4
TypeError: 'types.GenericAlias' object does not support item assignment
>>> list1
[1, [2, 3]]
>>> list2[1][1]=4
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list2[1][1]=4
TypeError: 'types.GenericAlias' object does not support item assignment
>>> list2[1][1]=4
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list2[1][1]=4
TypeError: 'types.GenericAlias' object does not support item assignment
>>> list2
<class 'list'>
>>> list1
[1, [2, 3]]
>>> from copy import deepcopy
>>> list1=[1,[2,3]]
>>> list2=deepcopy(list1)
>>> list2
[1, [2, 3]]
>>> list2
[1, [2, 3]]
>>> list2[1][1]=4
>>> list2
[1, [2, 4]]
>>> list1
[1, [2, 3]]
>>> dict={'a':1,'b':2,'c':[1,2,3]}
>>> dict2=dict1.copy()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict2=dict1.copy()
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
>>> dict2=dict1.copy()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict2=dict1.copy()
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
