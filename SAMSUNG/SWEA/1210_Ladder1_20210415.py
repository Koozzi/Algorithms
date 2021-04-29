"""
21:55
"""


def get_next_location(i, j, move):

    while True:
        if (move == -1 and j == 0) or (move == 1 and j == 99):
            break
        if board[i][j+move] == 0:
            break
        j += move

    return i, j


def find_start_idx(target_idx):

    i, j = 99, target_idx
    while True:

        i -= 1

        if i == 0:
            break

        left, right = j-1, j+1

        if left >= 0:
            if board[i][left] == 1:
                i, j = get_next_location(i, j, -1)
                continue

        if right <= 99:
            if board[i][right] == 1:
                i, j = get_next_location(i, j, 1)

    return j


for _ in range(10):
    t = int(input())

    board = [list(map(int, input().split())) for _ in range(100)]

    target_idx = 0
    for j in range(100):
        if board[99][j] == 2:
            target_idx = j
            break

    print("#{} {}".format(t, find_start_idx(target_idx)))