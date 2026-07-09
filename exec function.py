Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> code='num1,num2=7,8;print(f"{num1}+{num2}={num1+num2}")'
>>> exec(code)
7+8=15
>>> code=input('What shall we do today?')
What shall we do today?for num in range(6): print(num,num**2,num**3)
>>> exec(code)
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
>>> exec('{num:num**3 for num in range(6)}')
>>> eval('{num:num**3 for num in range(6)}')
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
>>> import os
>>> code=input('What shall we do today?')
What shall we do today?print(os.listdir())
>>> exec(code)
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python.pdb', 'python3.13t.exe', 'python3.13t.pdb', 'python3.13t_d.exe', 'python3.13t_d.pdb', 'python3.dll', 'python313.dll', 'python313.pdb', 'python313t.dll', 'python313t.pdb', 'python313t_d.dll', 'python313t_d.pdb', 'python313_d.dll', 'python313_d.pdb', 'python3t.dll', 'python3t_d.dll', 'python3_d.dll', 'pythonw.exe', 'pythonw.pdb', 'pythonw3.13t.exe', 'pythonw3.13t.pdb', 'pythonw3.13t_d.exe', 'pythonw3.13t_d.pdb', 'pythonw_d.exe', 'pythonw_d.pdb', 'python_d.exe', 'python_d.pdb', 'Scripts', 'share', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> exec('print(dir())',{'built':__builtins__},{'sum':sum,'iter':iter})
['iter', 'sum']
