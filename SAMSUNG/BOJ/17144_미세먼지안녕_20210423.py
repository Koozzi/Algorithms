from copy import deepcopy


def spread_dust(current_board):
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    new_board[cleaner_i][cleaner_j] = -1
    new_board[cleaner_i-1][cleaner_j] = -1

    for i in range(N):
        for j in range(M):
            if current_board[i][j] > 0:

                init_dust = current_board[i][j]
                spread_dust_amount = init_dust // 5
                spread_cnt = 0

                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    next_i = i + di
                    next_j = j + dj
                    if 0 <= next_i < N and 0 <= next_j < M:
                        if new_board[next_i][next_j] != -1:
                            new_board[next_i][next_j] += spread_dust_amount
                            spread_cnt += 1

                new_board[i][j] += init_dust - spread_dust_amount * spread_cnt

    return new_board


def change_direction(i, j):
    if (i == 0 and j == 0)\
        or (i == 0 and j == M-1)\
        or (i == cleaner_i-1 and j == M-1)\
        or (i == N-1 and j == 0)\
        or (i == N-1 and j == M-1)\
        or (i == cleaner_i and j == M-1):
        return True
    return False


def air_cleaner(current_board):
    new_board = deepcopy(current_board)

    move_top = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    i, j, d = cleaner_i - 2, cleaner_j, 0
    while True:
        if change_direction(i, j):
            d += 1
        next_i = i + move_top[d][0]
        next_j = j + move_top[d][1]

        if next_i == cleaner_i - 1 and next_j == cleaner_j:
            break

        new_board[i][j] = board[next_i][next_j]
        i, j = next_i, next_j
    new_board[cleaner_i-1][1] = 0

    move_down = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    i, j, d = cleaner_i + 1, cleaner_j, 0
    while True:
        if change_direction(i, j):
            d += 1

        next_i = i + move_down[d][0]
        next_j = j + move_down[d][1]

        if next_i == cleaner_i and next_j == cleaner_j:
            break

        new_board[i][j] = board[next_i][next_j]
        i, j = next_i, next_j
    new_board[cleaner_i][1] = 0

    return new_board


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cleaner_i, cleaner_j = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            cleaner_i = i
            cleaner_j = j

for _ in range(T):

    board = spread_dust(board)

    # print("After spread dust")
    # for b in board:
    #     print(b)
    # print()

    board = air_cleaner(board)

    # print("After air cleaner")
    # for b in board:
    #     print(b)

answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)