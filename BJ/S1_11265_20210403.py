'''
시작 23:55
제출 00:09
종료 00:09
'''
from collections import deque

def get_dijkstra(num):
    q = deque([[num, 0]])   
    while q:
        c, d = q.popleft() 
        for n in relation[c]:
            if d + board[c][n] < dijkstra[num][n]:
                dijkstra[num][n] = d + board[c][n]
                q.append([n, d + board[c][n]])

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dijkstra = [[2e9 for _ in range(N)] for _ in range(N)]
relation = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            if board[i][j] != 0:
                relation[i].append(j)

for num in range(N):
    get_dijkstra(num)

for _ in range(M):
    A, B, C = map(int, input().split())
    if dijkstra[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")