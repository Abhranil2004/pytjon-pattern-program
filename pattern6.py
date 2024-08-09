for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j,end="")
    for j in range(5-i+2,5+1):
        print(j,end="")
    print()
