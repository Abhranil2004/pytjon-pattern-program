# Pattern Printing Programs

This document provides several programs to print various patterns using Python.

## 1. Pattern: Descending Numbers


### Code


 Write a program to print the following pattern:
 <br>
 12345<br>
 1234<br>
 123<br>
 12<br>
 1
```
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```
Write a prohram to print the following pattern:
<br>
1<br>
21<br>
321<br>
4321<br>
54321
```
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()
```
Write a prohram to print the following pattern:
<br>
54321<br>
5432<br>
543<br>
54<br>
5
'''
```
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()
```
Write a program to print the following pattern:
<br>
54321<br>
4321<br>
321<br>
21<br>
1<br>
```
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
```
Write a program to print the following pattern:
<br>
12345<br>
2345<br>
345<br>
45<br>
5
```
for i in range(1,6):
    for j in range(i,6):     #range(start,stop,step)
        print(j,end="")
    print()
```
Write a program to print the following pattern:
<br>
*<br>
**<br>
***<br>
****<br>
*****
```
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
```
Write a program to print the following pattern:
<br>
*****<br>
****<br>
***<br>
**<br>
*
```
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()
```

Write a program to print the following pattern:
<br>
5<br>
545<br>
54345<br>
5432345<br>
543213245

```
for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j,end="")
    for j in range(5-i+2,5+1):
        print(j,end="")
    print()
```



