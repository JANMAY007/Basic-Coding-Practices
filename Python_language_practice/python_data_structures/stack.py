stack = []
flag = True
while bool(flag):
    option = int(input("""
    enter 1 to push
    enter 2 to pop
    enter 3 to view size
    enter 4 to view stack
    enter 5 to exit
    """))
    if option == 1:
        value = input("enter value: ")
        stack.append(value)
    elif option == 2:
        try:
            stack.pop()
        except IndexError:
            print("stack is empty")
    elif option == 3:
        print(len(stack))
    elif option == 4:
        print(stack)
    elif option == 5:
        flag = False
