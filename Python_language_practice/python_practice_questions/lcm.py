a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a < b:
    minimum = b
else:
    minimum = a
while 1:
    if minimum % a == 0 and minimum % b == 0:
        print("L.C.M =", min)
        break
    min += 1
