numbers = list(map(int, input().split()))  # list input
print(numbers)

numbers.insert(0, 18)  # insertion
print(numbers)
print(numbers.index(5))

print(3 in numbers)  # checking
print(numbers.count(1))

numbers.sort()  # sorting
print(numbers)
numbers.reverse()
print(numbers)

unique = []  # making set
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
