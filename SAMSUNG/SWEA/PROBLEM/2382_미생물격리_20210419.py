def get_new_direction(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3


def small_thing_move():
    tmp_board = [[[] for _ in range(N)] for _ in range(N)]
    new_board = [[[0, 0] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j][0] > 0:
                _amount, _direction = board[i][j]
                next_i = i + move[_direction][0]
                next_j = j + move[_direction][1]

                if next_i == 0 or next_i == N - 1 or next_j == 0 or next_j == N - 1:
                    _amount //= 2
                    _direction = get_new_direction(_direction)

                tmp_board[next_i][next_j].append([_amount, _direction])

    for i in range(N):
        for j in range(N):
            if len(tmp_board[i][j]) == 1:
                new_amount, new_direction = tmp_board[i][j][0]
                new_board[i][j] = [new_amount, new_direction]
            elif len(tmp_board[i][j]) > 1:
                max_amount, new_amount, new_direction = 0, 0, 0
                for a, d in tmp_board[i][j]:
                    new_amount += a
                    if a > max_amount:
                        max_amount = a
                        new_direction = d

                new_board[i][j] = [new_amount, new_direction]

    return new_board


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[[0, 0] for _ in range(N)] for _ in range(N)]
    move = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

    for _ in range(K):
        i, j, amount, direction = map(int, input().split())
        board[i][j] = [amount, direction]

    for _ in range(M):
        board = small_thing_move()

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += board[i][j][0]

    print("#{} {}".format(t, answer))


"""
1     
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
"""