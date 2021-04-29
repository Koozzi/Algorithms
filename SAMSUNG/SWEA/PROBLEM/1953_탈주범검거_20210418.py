"""
북 = [1, 1, 0, 0, 1, 1, 0]
동 = [1, 0, 1, 0, 0, 1, 1]
남 = [1, 1, 0, 1, 0, 0, 1]
서 = [1, 0, 1, 1, 1, 0, 0]
영 = [0, 0, 0, 0, 0, 0, 0]
"""
pipe_connected = [[],
    [[1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 0]],
    [[1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0]],
    [[1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 0]],
    [[1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0]],
]

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

next_location_index = [[],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0]
]


from collections import deque


def solve():
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    escape_count = 1
    while q:
        current_i, current_j, current_d = q.popleft()

        if current_d == time-1:
            return escape_count

        current_pipe = board[current_i][current_j]
        for d in next_location_index[current_pipe]:
            next_i = current_i + move[d][0]
            next_j = current_j + move[d][1]

            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and board[next_i][next_j] > 0:
                    next_pipe = board[next_i][next_j]
                    if pipe_connected[current_pipe][d][next_pipe-1]:
                        visit[next_i][next_j] = True
                        q.append([next_i, next_j, current_d + 1])
                        escape_count += 1

    return escape_count


T = int(input())
for t in range(1, T+1):
    N, M, start_i, start_j, time = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    if board[start_i][start_j] == 0:
        print("#{} {}".format(t, 1))
        continue

    print("#{} {}".format(t, solve()))

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