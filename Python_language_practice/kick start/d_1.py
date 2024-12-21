import numpy as np

if __name__ == '__main__':
    test = int(input())
    for k in range(1, test + 1):
        array_1 = list(map(int, input().split()))
        array_2 = list(map(int, input().split()))
        array_3 = list(map(int, input().split()))
        array = [array_1, array_2, array_3]
        array = np.array(array, dtype=object)
        print(array)
        print(array.ravel())
        maximum = 0
        if abs(maximum) <= 50:
            array[1].insert(1, 51)
        elif abs(maximum) <= 1000000000:
            np.insert(array, (1, 1), 1000000001)
        print(array)
        first = (array[0][0] + array[2][2]) / 2
        second = (array[0][1] + array[2][1]) / 2
        third = (array[0][2] + array[2][0]) / 2
        fourth = (array[1][0] + array[1][2]) / 2
        fifth = (array[0][0] + array[2][0]) / 2
        sixth = (array[0][2] + array[2][2]) / 2
        seventh = (array[0][0] + array[0][2]) / 2
        eight = (array[2][0] + array[2][2]) / 2
        counter = 0
        if first == second == third == fourth:
            counter += 4
            array[1][1] = first
            print(counter)
        elif first == second == third:
            counter += 3
            array[1][1] = first
            print(counter)
        elif first == second:
            counter += 2
            array[1][1] = first
            print(counter)
        else:
            counter += 1
            array[1][1] = first
            print(counter)
        if fifth == array[1][0]:
            counter += 1
            print(counter)
        if sixth == array[1][2]:
            counter += 1
            print(counter)
        if seventh == array[0][1]:
            counter += 1
            print(counter)
        if eight == array[2][1]:
            counter += 1
            print(counter)
        print(array)
        print('Case #' + str(k) + ': ' + str(counter))
