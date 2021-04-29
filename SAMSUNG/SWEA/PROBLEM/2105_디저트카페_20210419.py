def change_direction(X, Y, x, y, d1, d2):
    if (X == x + d1 and Y == y - d1) \
            or (X == x + d1 + d2 and Y == y - d1 + d2) \
            or (X == x + d2 and Y == y + d2):
        return True
    return False


def solve(x, y, d1, d2):
    desert = set([board[x][y]])
    move = [[1, -1], [1, 1], [-1, 1], [-1, -1]]

    X, Y, D = x, y, 0
    while True:

        if change_direction(X, Y, x, y, d1, d2):
            D += 1

        X += move[D][0]
        Y += move[D][1]

        if X == x and Y == y:
            break

        if board[X][Y] not in desert:
            desert.add(board[X][Y])
        elif board[X][Y] in desert:
            return -2

    return len(desert)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for x in range(N - 2):
        for y in range(N - 1):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if 0 <= y - d1 and x + d1 + d2 <= N - 1 and y + d2 <= N - 1:
                        answer = max(answer, solve(x, y, d1, d2))

    print("#{} {}".format(t, answer))

"""
2         
4                
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
5                
8 2 9 6 6
1 9 3 3 4
8 2 3 3 6
4 3 4 4 9
7 4 6 3 5
"""
