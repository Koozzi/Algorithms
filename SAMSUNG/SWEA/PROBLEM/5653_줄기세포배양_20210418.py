T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    input_board = [list(map(int, input().split())) for _ in range(N)]
    board = [[['.', 0, 0] for _ in range(M + K)] for _ in range(N + K)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for i in range(N):
        for j in range(M):
            if input_board[i][j] > 0:
                board[i + K // 2][j + K // 2] = ['i', input_board[i][j], input_board[i][j]]

    for _ in range(K):

        new_cell = []
        for i in range(N + K):
            for j in range(M + K):
                if board[i][j][0] == 'i':
                    board[i][j][1] -= 1
                    if board[i][j][1] == 0:
                        board[i][j] = ['a', board[i][j][2], board[i][j][2]]

                elif board[i][j][0] == 'a':
                    for di, dj in move:
                        next_i = i + di
                        next_j = j + dj

                        if 0 <= next_i < N + K and 0 <= next_j < M + K:
                            if board[next_i][next_j][0] == '.':
                                new_cell.append([next_i, next_j, board[i][j][2]])

                    board[i][j][1] -= 1
                    if board[i][j][1] == 0:
                        board[i][j][0] = 'd'

        for i, j, age in new_cell:
            if board[i][j][2] < age:
                board[i][j] = ['i', age, age]

    answer = 0
    for i in range(N + K):
        for j in range(M + K):
            if board[i][j][0] == 'i' or board[i][j][0] == 'a':
                answer += 1

    print("#{} {}".format(t, answer))