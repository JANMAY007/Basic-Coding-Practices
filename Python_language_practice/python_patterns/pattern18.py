size=int(input("enter the size of pattern: "))
for i in range(65,size+65):
    for j in range(size+65,i,-1):
        print(chr(i),end='')
    print()