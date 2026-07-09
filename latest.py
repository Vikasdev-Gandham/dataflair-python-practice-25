Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
msg="Hello, world"
arr=bytes(msg,'utf-8')
arr
b'Hello, world'
>>> bytes(7)
b'\x00\x00\x00\x00\x00\x00\x00'
>>> bytes([7,2,3,5])
b'\x07\x02\x03\x05'
>>> bytes.fromhex('FFFF F21E        ')
b'\xff\xff\xf2\x1e'
>>> b'\xff\xff\xf2\xle'.hex()
SyntaxError: (value error) invalid \x escape at position 12
>>> b'\xff\xff\xf2\xle'.hex()
SyntaxError: (value error) invalid \x escape at position 12
>>> msg='Hello, World'
>>> bytearray(msg,'utf-8')
bytearray(b'Hello, World')
>>> bytearray(7)
bytearray(b'\x00\x00\x00\x00\x00\x00\x00')
>>> bytearray([7,2,3,5])
bytearray(b'\x07\x02\x03\x05')
>>> arr=bytearray([7,2,3,5])
>>> arr.append(6)
>>> arr
bytearray(b'\x07\x02\x03\x05\x06')
>>> b'\x04\x01\x03\x02\x01\x03'.count(b'\x01\x03')
2
>>> b'\x04\x01\x03\x02\x01\x03'.partition(b'\x03')
(b'\x04\x01', b'\x03', b'\x02\x01\x03')
>>> bytearray(b'Hello, world').upper()
bytearray(b'HELLO, WORLD')
>>> msg=bytearray('Hello, world','utf-8')
>>> mv=memoryview(msg)
>>> mv[1]
101
>>> list(mv[1:3])
[101, 108]
>>> mv[1]=65
>>> msg
bytearray(b'HAllo, world')
>>> mv.tolist()
[72, 65, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]
