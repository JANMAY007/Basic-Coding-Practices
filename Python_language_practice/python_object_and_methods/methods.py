# If the argument passed is in function then the whole is called as method
# first argument should be self if class is been used
def method(name):
    print(f'Hi {name} !')
    print("Welcome here!!")


first_name = input()
method(first_name)
