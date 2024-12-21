size=int(input("enter the size of pattern: "))
for i in range(65,65+size):
    for j in range(1,size+1):
        print((chr(i)),end='')
    print()