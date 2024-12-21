import math
number = int(input("Enter any number: "))
#if number > 1:
if number!=2 and number%2==0:
    print(number,"is not a prime")
else:
    for i in range(2, math.ceil(number**(1/2))):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
#else:
 #   print(number, "is not a prime number")
#9999999967