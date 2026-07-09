Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=7
if a>6:
    print("Hello")
    print("How are you?")

    
Hello
How are you?
if a>7: print("Hi")
else: print("Hello")

Hello
if a>4:
    print("Hi")
    if a>7: print("Hello")

    
Hi
if a>4:print("4")
else a>6: print("6")
SyntaxError: expected ':'
if a>4: print("4")
else a>6: print("6")
SyntaxError: expected ':'
else a>6: print("6")
SyntaxError: invalid syntax
if a>4: print"(4")
SyntaxError: unmatched ')'
if a>4: print("4")
elif a>6: print("6")
else: print("7")

4
if a>4 and a<8: print("yes")

yes
#Fizzbuzz- write a program to print numbers 1 to 100, each on a new line.
#Print "Fizz" at the place of numbers multiples of 3.
#Print "Buss" at the place of numbers mulipoles of 5.
#Print "FizzBuzz" at the place of numbers muliples of both 3 and 5.
def fizzbuss():
    for num in range(1, 101):
        if num%3==0: print("Fizz",end='');
        if num%5==0: print("Buzz");continue
        if num%3==0: print(); continue
        print(num)

        
fizzbuzz()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    fizzbuzz()
NameError: name 'fizzbuzz' is not defined. Did you mean: 'fizzbuss'?
fizzbuss()
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
def fizzbuzz():
    for in range(1, 101):
        
SyntaxError: invalid syntax
def fizzbuzz():
    for num in range(1,101):
        if num%3==0: print("Fizz",end='');
        if num%5==0: print("Buzz"); continue
        if num%3==0: print(); continue
        print(num)

        
fizzbuzz()
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
#Double Sum- write a function that returns the sum of two inegers. if, however, the first is twice the second, return twice their sum,
>>> def double_sum(a,b):
...     return(1+int(a==2*b))*(a+b)
... 
>>> double_sum(2,3)
5
>>> double_sum(4,2)
12
>>> double_sum(4,_2)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    double_sum(4,_2)
NameError: name '_2' is not defined
>>> double_sum(4,-2)
2
>>> #All evens- write a function that takes an inclusive inerval from the user returns all values where all digits are even.
>>> def all_evens(a,b, res=[]):
...     for num in range(a,b+1):
...         if all([int(digit)%2==0 for digit in [char for char in str(num)]]):
...             res.append(num)
...     return res
... all_evens(200,500)
SyntaxError: invalid syntax
>>> all_evens(200,500)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    all_evens(200,500)
NameError: name 'all_evens' is not defined
>>> def all_evens(a,b,res=[]):
...     for num in range(a,b+1):
...         if all([int(digit)%2==0 for digit in [char for char in str(num)]]):
...             res.append(num)
...         return res
... 
...     
>>> all_evens(200,500)
[200]
>>> all_evens(200, 500)
[200, 200]
