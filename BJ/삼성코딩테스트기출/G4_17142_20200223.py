from itertools import combinations
from collections import deque
from copy import deepcopy
from sys import stdin

def spread_check():
    global N
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                return False
    return True

def spread_virus(virus):
    global N
    visit = [[False for j in range(N)] for i in range(N)]
    _depth = [[0 for j in range(N)] for i in range(N)]
    q = deque([])
    
    for v in virus:
        visit[v[0]][v[1]] = True
        q.append([v[0], v[1], 0])
    
    if spread_check():
        return True, 0

    while q:
        ci, cj, cd = q.popleft()

        for move in move_dir:
            ni, nj = ci + move[0], cj + move[1]
            
            if ni < 0 or nj < 0 or ni == N or nj == N:
                continue
            if visit[ni][nj] or board[ni][nj] == '-':
                continue

            if board[ni][nj] == '.':
                _depth[ni][nj] = cd + 1
            board[ni][nj] = '*'
            visit[ni][nj] = True
            q.append([ni, nj, cd+1])
            depth = cd + 1 

    depth = 0
    for row in _depth:
        for num in row:
            depth = max(depth, num)

    if spread_check(): return True, depth
    else: return False, 0

move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
virus_info = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            board[i][j] = '*'
            virus_info.append([i,j])
        if board[i][j] == 1:
            board[i][j] = '-'
        if board[i][j] == 0:
            board[i][j] = '.'

answer = 2e9
comb_virus = list(combinations(virus_info, M))
init_board = deepcopy(board)
for virus in comb_virus:
    board = deepcopy(init_board)
    check, time = spread_virus(virus)
    if check: answer = min(answer, time)

if answer == 2e9: print(-1)
else: print(answer)