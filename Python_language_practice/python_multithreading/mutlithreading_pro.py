import threading
import time


def data(word1):
    with open("data.txt") as file1:
        content = file1.readlines()
        # print(content)
        for words in content:
            if word1 in words:
                print("Found")
                print(words)


def information(word2):
    with open("information.txt") as file2:
        content = file2.readlines()
        # print(content)
        for words in content:
            if word2 in words:
                print("Found")
                print(words)


if __name__ == "__main__":
    # check = input("enter the word to check in both files: ")
    check1 = "and"
    check2 = "find"
    t1 = threading.Thread(target=data, args=(check1, ))
    t2 = threading.Thread(target=data, args=(check2, ))
    """t1 = threading.Thread(target=information, args=(check1,))
    t2 = threading.Thread(target=data, args=(check2,))"""
    t1.start()
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    time.sleep(1)
    print("Done...")
"""
ip
usp
"""