n=int(input('enter the number of rows:'))
for i in range(n):
    print(" "*(n-i), "*"*(i*2+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i), "*"*(i*2+1))