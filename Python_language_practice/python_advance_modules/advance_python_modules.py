# random module package
from datetime import date
import random
import re
import timeit

members = ["test", "hero", "rock", "singer"]

for i in range(3):
    print(random.randint(10, 20))

print(random.choice(members))

# datetime module package
today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)


# timing the code
def my_func():
    y = 3.14159
    for j in range(100):
        y = y ** 0.7
    return y


print(timeit.timeit(my_func, number=100000))

# regular expression

bar = "Hindustan is the best!"
a1 = re.search("^Hindustan.*best!$", bar)
a2 = re.findall("Hindustan", bar)
a3 = re.split("\\s", bar)
a4 = re.sub("\\s", "@", bar)

if a1:
    print("matched")
else:
    print("not matched")

print(a2)
print(a3)
print(a4)
