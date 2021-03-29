# 12:13
# 12:31
# 
from collections import deque
from itertools import combinations
from copy import deepcopy

def make_new_wall(copied_board, new_wall):
    for wall in new_wall:
        copied_board[wall[0]][wall[1]] = 1
    return copied_board

def spread_virus(copied_board, total_safe_section_cnt):
    new_total_safe_section_cnt = total_safe_section_cnt - 3
    visit = [[False for j in range(M)] for i in range(N)]
    q = deque([])

    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 2:
                visit[i][j] = True
                q.append([i,j])

    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            
            if not visit[next_i][next_j] and copied_board[next_i][next_j] == 0:
                new_total_safe_section_cnt -= 1
                copied_board[next_i][next_j] = 2
                visit[next_i][next_j] = True
                q.append([next_i,next_j])
    
    return new_total_safe_section_cnt


if __name__=="__main__":
    N, M = map(int, input().split())
    total_safe_section_cnt = 0
    wall_posiible_list, board = [], []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(M):
            if row[j] == 0:
                wall_posiible_list.append([i,j])
                total_safe_section_cnt += 1
    
    answer = 0
    for new_wall in combinations(wall_posiible_list, 3):
        copied_board = deepcopy(board)
        copied_board = make_new_wall(copied_board, new_wall)
        safe_section_cnt = spread_virus(copied_board, total_safe_section_cnt)
        answer = max(answer, safe_section_cnt)

print(answer)