from collections import deque


gear = [deque(list(input())) for _ in range(4)]

K = int(input())
for _ in range(K):
    gear_num, d = map(int, input().split())
    gear_num -= 1
    rotate_info = [0, 0, 0, 0]
    rotate_info[gear_num] = d

    for num in range(gear_num-1, -1, -1):
        if gear[num][2] != gear[num+1][6]:
            rotate_info[num] = -rotate_info[num+1]

    for num in range(gear_num+1, 4):
        if gear[num][6] != gear[num-1][2]:
            rotate_info[num] = -rotate_info[num-1]

    for num, D in enumerate(rotate_info):
        gear[num].rotate(D)

answer = 0
score = 1
for num in range(4):
    if gear[num][0] == '1':
        answer += score
    score *= 2
print(answer)
