Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To explore the calendar module in python
import calendar as cd
cal=cd.Calendar(firstweekday=2)
for weekday in cal.interweekdays():
    print(weekday)

    
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    for weekday in cal.interweekdays():
AttributeError: 'Calendar' object has no attribute 'interweekdays'. Did you mean: 'iterweekdays'?
cal=cd.Calendar(firstweekday=2)
for weekday in cal.interweekdays():
    print(weekday)

    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for weekday in cal.interweekdays():
AttributeError: 'Calendar' object has no attribute 'interweekdays'. Did you mean: 'iterweekdays'?
cal=cd.Calendar(firstweekday=2)
for weekday in cal.iterweekdays():
    print(weekday)

    
2
3
4
5
6
0
1
cal=cd.Calendar(firstweekday=0)
for date in cal.itermonthdates(2025,12):
    print(date,end=', ')

    
2025-12-01, 2025-12-02, 2025-12-03, 2025-12-04, 2025-12-05, 2025-12-06, 2025-12-07, 2025-12-08, 2025-12-09, 2025-12-10, 2025-12-11, 2025-12-12, 2025-12-13, 2025-12-14, 2025-12-15, 2025-12-16, 2025-12-17, 2025-12-18, 2025-12-19, 2025-12-20, 2025-12-21, 2025-12-22, 2025-12-23, 2025-12-24, 2025-12-25, 2025-12-26, 2025-12-27, 2025-12-28, 2025-12-29, 2025-12-30, 2025-12-31, 2026-01-01, 2026-01-02, 2026-01-03, 2026-01-04, 
for day in cal.itermonthdays(2019,12):
    print(day,end=', ')

    
0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 0, 0, 0, 0, 0, 
for item in cal.monthdatescalendar(2019,12):
    print(item,end=', ')

    
[datetime.date(2019, 11, 25), datetime.date(2019, 11, 26), datetime.date(2019, 11, 27), datetime.date(2019, 11, 28), datetime.date(2019, 11, 29), datetime.date(2019, 11, 30), datetime.date(2019, 12, 1)], [datetime.date(2019, 12, 2), datetime.date(2019, 12, 3), datetime.date(2019, 12, 4), datetime.date(2019, 12, 5), datetime.date(2019, 12, 6), datetime.date(2019, 12, 7), datetime.date(2019, 12, 8)], [datetime.date(2019, 12, 9), datetime.date(2019, 12, 10), datetime.date(2019, 12, 11), datetime.date(2019, 12, 12), datetime.date(2019, 12, 13), datetime.date(2019, 12, 14), datetime.date(2019, 12, 15)], [datetime.date(2019, 12, 16), datetime.date(2019, 12, 17), datetime.date(2019, 12, 18), datetime.date(2019, 12, 19), datetime.date(2019, 12, 20), datetime.date(2019, 12, 21), datetime.date(2019, 12, 22)], [datetime.date(2019, 12, 23), datetime.date(2019, 12, 24), datetime.date(2019, 12, 25), datetime.date(2019, 12, 26), datetime.date(2019, 12, 27), datetime.date(2019, 12, 28), datetime.date(2019, 12, 29)], [datetime.date(2019, 12, 30), datetime.date(2019, 12, 31), datetime.date(2020, 1, 1), datetime.date(2020, 1, 2), datetime.date(2020, 1, 3), datetime.date(2020, 1, 4), datetime.date(2020, 1, 5)], 
for day in cal.monthdayscalendar(2019,12):
    print(day)

    
[0, 0, 0, 0, 0, 0, 1]
[2, 3, 4, 5, 6, 7, 8]
[9, 10, 11, 12, 13, 14, 15]
[16, 17, 18, 19, 20, 21, 22]
[23, 24, 25, 26, 27, 28, 29]
[30, 31, 0, 0, 0, 0, 0]
textcal=cd.TextCalendar(0)
textcal.prmonth(2019,12)
   December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
textcal.pryear(2019,m=5)
                                                            2019

      January                   February                   March                     April                      May
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                   1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31      29 30                     27 28 29 30 31

        June                      July                     August                  September                  October
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4                         1          1  2  3  4  5  6
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
                                                                              30

      November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1
 4  5  6  7  8  9 10       2  3  4  5  6  7  8
11 12 13 14 15 16 17       9 10 11 12 13 14 15
18 19 20 21 22 23 24      16 17 18 19 20 21 22
25 26 27 28 29 30         23 24 25 26 27 28 29
                          30 31
textcal.pryear(2025,m=12)
                                                                                                                                                       2025

      January                   February                   March                     April                      May                       June                      July                     August                  September                  October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2          1  2  3  4  5  6                1  2  3  4                         1          1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7             1  2  3  4  5                      1  2       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30 31      29 30                     27 28 29 30 31            24 25 26 27 28 29 30      29 30 31
                                                    31                                                                            30
textcal.pryear(2025,m-4)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    textcal.pryear(2025,m-4)
NameError: name 'm' is not defined
textcal.pryear(2025,m=5)
                                                            2025

      January                   February                   March                     April                      May
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2          1  2  3  4  5  6                1  2  3  4
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
                                                    31

        June                      July                     August                  September                  October
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1          1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30 31      29 30                     27 28 29 30 31
30

      November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7
 3  4  5  6  7  8  9       8  9 10 11 12 13 14
10 11 12 13 14 15 16      15 16 17 18 19 20 21
17 18 19 20 21 22 23      22 23 24 25 26 27 28
24 25 26 27 28 29 30      29 30 31
htmlcal=cd.HTMLCalendar()
print(htmlcal.formatmonth(2019,12))
<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">December 2019</th></tr>
<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sun">1</td></tr>
<tr><td class="mon">2</td><td class="tue">3</td><td class="wed">4</td><td class="thu">5</td><td class="fri">6</td><td class="sat">7</td><td class="sun">8</td></tr>
<tr><td class="mon">9</td><td class="tue">10</td><td class="wed">11</td><td class="thu">12</td><td class="fri">13</td><td class="sat">14</td><td class="sun">15</td></tr>
<tr><td class="mon">16</td><td class="tue">17</td><td class="wed">18</td><td class="thu">19</td><td class="fri">20</td><td class="sat">21</td><td class="sun">22</td></tr>
<tr><td class="mon">23</td><td class="tue">24</td><td class="wed">25</td><td class="thu">26</td><td class="fri">27</td><td class="sat">28</td><td class="sun">29</td></tr>
<tr><td class="mon">30</td><td class="tue">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
</table>

cd.isleap(2020)
True
#Last Day- write a function that determines the last day of the month for a given in a given year
import calendar
def last_day(year,month):
    return calendar.monthrange(year,month)[1]

last_day(2019,6)
30
last_day(201,2)
28
last_day(2020,2)
29
#Holidays- A company has working days from Monday to Saturday, but has an off on the second and fourth Monday of each month. Write a function to determine the holidays in any year.
>>> def holidays(year):
...     for month in range(1,13):
...         cal=calendar.monthcalendar(year,month)
...         w1,w2,w3,w4,w5=cal[0],cal[1],cal[2],cal[3],cal[4]
...         if w1[calendar.MONDAY]:
...             holiday1=w2[calendar.MONDAY]
...             holiday2=w4[calendar.MONDAY]
...         else:
...             holiday1=w3[calendar.MONDAY]
...             holiday2=w5[calendar.MONDAY]
...         print(calendar.month_abbr[month],holiday1,holiday2)
... 
...         
>>> holidays(2020)
Jan 13 27
Feb 10 24
Mar 9 23
Apr 13 27
May 11 25
Jun 8 22
Jul 13 27
Aug 10 24
Sep 14 28
Oct 12 26
Nov 9 23
Dec 14 28
