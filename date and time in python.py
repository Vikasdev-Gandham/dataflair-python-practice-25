Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To introduce date and time with python
import time
time.time()
1760506074.4482884
time.gmtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
time.time()
1760506100.4464316
time.localtime()
time.struct_time(tm_year=2025, tm_mon=10, tm_mday=15, tm_hour=10, tm_min=58, tm_sec=27, tm_wday=2, tm_yday=288, tm_isdst=0)
time.localtime(777)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=5, tm_min=42, tm_sec=57, tm_wday=3, tm_yday=1, tm_isdst=0)
time.asctime()
'Wed Oct 15 10:58:43 2025'
time.asctime(time.localtime())
'Wed Oct 15 10:59:18 2025'
time.ctime()
'Wed Oct 15 10:59:31 2025'
time.clock()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    time.clock()
AttributeError: module 'time' has no attribute 'clock'
time.clock()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    time.clock()
AttributeError: module 'time' has no attribute 'clock'
time.clock()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    time.clock()
AttributeError: module 'time' has no attribute 'clock'
time.gmtime()
time.struct_time(tm_year=2025, tm_mon=10, tm_mday=15, tm_hour=5, tm_min=30, tm_sec=28, tm_wday=2, tm_yday=288, tm_isdst=0)
time.mktime(time.localtime())
1760506288.0
time.strftime("B %uth, '%y",time.localtime())
"B 3th, '25"
time.strptime("31 Dec 1995","%d %b %y")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    time.strptime("31 Dec 1995","%d %b %y")
  File "C:\Program Files\Python313\Lib\_strptime.py", line 670, in _strptime_time
    tt = _strptime(data_string, format)[0]
  File "C:\Program Files\Python313\Lib\_strptime.py", line 458, in _strptime
    raise ValueError("unconverted data remains: %s" %
ValueError: unconverted data remains: 95
time.strptime("31 Dec 1995","%d %n %y")
                     
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    time.strptime("31 Dec 1995","%d %n %y")
  File "C:\Program Files\Python313\Lib\_strptime.py", line 670, in _strptime_time
    tt = _strptime(data_string, format)[0]
  File "C:\Program Files\Python313\Lib\_strptime.py", line 447, in _strptime
    raise ValueError("'%s' is a bad directive in format '%s'" %
ValueError: 'n' is a bad directive in format '%d %n %y'
time.strptime("31 Dec 1995","%d %n %Y")
                     
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    time.strptime("31 Dec 1995","%d %n %Y")
  File "C:\Program Files\Python313\Lib\_strptime.py", line 670, in _strptime_time
    tt = _strptime(data_string, format)[0]
  File "C:\Program Files\Python313\Lib\_strptime.py", line 447, in _strptime
    raise ValueError("'%s' is a bad directive in format '%s'" %
ValueError: 'n' is a bad directive in format '%d %n %Y'
time.altzone
                     
-23400
time.timezone
                     
-19800
time.tzname
                     
('India Standard Time', 'India Daylight Time')
>>> calendar.month(2019,12)
...                      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    calendar.month(2019,12)
NameError: name 'calendar' is not defined. Did you forget to import 'calendar'?
>>> import calendar
>>> calender.month(2019,12)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    calender.month(2019,12)
NameError: name 'calender' is not defined. Did you mean: 'calendar'?
>>> calender.month(2019,12)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    calender.month(2019,12)
NameError: name 'calender' is not defined. Did you mean: 'calendar'?
>>> print(calendar.month(2019,12))
   December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

>>> calendar.month(2019,12)
'   December 2019\nMo Tu We Th Fr Sa Su\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28 29\n30 31\n'
>>> print(calendar.month(2025,10))
    October 2025
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

