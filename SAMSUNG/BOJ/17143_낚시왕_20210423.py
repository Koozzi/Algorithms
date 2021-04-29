def get_nearest_shark(j):
    global answer

    for i in range(N):
        if board[i][j] != [0, 0, 0]:
            answer += board[i][j][2]
            board[i][j] = [0, 0, 0]
            break


def shark_move():
    new_board = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != [0, 0, 0]:
                speed, direction, size = board[i][j]

                next_i, next_j = i, j
                for _ in range(speed):
                    if direction == 1 or direction == 2:
                        if next_i == 0: direction = 2
                        elif next_i == N-1: direction = 1

                    elif direction == 3 or direction == 4:
                        if next_j == 0: direction = 3
                        elif next_j == M-1: direction = 4

                    next_i += move[direction][0]
                    next_j += move[direction][1]

                if new_board[next_i][next_j][2] < size:
                    new_board[next_i][next_j] = [speed, direction, size]

    return new_board


N, M, K = map(int, input().split())
board = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]
move = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
answer = 0

for _i in range(K):
    i, j, s, d, z = map(int, input().split())
    if d == 1 or d == 2: s %= (N-1)*2
    elif d == 3 or d == 4: s %= (M-1)*2
    board[i-1][j-1] = [s, d, z]

for j in range(M):
    get_nearest_shark(j)

    # print("After getting nearest shark")
    # for b in board:
    #     print(b)
    # print()

    board = shark_move()
    # print("After shark move")
    # for b in board:
    #     print(b)
    # print()

print(answer)