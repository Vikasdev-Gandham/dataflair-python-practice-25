Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #One's complement- write a function that returns the one's complement of a string representing a binary number.
>>> def ones_complement(bin):
...     return ''.join([str((1,0)[int(digit)]) for digit in bin])
... 
>>> ones_complement('11010')
'00101'
>>> ones_complement('0010')
'1101'
