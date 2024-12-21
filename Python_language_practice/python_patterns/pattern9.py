size=int(input("enter the size of pattern: "))
for i in range(size+1,1,-1):
    for j in range(64+size,64,-1):
        print((chr(j)),end='')
    print()