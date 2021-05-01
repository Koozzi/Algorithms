# 17:55
# 18:55
#

from itertools import combinations
from collections import deque

def spread_virus(virus, board, safe_cnt):
    
    new_virus_cnt = 0 # 값이 safe_cnt와 같아지면 바로 Return
    visit = [[False for _ in range(N)] for _ in range(N)]
    q = deque([])

    for I, J in virus:
        visit[I][J] = True
        q.append([I,J,0])

    while q:
        current_i, current_j, current_d = q.popleft()
        
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1] 
            
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] != 1:
                if board[next_i][next_j] == 0:
                    new_virus_cnt += 1
                    if new_virus_cnt == safe_cnt:
                        return current_d + 1

                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d+1])

    return 2e9

if __name__=="__main__":
    answer = 2e9
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    safe_cnt = 0
    virus_info = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                virus_info.append([i,j])
            elif board[i][j] == 0:
                safe_cnt += 1
    
    if safe_cnt == 0:
        print(0)
        exit()
    
    comb_virus_info = combinations(virus_info, M)
    for virus in comb_virus_info:
        answer = min(answer, spread_virus(virus, board, safe_cnt))
    
    if answer == 2e9: print(-1)
    else: print(answer)