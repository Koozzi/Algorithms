from copy import deepcopy
from itertools import combinations
from collections import deque


def spread_virus(new_board):
    visit = [[False for _ in range(M)] for _ in range(N)]
    q = deque([])

    safe_count = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 2:
                visit[i][j] = True
                q.append([i, j])
            elif new_board[i][j] == 0:
                safe_count += 1

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue

            if not visit[next_i][next_j] and new_board[next_i][next_j] == 0:
                visit[next_i][next_j] = True
                q.append([next_i, next_j])
                new_board[next_i][next_j] = 2
                safe_count -= 1

    return safe_count


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

wall_candidate = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            wall_candidate.append([i, j])

answer = 0
for walls in combinations(wall_candidate, 3):
    new_board = deepcopy(board)

    for I, J in walls:
        new_board[I][J] = 1

    answer = max(answer, spread_virus(new_board))

print(answer)