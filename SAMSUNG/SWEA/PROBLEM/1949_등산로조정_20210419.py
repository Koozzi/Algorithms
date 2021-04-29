from collections import deque


def get_highest():
    highest = 0
    for i in range(N):
        for j in range(N):
            highest = max(highest, board[i][j])
    return highest


def get_start_index(highest):
    start_index = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == highest:
                start_index.append([i, j])
    return start_index


def dijkstra(start_i, start_j):
    depth = [[0 for _ in range(N)] for _ in range(N)]
    depth[start_i][start_j] = 1
    q = deque([[start_i, start_j]])
    max_depth = 1
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if board[next_i][next_j] < board[current_i][current_j]:
                    if depth[next_i][next_j] < depth[current_i][current_j] + 1:
                        depth[next_i][next_j] = depth[current_i][current_j] + 1
                        q.append([next_i, next_j])
                        max_depth = max(max_depth, depth[next_i][next_j])

    return max_depth


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    highest = get_highest()
    start_index = get_start_index(highest)
    answer = 0

    for k in range(K + 1):
        for i in range(N):
            for j in range(N):
                board[i][j] -= k
                for si, sj in start_index:
                    answer = max(answer, dijkstra(si, sj))
                board[i][j] += k

    print("#{} {}".format(t, answer))


"""
2      
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1
"""