def spread_dust():
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    new_board[cleaner_i][cleaner_j] = -1
    new_board[cleaner_i-1][cleaner_j] = -1

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                spread_dust_amount = board[i][j] // 5
                spread_count = 0
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    next_i = i + di
                    next_j = j + dj
                    if 0 <= next_i < N and 0 <= next_j < M:
                        if board[next_i][next_j] != -1:
                            spread_count += 1
                            new_board[next_i][next_j] += spread_dust_amount

                new_board[i][j] += (board[i][j] - spread_dust_amount * spread_count)

    return new_board


def air_cleaner():
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    I, J, D = cleaner_i - 2, cleaner_j, 0

    while True:
        next_i = I + move[D][0]
        next_j = J + move[D][1]

        board[I][J] = board[next_i][next_j]

        I, J = next_i, next_j

        if I == cleaner_i-1 and J == cleaner_j:
            break

        if (I == 0 and J == 0) or (I == 0 and J == M-1) or (I == cleaner_i-1 and J == M-1):
            D += 1

    board[cleaner_i-1][cleaner_j+1] = 0

    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    I, J, D = cleaner_i + 1, cleaner_j, 0

    while True:
        next_i = I + move[D][0]
        next_j = J + move[D][1]

        board[I][J] = board[next_i][next_j]

        I, J = next_i, next_j

        if I == cleaner_i and J == cleaner_j:
            break

        if (I == N-1 and J == 0) or (I == N-1 and J == M-1) or (I == cleaner_i and J == M-1):
            D += 1

    board[cleaner_i][cleaner_j+1] = 0


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 아래에 위치한 공기청정기 위치임
cleaner_i, cleaner_j = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            cleaner_i, cleaner_j = i, j

for _ in range(T):
    board = spread_dust()
    air_cleaner()

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)
