Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import array
>>> arr=array.array('i',[7,9,8])
>>> arr
array('i', [7, 9, 8])
>>> array.array('u','hello\u2641')

Warning (from warnings module):
  File "<pyshell#3>", line 1
DeprecationWarning: The 'u' type code is deprecated and will be removed in Python 3.16
array('u', 'hello♁')
>>> array.typecodes
'bBuwhHiIlLqQfd'
>>> arr.typecode
'i'
>>> arr.append(6)
>>> arr
array('i', [7, 9, 8, 6])
>>> arr=array.array('i',[7,9,6,7,2,5])
>>> arr.count(7)
2
>>> arr.insert(2,4)
>>> arr
array('i', [7, 9, 4, 6, 7, 2, 5])
>>> arr.pop(2)
4
>>> arr.tolist()
[7, 9, 6, 7, 2, 5]
>>> arr[2:7]
array('i', [6, 7, 2, 5])
