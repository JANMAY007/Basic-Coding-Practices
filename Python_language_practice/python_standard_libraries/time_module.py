import time


def count():
    for i in range(10000):
        pass


start = time.time()
count()
end = time.time()
duration = end - start
print(duration)
