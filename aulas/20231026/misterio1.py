Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> misterio = []
>>> len(misterio)
0
>>> misterio[0] = 10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    misterio[0] = 10
IndexError: list assignment index out of range
>>> misterio
[]
>>> misterio = [0]
>>> misterio
[0]
>>> len(misterio)
1
>>> misterio[0] = 10
>>> misterio
[10]
>>> misterio = []
>>> misterio.append(7)
>>> misterio
[7]
>>> type(misterio[0])
<class 'int'>
>>> type(misterio)
<class 'list'>
>>> misterio.append(3.5)
>>> misterio
[7, 3.5]
>>> misterio.append("IFPB")
>>> misterio
[7, 3.5, 'IFPB']
>>> misterio.append(True)
>>> misterio
[7, 3.5, 'IFPB', True]
>>> type(misterio[3])
<class 'bool'>
>>> type(misterio)
<class 'list'>
>>> misterio.append([1,2,3,4])
>>> misterio
[7, 3.5, 'IFPB', True, [1, 2, 3, 4]]
>>> misterio[4][0]
1
>>> type(misterio[4][0])
<class 'int'>
>>> type(misterio[4])
<class 'list'>
>>> misterio[4].append(5)
>>> misterio
[7, 3.5, 'IFPB', True, [1, 2, 3, 4, 5]]
>>> len(misterio[4])
5
>>> 