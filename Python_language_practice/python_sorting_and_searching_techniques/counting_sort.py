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


if __name__ == "__main__":
    array1 = list(map(int, input("enter elements: ").split()))
    max_val = max(array1)  # int(input("enter max value: "))
    print(counting_sort(array1, max_val))
