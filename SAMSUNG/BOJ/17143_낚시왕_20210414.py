def get_nearest_shark(j):
    global answer

    for i in range(N):
        if board[i][j] != [0, 0, 0]:
            answer += board[i][j][2]
            board[i][j] = [0, 0, 0]
            return


def shark_move():
    new_board = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != [0, 0, 0]:
                s, d, z = board[i][j]
                I, J = i, j

                for _ in range(s):
                    if d == 1 or d == 2:
                        if I == N-1: d = 1
                        elif I == 0: d = 2
                    elif d == 3 or d == 4:
                        if J == M-1: d = 4
                        elif J == 0: d = 3
                    I += move[d][0]
                    J += move[d][1]

                if new_board[I][J][2] < z:
                    new_board[I][J] = [s, d, z]

    return new_board


N, M, K = map(int, input().split())
board = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]
move = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]

for _ in range(K):
    I, J, S, D, Z = map(int, input().split())

    if D == 1 or D == 2:
        S %= (N-1)*2
    elif D == 3 or D == 4:
        S %= (M-1)*2

    board[I-1][J-1] = [S, D, Z]

answer = 0
for j in range(M):
    get_nearest_shark(j)
    board = shark_move()

print(answer)
