from collections import deque
from sys import stdin

def BFS(start_i, start_j):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and board[next_i][next_j] == 1:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])

while True:
    M, N = map(int, stdin.readline().split())

    if M == 0 and N == 0:
        break

    board = [list(map(int, stdin.readline().split())) for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    land_count = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] == 1:
                land_count += 1
                BFS(i,j)
    
    print(land_count)
