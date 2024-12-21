"""def selection_sort(array_list):
    for j in range(len(array_list) - 1, 0, -1):
        k = 0
        for i in range(1, j + 1):
            if array_list[i] > array_list[k]:
                k = i
            array_list[j], array_list[k] = array_list[j], array_list[k]
    return array_list"""


def min_index(a, i, j):
    if i == j:
        return i
    k = min_index(a, i + 1, j)
    return i if a[i] < a[k] else k


def selection_sort(a, n, index=0):
    if index == n:
        return
    k = min_index(a, index, n - 1)
    if k != index:
        a[k], a[index] = a[index], a[k]
    selection_sort(a, n, index + 1)


if __name__ == "__main__":
    array = list(map(int, input().split()))
    selection_sort(array, len(array))
    print(array)
