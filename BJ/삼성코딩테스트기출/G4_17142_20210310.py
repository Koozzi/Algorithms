from itertools import combinations
from collections import deque
from copy import deepcopy

def spread_check(new_board):
    global N

    for i in range(N):
        for j in range(N):
            if new_board[i][j] == 0:
                return False
    
    return True

def spread_virus(new_board, virus):
    global N, M, zero_cnt, virus_cnt

    _zero_cnt = 0
    visit = [[False for j in range(N)] for i in range(N)]
    q = deque([])
    for v in virus:
        visit[v[0]][v[1]] = True
        q.append([v[0], v[1], 0])
    
    while q:
        current_i, current_j, current_d = q.popleft()

        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if new_board[next_i][next_j] == 1:
                continue
            if visit[next_i][next_j]:
                continue
            if new_board[next_i][next_j] == 0:
                _zero_cnt += 1
                if _zero_cnt == zero_cnt:
                    return current_d+1, new_board
            q.append([next_i, next_j, current_d+1])
            visit[next_i][next_j] = True
            
    return 2e9, new_board

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

if spread_check(board):
    print(0)
    exit()

virus_info = []
zero_cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            zero_cnt += 1
        elif board[i][j] == 2:
            virus_info.append([i,j])

answer = 2e9
comb_virus = list(combinations(virus_info, M))
for virus in comb_virus:
    new_board = deepcopy(board)
    spread_time, new_board = spread_virus(new_board, virus)
    answer = min(answer, spread_time)

if answer == 2e9: print(-1)
else: print(answer)