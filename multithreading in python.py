Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Objective- To implement multithreading using python
import threading
def double(num):
    print(f'{num}*2={num*2}\n')

    
def triple(num):
    print(f'{num}*3={num*3}')

    
def demo():
    t1=threading.Thread(target=double,args=(7,))
    t2=threading.Thread(target=triple,args=(7,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Finished")

    
demo()
7*2=14
7*3=21

Finished
threading.active_count()
2
threading.current_thread()
<_MainThread(MainThread, started 14176)>
threading.main_thread()
<_MainThread(MainThread, started 14176)>
Threading.get_ident()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Threading.get_ident()
NameError: name 'Threading' is not defined. Did you mean: 'threading'?
theading.get_ident()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    theading.get_ident()
NameError: name 'theading' is not defined. Did you mean: 'threading'?
threading.get_ident()
14176
threading.get_ident()
14176
threading.enumerate()
[<_MainThread(MainThread, started 14176)>, <Thread(SockThread, started daemon 27152)>]
>>> t1=theading.Thread(target=double,args=(7,))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t1=theading.Thread(target=double,args=(7,))
NameError: name 'theading' is not defined. Did you mean: 'threading'?
>>> t1=threading.Thread(target=double,args=(7,))
>>> t1.is_alive()
False
>>> t1.isDaemon()

Warning (from warnings module):
  File "<pyshell#29>", line 1
DeprecationWarning: isDaemon() is deprecated, get the daemon attribute instead
False
>>> from threading import Lock
>>> 1=Lock()
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> l=Lock()
>>> l
<unlocked _thread.lock object at 0x000001727FBEAD10>
>>> l.acquire()
True
>>> l
<locked _thread.lock object at 0x000001727FBEAD10>
>>> l.release()
>>> from threading import Timer
>>> def say():
...     print("Hello")
... 
...     
>>> t.Timer(2,sya)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t.Timer(2,sya)
NameError: name 't' is not defined
>>> t=Timer(2,say)
>>> t.start()
>>> Hello
