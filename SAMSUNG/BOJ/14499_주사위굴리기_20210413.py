
"""
dice[0] = 위
dice[1] = 뒤
dice[2] = 오
dice[3] = 왼
dice[4] = 앞
dice[5] = 밑
"""
from copy import deepcopy


def change_dice_state(D):
    new_dice = deepcopy(dice)

    if D == 1:      # 동쪽
        new_dice[2] = dice[0]
        new_dice[0] = dice[3]
        new_dice[3] = dice[5]
        new_dice[5] = dice[2]
    elif D == 2:    # 서쪽
        new_dice[3] = dice[0]
        new_dice[0] = dice[2]
        new_dice[2] = dice[5]
        new_dice[5] = dice[3]
    elif D == 3:    # 북쪽
        new_dice[1] = dice[0]
        new_dice[0] = dice[4]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1]
    elif D == 4:    # 남쪽
        new_dice[4] = dice[0]
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[5] = dice[4]

    return new_dice


dice = [0, 0, 0, 0, 0, 0]
N, M, I, J, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]

commands = list(map(int, input().split()))
for D in commands:

    I += move[D][0]
    J += move[D][1]

    if not 0 <= I < N or not 0 <= J < M:
        I -= move[D][0]
        J -= move[D][1]
        continue

    dice = change_dice_state(D)

    if board[I][J] == 0:
        board[I][J] = dice[5]
    elif board[I][J] != 0:
        dice[5] = board[I][J]
        board[I][J] = 0

    print(dice[0])

