# 14:44
# 15:09
#

from collections import deque

def gear_rotate(gear_num, direction):
    rotate_info = [0,0,0,0]
    rotate_info[gear_num] = direction
    for num in range(gear_num-1, -1, -1):
        if gear[num][2] != gear[num+1][6]:
            rotate_info[num] = rotate_info[num+1] * -1

    for num in range(gear_num+1, 4):
        if gear[num][6] != gear[num-1][2]:
            rotate_info[num] = rotate_info[num-1] * -1
    
    for num, d in enumerate(rotate_info):
        gear[num].rotate(d)

def get_score(gear):
    score = 0
    for num in range(4):
        if gear[num][0] == '1':
            score += (2 ** num)
    return score

if __name__=="__main__":
    gear = [deque(list(input())) for _ in range(4)]
    K = int(input())
    for _ in range(K):
        gear_num, direction = map(int, input().split())
        gear_rotate(gear_num-1, direction)
    print(get_score(gear))