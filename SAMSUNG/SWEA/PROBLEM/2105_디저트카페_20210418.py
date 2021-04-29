def solve(x, y, d1, d2):

    desert = set([])

    _x, _y = x, y
    for _ in range(d1):
        _x += 1
        _y -= 1
        if board[_x][_y] in desert:
            return -2
        desert.add(board[_x][_y])

    _x, _y = x + d1, y - d1
    for _ in range(d2):
        _x += 1
        _y += 1
        if board[_x][_y] in desert:
            return -2
        desert.add(board[_x][_y])

    _x, _y = x + d1 + d2, y - d1 + d2
    for _ in range(d1):
        _x -= 1
        _y += 1
        if board[_x][_y] in desert:
            return -2
        desert.add(board[_x][_y])

    _x, _y = x + d2, y + d2
    for _ in range(d2):
        _x -= 1
        _y -= 1
        if board[_x][_y] in desert:
            return -2
        desert.add(board[_x][_y])

    return len(desert)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    for x in range(N-2):
        for y in range(1, N-1):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if y + d2 <= N - 1 and x + d1 + d2 <= N - 1 and y - d1 >= 0:
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