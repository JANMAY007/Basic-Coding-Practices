numbers = [1, 2, 3, 4, 5]
first, *others, last = numbers  # list unpacking
print(first)
print(others)
print(last)

letters = ['a', 'b', 'c']
# for letter in letters:
for letter in enumerate(letters):
    print(letter)
