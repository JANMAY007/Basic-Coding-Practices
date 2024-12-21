size=int(input("enter the size of pattern: "))
for i in range(1,size+1):
    for j in range(size,i-1,-1):
        print('*',end='')
    print()