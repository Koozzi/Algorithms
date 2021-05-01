from collections import deque

def rotate(command):
    
    X, D, K = command
    for i in range(X, N+1, X):
        if D == 0:
            for _ in range(K):
                board[i-1].insert(0, board[i-1][-1])
                board[i-1].pop()
        elif D == 1:
            for _ in range(K):
                board[i-1].append(board[i-1][0])
                board[i-1].pop(0)

def BFS(start_i, start_j):

    q = deque([[start_i, start_j]])
    visit[start_i][start_j] = True
    tmp = [[start_i, start_j]] 

    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i, next_j = current_i + move[0], current_j + move[1]
            
            if 0 <= next_i < N:
                if next_j == -1: next_j = M-1
                elif next_j == M: next_j = 0

                if visit[next_i][next_j]:
                    continue
                
                if board[current_i][current_j] == board[next_i][next_j]:
                    q.append([next_i, next_j])
                    visit[next_i][next_j] = True
                    tmp.append([next_i, next_j])
    
    if len(tmp) > 1:
        for I, J in tmp:
            board[I][J] = 0

    return len(tmp)

def cnt_sum():
    c, s = 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
               c += 1
               s += board[i][j]
    return c, s 

N, M, T  =  map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
commands = [list(map(int, input().split())) for i in range(T)]

for command in commands:
    rotate(command)

    visit = [[False for j in range(M)] for i in range(N)]
    erased = False
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or visit[i][j]: continue
            erase_cnt = BFS(i, j)
            if erase_cnt == 1:continue
            erased = True
                
    if not erased:

        c, s = cnt_sum()

        if c == 0:
            break
        
        avg = s / c
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0: continue
                if board[i][j] > avg: board[i][j] -= 1
                elif board[i][j] < avg: board[i][j] += 1

c, answer = cnt_sum()
print(answer)