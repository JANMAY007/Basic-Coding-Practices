def permutate(a,b):
    if len(a)==1:
        print(a)
    elif len(a)==2:
        print("%s%s"%(b,a))
        if(a[0]!=a[1]):
            c=a[::-1]
            print("%s%s"%(b,c))
    else:
        e=""    
        for i in range(len(a)):
            z=int(0)
            d=""
            e=b+a[i]
            y=int(0)      
        for j in range(0,i):
            if a[j]==a[i]:
                z=z+1
        if(z==0):
            for k in range(len(a)):
                if(i!=k):
                    d=d+a[k]
                    y=y+1
        permutate(d,e)

a=input("Enter a string:")
b=""
print("\nAll the ways of permutations are:")
permutate(a,b)