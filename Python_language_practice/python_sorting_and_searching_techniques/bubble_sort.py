"""def bubble_sort(array_list):
    for j in range(len(array_list) - 1, 0, -1):
        for i in range(j):
            if array_list[i] > array_list[i + 1]:
                temp = array_list[i]
                array_list[i] = array_list[i + 1]
                array_list[i + 1] = temp
    return array_list"""


def bubble_sort(n):
    if n is None:
        n = len(array)
    if n == 1:
        return array
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    bubble_sort(n - 1)


if __name__ == "__main__":
    array = list(map(int, input().split()))
    bubble_sort(len(array))
    print(array)
