from itertools import combinations
from collections import deque


def spread_virus(selected_virus):
    visit = [[False for _ in range(N)] for _ in range(N)]
    q = deque([])
    for i, j in selected_virus:
        visit[i][j] = True
        q.append([i, j, 0])

    count = 0

    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j] and board[next_i][next_j] != 1:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j, current_d + 1])
                    if board[next_i][next_j] == 0:
                        count += 1
                        if count == safe_count:
                            return current_d + 1

    return 2e9


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

init_virus = []
safe_count = 0
answer = 2e9

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            safe_count += 1
        elif board[i][j] == 2:
            init_virus.append([i, j])

if safe_count == 0:
    print(0)
    exit()

for selected_virus in combinations(init_virus, M):
    answer = min(answer, spread_virus(selected_virus))

if answer == 2e9: print(-1)
else: print(answer)