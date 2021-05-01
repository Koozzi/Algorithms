# 23:52
# 23:01
#

from itertools import combinations
from collections import deque

def spread_virus(virus):
    new_virus_count = 0
    q = deque([])
    visit = [[False for _ in range(N)] for _ in range(N)]
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
                    new_virus_count += 1
                    if new_virus_count == safe_count:
                        return current_d + 1
                visit[next_i][next_j] = True
                q.append([next_i,next_j,current_d+1])
    return 2e9



if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    total_virus = []
    answer, safe_count = 2e9, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                total_virus.append([i,j])
            elif board[i][j] == 0:
                safe_count += 1

    if safe_count == 0:
        print(0)
        exit()

    for virus in combinations(total_virus, M):
        answer = min(answer, spread_virus(virus))
    
    if answer == 2e9: print(-1)
    else: print(answer)