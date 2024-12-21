def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            return i
    return -1


if __name__ == "__main__":
    array = list(map(int, input().split()))
    check = int(input())
    result = linear_search(array, check)
    if result != -1:
        print(str(check), "is present at index", str(result))
    else:
        print(str(check), "is not present in the array")
