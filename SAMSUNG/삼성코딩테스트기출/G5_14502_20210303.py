from collections import deque
from itertools import combinations
from copy import deepcopy

def BFS(copied_board):
    global N, M

    q = deque()
    visit = [[False for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 2:
                q.append([i,j])
                visit[i][j] = True

    while q:
        current_i, current_j = q.popleft()

        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            if visit[next_i][next_j]:
                continue
            if copied_board[next_i][next_j] == 1:
                continue

            q.append([next_i, next_j])
            visit[next_i][next_j] = True
            copied_board[next_i][next_j] = 2
    
    safe_cnt = 0
    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 0:
                safe_cnt += 1
    
    return safe_cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

wall_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            wall_list.append([i,j])

answer = 0
comb_wall_list = list(combinations(wall_list, 3))
for new_wall in comb_wall_list:
    copied_board = deepcopy(board)
    for wall in new_wall:
        copied_board[wall[0]][wall[1]] = 1
    answer = max(answer, BFS(copied_board))

print(answer)