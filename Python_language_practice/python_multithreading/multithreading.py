from time import sleep
import threading


def cube(num):
    print("Cube: {}".format(num * num * num))


def square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    number1 = int(input("enter the number whose square is to be found out: "))
    number2 = int(input("enter the number whose cube is to be found out: "))
    t1 = threading.Thread(target=square, args=(number1, ))
    t2 = threading.Thread(target=cube, args=(number2, ))
    sleep(1)
    t1.start()
    sleep(1)
    t2.start()
    sleep(1)
    t1.join()
    t2.join()
    print("Done...")
