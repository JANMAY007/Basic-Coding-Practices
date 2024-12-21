size=int(input("enter the size of pattern: "))
for i in range(1,size+1):
    for j in range(65,i+65):
        print(chr(j),end='')
    print()