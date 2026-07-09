Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(num1,num2):
...     return num1+num2
... 
>>> add(2,-3)
-1
>>> def hello():
...     """
...     This function says hello
...     """
...     print("Hello")
... 
...     
>>> hello._doc_
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    hello._doc_
AttributeError: 'function' object has no attribute '_doc_'. Did you mean: '__doc__'?

>>> hello._doc_
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    hello._doc_
AttributeError: 'function' object has no attribute '_doc_'. Did you mean: '__doc__'?
>>> hello._doc_ '\n\tThis function says hello\n\t'
SyntaxError: invalid syntax
>>> hello._doc_ '\n\tThis function says hello\n\t'
SyntaxError: invalid syntax
>>> def add(num1,num2):
...     return num1+num2
... 
>>> add(2,-3)
-1
>>> def hello():
...     """
...     This function says hello
...     """
...     print("Hello')
...           
SyntaxError: unterminated string literal (detected at line 5)

def hello():
    """
    This function says hello
    """
    print("Hello")

    
hello.__doc__
'\nThis function says hello\n'
(lambda a,b:a**(b+2)(3,4))
<function <lambda> at 0x00000262C69D2340>
wrong
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    wrong
NameError: name 'wrong' is not defined
#nth Prime- Write a function (you may use helper functions) that takes in a number and returns the nth prime number.
def is_prime(n):
    if n==1: return false
    for num in range(2,int(n/2)+1):
        if n%num==0: return false
        return true

    
def.next_prime(n):
    
SyntaxError: invalid syntax
def.next_prime(n):
    
SyntaxError: invalid syntax
def next_prime(n):
    num=n+1
    while num>n:
        if is prime(num): return num
        
SyntaxError: invalid syntax
def next_pime(n):
    num=n+1
    while num>n:
        if is_prime(num): return num
        num+=1

        
def nth_prime(n):
    count,p=0,2
    while count<1: p=next_prime(p); count+=1
    return p

nth_prime(1)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    nth_prime(1)
  File "<pyshell#69>", line 3, in nth_prime
    while count<1: p=next_prime(p); count+=1
NameError: name 'next_prime' is not defined. Did you mean: 'next_pime'?
def is_prime(n):
    if n==1: return False
    for num in range(2,int(n/2)+1):
        if n%num==0: return False
        return True

    
def next_prime(n):
    num=n+1
    while num>n:
        if is_prime(num): return num
        num+=1

        
def nth_prime(n):
    count,p=0,2
    while count<n-1: p=next_prime(p); count+=1
    return p

nth_prime(1)
2
nth_prime(4)
9
nth_prime(10)
21
#Caesar Cipher- Write a function implementing the caesar cipher. such a cipher is one that user a very simple encryption technique. If the key is 2, 'a' become 'c', 'b' comes 'a', and so on. This completes a full cycles as 'y' becomes 'A' and 'z' becomes 'B'. Encrypt messages to send to a friend.
def caesar(message,key):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=''
    for letter in message:
        if letter in ' !@#$%^&*()_-+={[}]:;"\'<,>.?/~`': s+=letter; continue
        return s

    
caesar('Did you blow the whistle yet?',3)
''
caesar('Did you blow the whistle yet?',2)
''
def caesar(message,key):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=''
    for letter in message:
        if letter in ' !@#$%^&*()_-+={[}]:;"\'<,>.?/~`': s+=letter; continue
        s+=alphabet[(alphabet.index(letter)+key)%52]
        return s

    
caesar('Did you blow the whisle yet?',3)
'G'
caesar('Did you blow the whistle yet?',2)
'F'
