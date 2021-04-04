'''
시작 17:47
제출 18:13
종료
'''

from itertools import combinations
from collections import deque
from copy import deepcopy

def spread_virus(copied_board, q, visit):

    spread_cnt = 0

    while q:
        current_i, current_j, current_d = q.popleft()

        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if visit[next_i][next_j]:
                continue
            if copied_board[next_i][next_j] == 9 or copied_board[next_i][next_j] == 1:
                continue
            
            if copied_board[next_i][next_j] == 0:
                copied_board[next_i][next_j] = 9
                spread_cnt += 1
                if spread_cnt == safe_cnt:
                    return current_d + 1

            visit[next_i][next_j] = True
            q.append([next_i,next_j,current_d+1])

    return -1

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

safe_cnt, total_virus = 0, []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            total_virus.append([i,j])
        elif board[i][j] == 0:
            safe_cnt += 1

if safe_cnt == 0:
    print(0)
    exit()

answer = 2e9
for viruses in combinations(total_virus, M):
    visit = [[False for _ in range(N)] for _ in range(N)]
    copied_board = deepcopy(board)
    q = deque([])

    for I, J in viruses:
        visit[I][J] = True
        q.append([I,J,0])
        copied_board[I][J] = 9
    
    time = spread_virus(copied_board, q, visit)
    if time != -1:
        answer = min(answer, time)

if answer == 2e9: print(-1)
else: print(answer)