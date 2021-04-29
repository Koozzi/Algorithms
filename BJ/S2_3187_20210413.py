from collections import deque

def BFS(start_i, start_j):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    
    k, v = 0, 0
    if board[start_i][start_j] == 'k': k += 1
    elif board[start_i][start_j] == 'v': v += 1

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and board[next_i][next_j] != '#':
                    visit[next_i][next_j] = True    
                    q.append([next_i, next_j])
                    if board[next_i][next_j] == 'v': v += 1
                    elif board[next_i][next_j] == 'k': k += 1

    if k > v: return k, 0
    else: return 0, v

N, M = map(int, input().split())
board = [input() for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

k_count, v_count = 0, 0
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] != '#':
            k, v = BFS(i, j)
            k_count += k
            v_count += v

print(k_count, v_count)