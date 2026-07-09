Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> print.(re.match('meow','homeowner'))
SyntaxError: invalid syntax
>>> print(re.match('meow','homeowner'))
None
>>> print(re.search('meow','homeowner'))
<re.Match object; span=(2, 6), match='meow'>
>>> re.search('\w+c{2}\w*','Occam\'s Razor').group()
'Occam'
>>> re.search('[\w.-]+@[\w-]+\.[\w]+','Drop a mail at info@data-flair.training').group()
'info@data-flair.training'
>>> #Is Float- Write a function that checks whether a number input to it is a floating-point number.
>>> from re import match
>>> def is_float(item):
...     return bool(match("^[+-]?\d*\.\d*$",str(item)))
... 
>>> is_float(-0.0)
True
>>> is_float(2)
False
>>> is_float2.4)
SyntaxError: unmatched ')'
>>> is_float(2.4)
True
>>> #Removing Comments- Write a function that takes in HTML code and removes any comments from it.
>>> def removing_comments(html):
...     print(re.sub("<!--.*?-->","",html))
... 
...     
>>> removing_comments("""
... <head></head>
... <body>
...     <p>Hello, world</p>
...     <!-- This is a comment -->
</body>""")

<head></head>
<body>
    <p>Hello, world</p>
    
</body>
