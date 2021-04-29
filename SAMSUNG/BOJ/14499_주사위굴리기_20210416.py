from copy import deepcopy


def change_dice(d):
    new_dice = deepcopy(dice)

    if d == 1:
        new_dice[3] = dice[0]
        new_dice[0] = dice[2]
        new_dice[2] = dice[1]
        new_dice[1] = dice[3]

    elif d == 2:
        new_dice[2] = dice[0]
        new_dice[0] = dice[3]
        new_dice[3] = dice[1]
        new_dice[1] = dice[2]

    elif d == 3:
        new_dice[5] = dice[0]
        new_dice[0] = dice[4]
        new_dice[4] = dice[1]
        new_dice[1] = dice[5]

    elif d == 4:
        new_dice[4] = dice[0]
        new_dice[0] = dice[5]
        new_dice[5] = dice[1]
        new_dice[1] = dice[4]

    return new_dice


N, M, I, J, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [0, 0, 0, 0, 0, 0]

for d in command:

    if not 0 <= I + move[d][0] < N or not 0 <= J + move[d][1] < M:
        continue

    I += move[d][0]
    J += move[d][1]

    dice = change_dice(d)

    if board[I][J] == 0:
        board[I][J] = dice[1]
    else:
        dice[1] = board[I][J]
        board[I][J] = 0

    print(dice[0])