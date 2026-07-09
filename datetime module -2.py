Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To understand the datetime classs from the datetime module.
from datetime import datetime
datetime.now()
datetime.datetime(2025, 10, 17, 11, 27, 38, 376346)
import time
d=datetime.fromtimestamp(time.time())
d
datetime.datetime(2025, 10, 17, 11, 28, 4, 992251)
d.month
10
d.date()
datetime.date(2025, 10, 17)
datetime.date(2019, 6, 15)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    datetime.date(2019, 6, 15)
TypeError: descriptor 'date' for 'datetime.datetime' objects doesn't apply to a 'int' object
d.timestamp()
1760680684.992251
d.isoformat()
'2025-10-17T11:28:04.992251'
from datetime import timedelta
d+timedelta(7)
datetime.datetime(2025, 10, 24, 11, 28, 4, 992251)
#Right Now- Write a function that prints the date and time at this moment as a string
def right_now():
    now=datetime.now()
    return now.strftime("%Y/%m/%d %H:%M:%S %p")

right_now()
'2025/10/17 11:32:06 AM'
>>> right_now()
'2025/10/17 11:32:14 AM'
>>> #Running Length- Write a function that takes in the running length of a movie in minutes and returns the same in hours and minutes.
>>> import datetime
>>> def running_length(mins):
...     duration=str(datetime.timedelta(minutes=mins)).split(':')
...     return f'{duration[0]}h {duration[1]}min'
... 
>>> running_length(200)
'3h 20min'
>>> running_length(160)
'2h 40min'
