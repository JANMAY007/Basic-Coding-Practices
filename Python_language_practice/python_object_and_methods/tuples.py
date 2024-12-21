names = ("hello", "hi-hi", "namaste")
print(names[1])
print(names[-1])
print(names[-2])
print(names[1:3])
print(names[:-1])
print(names[::-1])
print(names[1::])
array = list(names)
array[1] = "hi"
t = tuple(array)
print(t)
for a in names:
    print(a)
for a in array:
    print(a)
for a in t:
    print(a)
