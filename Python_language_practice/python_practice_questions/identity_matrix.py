n=int(input("enter the size of matrix:"))
for i in range(n):
    for j in range(n):
        if(i==j):
            print("1",sep=' ',end=' ')
        else:
            print("0",sep=' ',end=' ')
    print()