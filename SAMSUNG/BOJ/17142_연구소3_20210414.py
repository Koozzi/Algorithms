from itertools import combinations
from collections import deque


def spread_virus(virus_list):
    _safe_area_count = safe_area_count
    visit = [[False for _ in range(N)] for _ in range(N)]
    q = deque([])
    for i, j in virus_list:
        visit[i][j] = True
        q.append([i, j, 0])

    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j]:
                    if board[next_i][next_j] != 1:
                        visit[next_i][next_j] = True
                        q.append([next_i, next_j, current_d + 1])
                        if board[next_i][next_j] == 0:
                            _safe_area_count -= 1
                            if _safe_area_count == 0:
                                return current_d + 1

    return 2e9


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus_candidate = []
safe_area_count = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus_candidate.append([i, j])
        elif board[i][j] == 0:
            safe_area_count += 1

if safe_area_count == 0:
    print(0)
    exit()

answer = 2e9
for virus_list in combinations(virus_candidate, M):
    answer = min(answer, spread_virus(virus_list))

if answer == 2e9:
    print(-1)
else:
    print(answer)