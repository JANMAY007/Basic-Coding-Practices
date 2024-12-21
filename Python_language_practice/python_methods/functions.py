def main(v):
    a = v
    if a < 10:
        print("a is smaller than 10")
    elif 10 <= a <= 15:
        print("a is in between")
    else:
        print("a is stupid")


if __name__ == '__main__':
    main(5)
