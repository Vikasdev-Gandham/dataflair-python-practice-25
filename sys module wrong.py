Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sys
sys.version
'3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]'
sys.version_info
sys.version_info(major=3, minor=13, micro=1, releaselevel='final', serial=0)
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', '_is_interned', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_vpath', '_xoptions', 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
x=42
x
42
print(x)
42
def show(x):
    print("Outpit:",x)

    
sys.displayhook = show
x
Outpit: 42
print(x)
42
Outpit: None
print("Type in value: ",sys.stdin.readline()[:-1])
23
Type in value:  23
Outpit: None
sys.stdout.write('Way to write')
Way to writeOutpit: 12
import math
sys.modules
Outpit: 
sys.path
Outpit: ['', 'C:\\Program Files\\Python313\\Lib\\idlelib', 'C:\\Program Files\\Python313\\python313.zip', 'C:\\Program Files\\Python313\\DLLs', 'C:\\Program Files\\Python313\\Lib', 'C:\\Program Files\\Python313', 'C:\\Program Files\\Python313\\Lib\\site-packages', 'C:\\Program Files\\Python313\\Lib\\site-packages\\win32', 'C:\\Program Files\\Python313\\Lib\\site-packages\\win32\\lib', 'C:\\Program Files\\Python313\\Lib\\site-packages\\Pythonwin']
sys.path.append('c:\\Users\\Admin\\desktop')
Outpit: None
for num in range(100):
    print(num)
    if num==5: sys.exit()

    
0
Outpit: None
1
Outpit: None
2
Outpit: None
3
Outpit: None
4
Outpit: None
5
Outpit: None
saveout = sys.stdout
fsock=open('out.log','w')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fsock=open('out.log','w')
PermissionError: [Errno 13] Permission denied: 'out.log'
saveout = sys.stdout
fsock=open('out.log','w')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    fsock=open('out.log','w')
PermissionError: [Errno 13] Permission denied: 'out.log'
sys.stdout=fsock
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sys.stdout=fsock
NameError: name 'fsock' is not defined
print('Message to log')
Message to log
Outpit: None
import time
for num in range(10):
    print(num)
    sys.stdout.flush()
    time.sleep(1)

    
0
Outpit: None
Outpit: None
Outpit: None
1
Outpit: None
Outpit: None
Outpit: None
2
Outpit: None
Outpit: None
Outpit: None
3
Outpit: None
Outpit: None
Outpit: None
4
Outpit: None
Outpit: None
Outpit: None
5
Outpit: None
Outpit: None
Outpit: None
6
Outpit: None
Outpit: None
Outpit: None
7
Outpit: None
Outpit: None
Outpit: None
8
Outpit: None
Outpit: None
Outpit: None
9
Outpit: None
Outpit: None
Outpit: None
