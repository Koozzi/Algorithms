'''
시작 17:30
제출 17:48
종료
'''

from itertools import combinations
from collections import deque

def spread_virus(viruses):
    visit = [[False for _ in range(N)] for _ in range(N)]    
    q = deque([])
    spread_cnt = 0

    for I,J in viruses:
        visit[I][J] = True
        q.append([I,J,0])
    
    while q:
        current_i, current_j, current_d = q.popleft()

        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            
            if not visit[next_i][next_j] and board[next_i][next_j] != 1:
                visit[next_i][next_j] = True
                q.append([next_i,next_j,current_d + 1])

                if board[next_i][next_j] == 0:
                    spread_cnt += 1
                if spread_cnt == total_safe_area:
                    return current_d + 1
    
    return 2e9


answer = 2e9
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

init_virus = []
total_safe_area = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            init_virus.append([i,j])
        elif board[i][j] == 0:
            total_safe_area += 1

if total_safe_area == 0:
    print(0)
    exit()

for viruses in combinations(init_virus, M):
    answer = min(answer, spread_virus(viruses))

if answer == 2e9: print(-1)
else: print(answer)