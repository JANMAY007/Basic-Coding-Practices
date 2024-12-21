def radix_sort(arr):
    exponent = 1
    while max(arr)/exponent > 0:
        count_sort(arr, exponent)
        exponent *= 10


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


if __name__ == "__main__":
    array = list(map(int, input().split()))
    radix_sort(array)
    print(array)
