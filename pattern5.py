'''Write a program to print the following pattern:
12345
2345
345
45
5
'''

for i in range(1,6):
    for j in range(i,6):     #range(start,stop,step)
        print(j,end="")
    print()
