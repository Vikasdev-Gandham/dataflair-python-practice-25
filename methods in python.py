Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To implement methods in python
class Car:
    def __init__(self,brand,model,color,fuel):
        self.brand=brand
        self.model=model
        self.color=color
        self.fuel=fuel
    def start(self):
        pass
    def halt(self):
        pass
    def drift(self):
        pass
    def speedup(self):
        pass
    def turn(self):
        pass

    
blackverna=Car('Hyundai','Verna','Black','Diesel')
blackverna.drift()
class Try:
    def __init__(self):
        pass
    def printhello(self,name):
        print(f"Hello, {name}")
        return name

    
Try().printhello('Ayushi')
Hello, Ayushi
'Ayushi'
class Result:
    def __init__(self,phy,chem,math):
            self.phy=phy
            self.chem=chem
            self.math=math
    def
    
SyntaxError: invalid syntax
class Result:
    def __init__(self,phy,chem,math):
            self.phy=phy
            self.chem=chem
            self.math=math
    def
    
SyntaxError: invalid syntax
class Result:
    def __init__(self,phy,chem,math):
            self.phy=phy
            self.chem=chem
            self.math=math
    def printavg(self):
        print(f"Average={(self.phy+self.chem+self.math)/3")
        
SyntaxError: f-string: expecting '}'
class Result:
    def __init__(self,phy,chem,math):
            self.phy=phy
            self.chem=chem
            self.math=math
    def printavg(self):
        print(f"Average={(self.phy+self.chem+self.math)/3)")
        
SyntaxError: f-string: unmatched ')'
class Result:
    def __init__(self.phy,chem,math):
        
SyntaxError: invalid syntax
class Result:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    def printavg(self):
        print(f"Average={ (self.phy+self.chem+self.math)/3}")

        
#Funny Parentheses- Write a function that validates a string with parentheses, curly braces, and square brackets.
        
class parentheses:
    def is_valid(self,str):
        stack,valid=[],{'(':')','[':']','{':'},}
                        
SyntaxError: unterminated string literal (detected at line 3)
class parentheses:
    def is_valid(self,str):
        stack,valid=[],{'(':')','[':']','{':'}'}
        for char in str:
            if char in valid:
                stack.append(char)
            elif len(stack)==0 or valid[stack.pop()]!=char:
                return False
            return len(stack)==0

        
p=parentheses()
p.is_valid('()[]{}')
False
p.is_valid('()[]{([)]}')
False
p.is_valid('([)]')
False
p.is_valid('()[]{}')
False
#Mirror, Mirror- Write a function that validates a string with parentheses, curly braces, and square brackets.
class mirror:
    def mirrored_words(self,text):
        return ' '.join(reversed(text.spliut()))

    
mirror().mirrored_woords('two joys and few perils')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    mirror().mirrored_woords('two joys and few perils')
AttributeError: 'mirror' object has no attribute 'mirrored_woords'. Did you mean: 'mirrored_words'?
mirror().mirrored_words('two joys and few perils')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    mirror().mirrored_words('two joys and few perils')
  File "<pyshell#68>", line 3, in mirrored_words
    return ' '.join(reversed(text.spliut()))
AttributeError: 'str' object has no attribute 'spliut'. Did you mean: 'split'?
>>> class mirror:
...     def mirrored_words(self,text):
...         return ' '.join(reversed(text.split()))
... 
...     
>>> mirror().mirrored_words('two joys and few perils')
'perils few and joys two'
