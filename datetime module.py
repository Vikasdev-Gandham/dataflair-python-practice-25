Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To explore the datetime module- date, time
from datetime import date
date.today()
datetime.date(2025, 10, 17)
date.today().month
10
date.today().weekday()
4
from datetime import timedelta
date.today()+timedelta(5)
datetime.date(2025, 10, 22)
from datetime import time
time.max
datetime.time(23, 59, 59, 999999)
t=time(12)
t=t.replace(hour=16,minuts=55)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t=t.replace(hour=16,minuts=55)
TypeError: replace() got an unexpected keyword argument 'minuts'. Did you mean 'minute'?
t=time(12)
t=t.replace(hour=16,minuts=55)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t=t.replace(hour=16,minuts=55)
TypeError: replace() got an unexpected keyword argument 'minuts'. Did you mean 'minute'?
t
datetime.time(12, 0)
#days from Today- Write a function that takes in a number of days and returns the date that many days from today.
def days_from_today(days):
    return date.today()+timedelta(days)

days_from_today(21)
datetime.date(2025, 11, 7)
#Age Calculator- Write a function that takes in the date of birth and calculates the age today.
def age_calculator(birthdate):
    today=date.today()
    year,month,day=birthdate.splite('/')
    return str(today.year-birthdate.year=((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

    today=date.today()
    year,month,day=birthdate.splite('/')
    return str(today.year-birthdate.year=((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'SyntaxError: expression cannot contain assignment, perhaps you meant "=="?def age_calculator(birthdate):
        today=date.today()
        year,month,day=birthdate.splite('/')
        return str(today.year-birthdate.year=((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'
    
SyntaxError: unexpected indent
def age_calculator(birthdate):
    today=date.today()
    year,month,day=birthdate.splite('/')
    birthdate=date(int(year,int(month),int(day))
    return str(today.year-birthdate.year=((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'
SyntaxError: '(' was never closed
def age_calculator(birthdate):
    today=date.today()
    year,month,day=birthdate.splite('/')
    birthdate=date(int(year),int(month),int(day))
    return str(today.year-birthdate.year=((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
def age_calculator(birthdate):
    today=date.today()
    year,month,day=birthdate.splite('/')
    birthdate=date(int(year),int(month),int(day))
    return str(today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'

age_calculator('1995/12/31')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    age_calculator('1995/12/31')
  File "<pyshell#28>", line 3, in age_calculator
    year,month,day=birthdate.splite('/')
AttributeError: 'str' object has no attribute 'splite'. Did you mean: 'split'?
def age_calculator(birthdate):
    today=date.today()
    year,month,day=birthdate.split('/')
    birthdate=date(int(year),int(month),int(day))
    return str(today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day)))+' years'

age_calculator('1995/12/31')
'29 years'
age_calculator('1991/31/07')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    age_calculator('1991/31/07')
  File "<pyshell#31>", line 4, in age_calculator
    birthdate=date(int(year),int(month),int(day))
ValueError: month must be in 1..12
>>> age_calculator('1991/31/7')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    age_calculator('1991/31/7')
  File "<pyshell#31>", line 4, in age_calculator
    birthdate=date(int(year),int(month),int(day))
ValueError: month must be in 1..12
>>> age_calculator('1991/07/31')
'34 years'
>>> age_calculator('1989/09/15')
'36 years'
>>> age_calculator('1992/09/15')
'33 years'
>>> age_calculator('1993/03/08')
'32 years'
