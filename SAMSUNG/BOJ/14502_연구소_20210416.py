from itertools import combinations
from copy import deepcopy
from collections import deque


def spread_virus():
    visit = [[False for _ in range(M)] for _ in range(N)]
    q = deque([])

    for i, j in virus:
        q.append([i, j])

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] == 0:
                visit[next_i][next_j] = True
                q.append([next_i, next_j])

    safe_area = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and not visit[i][j]:
                safe_area += 1

    return safe_area


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

virus = []
wall_candidate = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            wall_candidate.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

answer = 0
for walls in combinations(wall_candidate, 3):

    for i, j in walls:
        board[i][j] = 1

    answer = max(answer, spread_virus())

    for i, j in walls:
        board[i][j] = 0

print(answer)
