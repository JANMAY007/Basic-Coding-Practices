def binary_search_recursive(arr, low, high, search):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] > search:
            return binary_search_recursive(arr, low, mid - 1, search)
        else:
            return binary_search_recursive(arr, mid + 1, high, search)
    else:
        return -1


def binary_search_iterative(arr, search):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < search:
            low = mid + 1
        elif arr[mid] > search:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    array = list(map(int, input().split()))
    check = int(input())
    result = binary_search_recursive(array, 0, len(array) - 1, check)
    if result != -1:
        print(str(check), "is present at index", str(result))
    else:
        print(str(check), "is not present in the array")
