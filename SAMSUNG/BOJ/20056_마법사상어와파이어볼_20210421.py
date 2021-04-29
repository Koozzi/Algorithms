def get_next_direction(l):

    for i in range(1, len(l)):
        if l[i-1][2] % 2 != l[i][2] % 2:
            return [1, 3, 5, 7]
    return [0, 2, 4, 6]


def fireball_combine(tmp_board):
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(tmp_board[i][j]) > 1:
                new_m, new_s = 0, 0

                for _m, _s, _d in tmp_board[i][j]:
                    new_m += _m
                    new_s += _s

                new_m //= 5
                new_s //= len(tmp_board[i][j])

                if new_m == 0:
                    continue

                for new_d in get_next_direction(tmp_board[i][j]):
                    new_board[i][j].append([new_m, new_s, new_d])

            else:
                new_board[i][j] = tmp_board[i][j]

    return new_board


def fireball_move():
    tmp_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for m, s, d in board[i][j]:

                next_i = (i + move[d][0] * s) % N
                next_j = (j + move[d][1] * s) % N

                tmp_board[next_i][next_j].append([m, s, d])

    # print("after move")
    # for i in tmp_board:
    #     print(i)

    return fireball_combine(tmp_board)


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])

# for i in board:
#     print(i)

for _ in range(K):
    board = fireball_move()
    # print("after combine")
    # for i in board:
    #     print(i)

answer = 0
for i in range(N):
    for j in range(N):
        for m, s, d in board[i][j]:
            answer += m

print(answer)