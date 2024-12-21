# for small strings you can use quotes
my_string = "hi from janmay"
print(my_string)

# adding two strings
our_string = 'hello' + 'hi'
print(our_string)

# making long string
para_string = """Namaste 
hello
hi"""
print(para_string)

# length of string
string = 'Python for the beginners'
print(len(string))

# making upper case and lower case
course = 'Python for the beginners'
print(course.upper())
print(course.lower())

# indexing element
my_string = 'Python for the beginners'
print(my_string.find('f'))
print(my_string.replace('for', 'course'))
# finding element in string
print('Python' in my_string)

# string formatting
first_name = 'Janmay'
last_name = 'Bhatt'
# message=first_name+' '+last_name+' is a businessman'
message = f'{first_name} {last_name} is a businessman'  # f''is for formatting the string
print(message)
