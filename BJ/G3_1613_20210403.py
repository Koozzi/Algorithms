'''
시작 00:17
제출 00:33
종료 00:45
'''
from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A-1][B-1] = True

for k in range(N):
    for i in range(N):
        if graph[i][k]:
            for j in range(N):
                if graph[k][j]:
                    graph[i][j] = True

S = int(stdin.readline())
for _ in range(S):
    A, B = map(int, stdin.readline().split())
    if graph[A-1][B-1]:
        print(-1)
    else:
        if graph[B-1][A-1]:
            print(1)
        else:
            print(0)