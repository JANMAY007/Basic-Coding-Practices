queue = []
flag = True
while bool(flag):
    option = int(input("""
    enter 1 to enqueue
    enter 2 to dequeue
    enter 3 to view size
    enter 4 to display
    enter 5 to exit
    """))
    if option == 1:
        value = input("enter the value")
        queue.append(value)
    elif option == 2:
        try:
            queue.pop(0)
        except IndexError:
            print("queue is empty")
    elif option == 3:
        print(len(queue))
    elif option == 4:
        print(queue)
    elif option == 5:
        flag = False
