def mergesort(array_list):
    if len(array_list) > 1:
        mid = len(array_list) // 2
        left_half = array_list[:mid]
        right_half = array_list[mid:]
        mergesort(left_half)
        mergesort(right_half)
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


if __name__ == "__main__":
    array = input("enter elements:").split()
    print(mergesort(array))
