from collections import deque
from scipy import spatial
import numpy as np
import sys


row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


def shortest_distance():
    return True


def complete_task(mount, work, array):
    for point in mount:
        index = array.__index__(point)
    return True


if __name__ == '__main__':
    input_files = [
        'a_example',
        'b_single_arm',
        'c_few_arms',
        'd_tight_schedule',
        'e_dense_workspace',
        'f_decentralized'
    ]
    """for input_file in input_files:
        print(input_file)"""
    with open('a_example' + '.txt') as file:
        W, H, R, M, T, L = file.readline().split()
        W, H, R, M, T, L = int(W), int(H), int(R), int(M), int(T), int(L)
        mount_points = []
        for _ in range(M):
            mount_points.append(tuple(file.readline().split()))
        mount_points = np.array(mount_points)
        # print(mount_points)
        work_space = np.zeros((W, H), dtype=int)
        # print(work_space)
        score_points = []
        task = []
        for _ in range(T):
            score_points.append(tuple(file.readline().split()))
            task.append(file.readline().split())
        # print(score_points)
        # print(task)
        tasks = []
        for elem in task:
            for i in range(0, len(elem) - 1, 2):
                tasks.append((elem[i], elem[i + 1]))
        task = set(tasks)
        # print(task)
        sys.stdout.write("\rSolving...\n")
        for x, y in mount_points:
            work_space[int(x)][int(y)] = 1
        for x, y in task:
            work_space[int(x)][int(y)] = 2
        # print(work_space)
        answer = complete_task(mount_points, task,  work_space)
