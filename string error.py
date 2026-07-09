Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('I\'m an astronaut')
I'm an astronaut
print('I\t\\m an astronaut')
I	\m an astronaut
print('\\/')
\/
a=7
print(f'I have {a} cats')
I have 7 cats
print('I have {0} cats'.format(a))
I have 7 cats
print('I have {a} cats'.format(a=5))
I have 5 cats
print('I have {b} dogs'.format(b=3))
I have 3 dogs
print("%d and %d" %(a,b))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("%d and %d" %(a,b))
NameError: name 'b' is not defined
print("%d and %d" %(a,b))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("%d and %d" %(a,b))
NameError: name 'b' is not defined
b=7
print("%d and %d" %(a,b))
7 and 7
b=11
print("%d and %d" %(a,b))
7 and 11
#Tall, Taller, Taller- Write a function that takes in a person's height in cm and represents it in feet and inches.
def get_height(height):
    feet=height/30.48
    inches=(feet%1)*12
    print(f'You are (int(feet))\' (round(inches.1))" tall.')

    

get_height(160)
You are (int(feet))' (round(inches.1))" tall.
get_height(179)
You are (int(feet))' (round(inches.1))" tall.
#Tall, Taller, Taller- Write a function that takes in a person's height in cm and represents it in feet and inches.
def get_height(height):
    feet=height/30.48
    inches=(feet%)*12
    
SyntaxError: invalid syntax
def get_height(height):
    feet=height/30.48
    inches=(feet%1)*12
    print*f'You are (int*feet))\' (round(inches,1))" tall.')
    
SyntaxError: unmatched ')'
def get_height(height)
SyntaxError: expected ':'
def get_height(height)
SyntaxError: expected ':'
def get_height(height):
    feet=height/30.48
    inches=(feet%1)*12
    print(f'You are (int(feet))\' (round(inches,1)" tall.')

    
get_height(160)
You are (int(feet))' (round(inches,1)" tall.
def get_height(height):
    feet=height/30.48
    inches=(feet%1)*12
    print(f'You are {int(feet)}\' {round(inches,1)}" tall.')

    
get_height(160)
You are 5' 3.0" tall.
get_height(179)
You are 5' 10.5" tall.
get_height(134)
You are 4' 4.8" tall.
#To Gerumd- Write a function that takes a verb and converts it into its gerund form. gerund is a verb form that functions as a noun, ending in 'ing'
def to_gerund(verb):
    if verb([-1]=='e':
            
SyntaxError: invalid syntax
def to_gerund(verb):
    if verb[-1]=='e':
        return f'(verb) becomes {verb[:-1]+"ing")'
    
SyntaxError: f-string: unmatched ')'
def to_gerund(verb):
    if verb[-1]=='e':
        return f'{verb} becomes {verb[:-1]+"ing"}
    
SyntaxError: unterminated f-string literal (detected at line 3)
def to_gerun(verb):
    if verb[-1]=='e':
        return f'{verb} becomes {verb[:-1]+"ing"}'
    if verb[-3]!='ing':
        return f'{verb} becomes {verb+"ing"}'
    return verb

to_gerund('bake')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    to_gerund('bake')
NameError: name 'to_gerund' is not defined. Did you mean: 'to_gerun'?
to_gerun('bake')
'bake becomes baking'
def to_gerund(verb):
    if verb[-1]=='e':
        return f'{verb} becomes {verb[:-1]+"ing"}'
    if verb[-3:]!='ing':
        return f'{verb} becomes {verb+"ing"}'
    return verb

to_gerund('bake')
'bake becomes baking'
to_gerund('jump')
'jump becomes jumping'
to_gerund('hike')
'hike becomes hiking'
to_gerund('bathe')
'bathe becomes bathing'
to_gerund('hitting')
'hitting'
#Only Even Caps- Write a function that takes in a string. Make it capitalize the letters with even ASCII values and turn to lowercase those with odd ASCII values.
def even_caps(sentence):
    s=''
    for char in sentence:
        if char.isalpha() and ord(char)!=32:
            if char.islower() and ord(char)%2==0:
                s+=char(ord(char)-32)
            elif char.isupper() and ord(char)%2!=0:
                s+=chr(ord(char)+32
            else: s+=char
            
SyntaxError: '(' was never closed
def even_caps(sentence):
    s=''
    for char in sntence:
        if char.isalpha() and ord(char)!=32:
            if char.islower() and ord(char)$2==0:
                
SyntaxError: invalid syntax
def even_caps(sentence):
    s=''
    for char in sentence:
        if char.isalpha() and ord(char)!=32:
            if char.islower() and ord(char)%2==0:
                s+=chr(ord(char)-32)
            elif char.isupper() and ord(char)%2!=0:
                s+=chr(ord(char)+32)
            else: s+=char
        else: s+=char
    return s

even_caps('I got all i need in a world of doubt')
'i goT aLL i NeeD iN a woRLD oF DouBT'
>>> even_caps('Here in the ashes, your soul cries out')
'HeRe iN THe asHes, youR souL cRies ouT'
>>> #Abbreviation- write a function that takes in two lists. the first holds abbreviations and the second holds words. your task is to make it make sure no abbreviation suggests more than one word in the second list.
>>> def abbreviation(abbs,words):
...     for abb in abbs:
...         count=0
...         for word in words:
...             if word.startswith(abb):
...                 count+=1
...             if count!=1: return flase
...         return true
... 
...     
>>> abbreviation(['h','hel','b'],['help','hello','holy','blased','helium'])
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    abbreviation(['h','hel','b'],['help','hello','holy','blased','helium'])
  File "<pyshell#124>", line 7, in abbreviation
    if count!=1: return flase
NameError: name 'flase' is not defined
>>> abbreviation(['ho','help','heli','b'],['help','hello','holy','biased','helium'])
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    abbreviation(['ho','help','heli','b'],['help','hello','holy','biased','helium'])
  File "<pyshell#124>", line 7, in abbreviation
    if count!=1: return flase
NameError: name 'flase' is not defined
>>> def abbreviation(abbs,words):
...     for abb in abbs:
...         count=0
...         for word in words:
...             if word.startswith(abb):
...                 count+=1
...             if count!=1: return false
...         return true
... abbreviation(['h','hel','b'],['help','hello','holy','biased','helium'])
SyntaxError: invalid syntax
>>> abbreviation(['h','hel','b'],['help','hello','holy','biased','helium'])
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    abbreviation(['h','hel','b'],['help','hello','holy','biased','helium'])
  File "<pyshell#124>", line 7, in abbreviation
    if count!=1: return flase
NameError: name 'flase' is not defined
