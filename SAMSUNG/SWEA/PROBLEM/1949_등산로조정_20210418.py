from collections import deque


def find_road(start_i, start_j):
    depth = [[1 for _ in range(N)] for _ in range(N)]
    q = deque([[start_i, start_j]])
    max_len = 1
    while q:
        current_i, current_j = q.popleft()

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if board[next_i][next_j] < board[current_i][current_j]:
                if depth[next_i][next_j] <= depth[current_i][current_j] + 1:
                    depth[next_i][next_j] = depth[current_i][current_j] + 1
                    max_len = max(max_len, depth[next_i][next_j])
                    q.append([next_i, next_j])

    return max_len


def solve():
    max_len = 0
    for i in range(N):
        for j in range(N):
            if (i, j) in start_index:
                max_len = max(max_len, find_road(i, j))

    return max_len


def find_highest():
    height = 0
    for i in range(N):
        for j in range(N):
            height = max(height, board[i][j])

    return height


def make_start_index(height):
    s = set([])
    for i in range(N):
        for j in range(N):
            if board[i][j] == height:
                s.add((i, j))

    return s


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_height = find_highest()
    start_index = make_start_index(max_height)

    answer = 0
    for k in range(K+1):
        for i in range(N):
            for j in range(N):
                board[i][j] -= k
                answer = max(answer, solve())
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