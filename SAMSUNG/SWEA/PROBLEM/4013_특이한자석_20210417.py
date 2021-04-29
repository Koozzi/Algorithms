from collections import deque


T = int(input())
for t in range(1, T+1):
    K = int(input())
    gear = [deque(list(map(int, input().split()))) for _ in range(4)]

    for _ in range(K):
        num, direction = map(int, input().split())
        num -= 1
        rotate_info = [0, 0, 0, 0]
        rotate_info[num] = direction

        for idx in range(num-1, -1, -1):
            if gear[idx][2] == gear[idx+1][6]:
                break
            rotate_info[idx] = -rotate_info[idx+1]

        for idx in range(num+1, 4):
            if gear[idx][6] == gear[idx-1][2]:
                break
            rotate_info[idx] = -rotate_info[idx-1]

        for _num, direction in enumerate(rotate_info):
            gear[_num].rotate(direction)

    answer = 0
    new_score = 1
    for num in range(4):
        answer += gear[num][0] * new_score
        new_score *= 2

    print("#{} {}".format(t, answer))
