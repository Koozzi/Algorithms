def get_direction(l):

    for i in range(1, len(l)):
        if l[i-1][2] % 2 != l[i][2] % 2:
            return [1, 3, 5, 7]
    return [0, 2, 4, 6]


def combine_fireball(current_board):
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(current_board[i][j]) > 1:
                new_m, new_s = 0, 0

                for m, s, d in current_board[i][j]:
                    new_m += m
                    new_s += s

                new_m //= 5
                new_s //= len(current_board[i][j])

                if new_m == 0:
                    continue

                for new_d in get_direction(current_board[i][j]):
                    new_board[i][j].append([new_m, new_s, new_d])
            else:
                new_board[i][j] = current_board[i][j]

    return new_board


def fireball_move(current_board):
    new_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for m, s, d in current_board[i][j]:

                next_i = (i + move[d][0] * s) % N
                next_j = (j + move[d][1] * s) % N

                new_board[next_i][next_j].append([m, s, d])

    return combine_fireball(new_board)


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(M):
    i, j, m, s, d = map(int, input().split())
    board[i-1][j-1].append([m, s, d])

for _ in range(K):
    board = fireball_move(board)

answer = 0
for i in range(N):
    for j in range(N):
        for m, s, d in board[i][j]:
            answer += m
print(answer)

