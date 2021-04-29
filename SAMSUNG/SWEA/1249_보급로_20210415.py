"""
21:42
"""
from collections import deque


def dijkstra(start_i, start_j):
    recover_time = [[2e9 for _ in range(N)] for _ in range(N)]
    recover_time[0][0] = 0
    q = deque([[start_i, start_j]])

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if recover_time[next_i][next_j] > recover_time[current_i][current_j] + board[next_i][next_j]:
                recover_time[next_i][next_j] = recover_time[current_i][current_j] + board[next_i][next_j]
                q.append([next_i, next_j])

    return recover_time[N-1][N-1]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    print("#{}, {}".format(t, dijkstra(0, 0)))

