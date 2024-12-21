size=int(input("enter the size of pattern: "))
for i in range(size+1,1,-1):
    for j in range(65,i+64):
        print(chr(j),end='')
    print()