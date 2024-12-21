def bubble_sort(array_list):
    for j in range(len(array_list) - 1, 0, -1):
        for i in range(j):
            if array_list[i] > array_list[i + 1]:
                temp = array_list[i]
                array_list[i] = array_list[i + 1]
                array_list[i + 1] = temp
    return array_list


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


def counting_sort(array_list, max_value):
    m = max_value + 1
    count = [0] * m
    for a in array_list:
        count[a] += 1
        i = 0
        for b in range(m):
            for c in range(count[b]):
                array_list[i] = b
                i += 1
    return array_list


def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and arr[i] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def heap_sort(arr):
    size = len(arr)
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def insertion_sort(array_list):
    for i in range(1, len(array_list)):
        current_value = array_list[i]
        position = i
        while position > 0 and array_list[position - 1] > current_value:
            array_list[position] = array_list[position - 1]
            position -= 1
        array_list[position] = current_value


def merge_sort(array_list):
    if len(array_list) > 1:
        mid = len(array_list) // 2
        left_half = array_list[:mid]
        right_half = array_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_list[k] = left_half[i]
                i = i + 1
            else:
                array_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            array_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array_list[k] = right_half[j]
            j += 1
            k += 1
    return array_list


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


def radix_sort(arr):
    exponent = 1
    while max(arr)/exponent > 0:
        count_sort(arr, exponent)
        exponent *= 10
    return arr


def count_sort(arr, exponent):
    output = [0] * (len(arr))
    count = [0] * 10
    for i in range(0, len(arr)):
        index = (arr[i] / exponent)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(arr) - 1
    while i >= 0:
        index = (arr[i] / exponent)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]


def selection_sort(array_list):
    for j in range(len(array_list) - 1, 0, -1):
        k = 0
        for i in range(1, j + 1):
            if array_list[i] > array_list[k]:
                k = i
            temp = array_list[j]
            array_list[j] = array_list[k]
            array_list[k] = temp
    return array_list


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
