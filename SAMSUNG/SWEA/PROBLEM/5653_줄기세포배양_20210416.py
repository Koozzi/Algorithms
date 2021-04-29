"""
19:47
20:23 (제출)
"""

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    init_board = [list(map(int, input().split())) for _ in range(N)]
    board = [[[0, 0] for _ in range(K + M)] for _ in range(K + N)]

    # empty, inactive, active, dead
    state = [['empty' for _ in range(K + M)] for _ in range(K + N)]

    for i in range(N):
        for j in range(M):
            board[i+K//2][j+K//2] = [init_board[i][j], init_board[i][j]]
            if init_board[i][j] > 0:
                state[i+K//2][j+K//2] = 'inactive'

    for k in range(1, K+1):

        new_cell = []
        for i in range(K+N):
            for j in range(K+M):
                init_age, current_age = board[i][j]

                if state[i][j] == 'inactive':
                    board[i][j][1] -= 1
                    if board[i][j][1] == 0:
                        state[i][j] = 'active'
                        board[i][j][1] = board[i][j][0]

                elif state[i][j] == 'active':
                    board[i][j][1] -= 1
                    if board[i][j][1] == 0:
                        state[i][j] = 'dead'

                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i = i + di
                        next_j = j + dj

                        if state[next_i][next_j] == 'empty':
                            new_cell.append([next_i, next_j])
                            if init_age > board[next_i][next_j][0]:
                                board[next_i][next_j] = [init_age, init_age]

        for ci, cj in new_cell:
            state[ci][cj] = 'inactive'

    answer = 0
    for i in range(K + N):
        for j in range(K + M):
            if state[i][j] == 'inactive' or state[i][j] == 'active':
                answer += 1

    print("#{} {}".format(t, answer))