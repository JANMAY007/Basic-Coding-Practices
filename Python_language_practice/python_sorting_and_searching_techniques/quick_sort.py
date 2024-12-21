def partition(array, low, high):
    k = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            k = k + 1
            array[k], array[j] = array[j], array[k]
    array[k + 1], array[high] = array[high], array[k + 1]
    return k + 1


def quick_sort(array_list, low, high):
    if low < high:
        pi = partition(array_list, low, high)
        quick_sort(array_list, low, pi - 1)
        quick_sort(array_list, pi + 1, high)


if __name__ == "__main__":
    arr = list(map(int, input("enter elements: ").split()))
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
