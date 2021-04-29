from collections import deque

def BFS(start_i, start_j):
    q = deque([[start_i, start_j]])
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            
            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and board[next_i][next_j] == 1:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])
                
T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        I, J = map(int, input().split())
        board[I][J] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] == 1:
                visit[i][j] = True
                answer += 1
                BFS(i,j)
    
    print(answer)