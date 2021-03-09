from copy import deepcopy
from sys import stdin

N, M, I, J, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
command = list(map(int, stdin.readline().split()))
move_dir = [[0,0],[0,1],[0,-1],[-1,0],[1,0]]
dice = [0,0,0,0,0,0]
# 위 아래 오 왼 앞 뒤

for d in command:
    if 0 <= I + move_dir[d][0] < N and 0 <= J + move_dir[d][1] < M:
        I, J = I + move_dir[d][0], J + move_dir[d][1]
        copied_dice = deepcopy(dice)
        if d == 1:
            dice[0] = copied_dice[3]
            dice[1] = copied_dice[2]
            dice[2] = copied_dice[0]
            dice[3] = copied_dice[1]
        elif d == 2:
            dice[0] = copied_dice[2]
            dice[1] = copied_dice[3]
            dice[2] = copied_dice[1]
            dice[3] = copied_dice[0]
        elif d == 3:
            dice[0] = copied_dice[4]
            dice[1] = copied_dice[5]
            dice[4] = copied_dice[1]
            dice[5] = copied_dice[0]
        elif d == 4:
            dice[0] = copied_dice[5]
            dice[1] = copied_dice[4]
            dice[4] = copied_dice[0]
            dice[5] = copied_dice[1]
        
        if board[I][J] == 0: board[I][J] = dice[1]
        else:
            dice[1] = board[I][J]
            board[I][J] = 0

        print(dice[0])
