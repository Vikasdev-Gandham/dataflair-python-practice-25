Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To carry out unit-testing with python
import unittest
def
def Tests(unittest.TestCase0:
          
SyntaxError: invalid syntax
import uniitest
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import uniitest
ModuleNotFoundError: No module named 'uniitest'
import unittest
>>> def modthree(x):
...     return x%3
... 
>>> class Tests(unittest.TestCase):
...     def test(self):
...         self.assertEqual(modthree(4),1)
... 
...         
>>> unittest.main()
.
----------------------------------------------------------------------
Ran 1 test in 0.036s

OK
>>> class TestStringMethods(unittest.TestCase):
...     def test_lstrip(self): #testing for left stripping
...         self.assertEqual(' hello '.lstrip(),'hello ')
...         def test_isupper(self): #testing for isupper
...             self.assertTrue('HELLO'.isupper())
...             self.assertFalse('HELLO'.isupper())
...         def test_split(self): #testing for split
...             self.assertEqual('Hello World'.split(),['Hello','World'])
...         with self.assertRaises(typeError):
...             'Hello World'.split(2)
... 
...             
>>> unittest.main()
E.
======================================================================
ERROR: test_lstrip (__main__.TestStringMethods.test_lstrip)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<pyshell#23>", line 9, in test_lstrip
NameError: name 'typeError' is not defined. Did you mean: 'TypeError'?

----------------------------------------------------------------------
Ran 2 tests in 0.044s

FAILED (errors=1)
