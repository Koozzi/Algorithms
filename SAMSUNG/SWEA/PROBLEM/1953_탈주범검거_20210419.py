pipe_connected = [[],
    [[0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 1, 0, 0]],
    [[0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0]],
    [[0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 1, 0, 0]],
    [[0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0]],
]
# north = [0, 1, 1, 0, 0, 1, 1, 0]
# south = [0, 1, 1, 0, 1, 0, 0, 1]
# west  = [0, 1, 0, 1, 1, 1, 0, 0]
# east  = [0, 1, 0, 1, 0, 0, 1, 1]
# impos = [0, 0, 0, 0, 0, 0, 0, 0]

from collections import deque


def escape():
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[I][J] = 1
    q = deque([[I, J, 0]])
    escape_count = 1
    while q:
        current_i, current_j, current_d = q.popleft()

        if current_d == K - 1:
            return escape_count

        current_type = board[current_i][current_j]
        for d in range(4):
            next_i = current_i + move[d][0]
            next_j = current_j + move[d][1]
            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and board[next_i][next_j] > 0:
                    if pipe_connected[current_type][d][board[next_i][next_j]]:
                        visit[next_i][next_j] = 1
                        q.append([next_i, next_j, current_d + 1])
                        escape_count += 1

    # print(t)
    # for v in visit:
    #     print(v)

    return escape_count


T = int(input())
for t in range(1, T+1):
    N, M, I, J, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    print("#{} {}".format(t, escape()))

"""
2        
5 6 2 1 3      
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
5 6 2 2 6      
3 0 0 0 0 3
2 0 0 0 0 6
1 3 1 1 3 1
2 0 2 0 0 2
0 0 4 3 1 1
"""