"""def insertion_sort(array_list):
    for i in range(1, len(array_list)):
        current_value = array_list[i]
        position = i
        while position > 0 and array_list[position - 1] > current_value:
            array_list[position] = array_list[position - 1]
            position -= 1
        array_list[position] = current_value"""


def insertion_sort(array_list, n):
    if n <= 1:
        return
    insertion_sort(array_list, n - 1)
    current_value = array_list[n - 1]
    position = n - 2
    while position >= 0 and array_list[position] > current_value:
        array_list[position + 1] = array_list[position]
        position = position - 1
    array_list[position + 1] = current_value


if __name__ == "__main__":
    array = list(map(int, input().split()))
    insertion_sort(array, len(array))
    print(array)
