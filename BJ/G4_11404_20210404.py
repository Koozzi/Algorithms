'''
시작 00:50
제출 01:00
종료 
'''

from sys import stdin

N = int(stdin.readline())
floyd = [[2e9 for _ in range(N)] for _ in range(N)]
M = int(stdin.readline())
for _ in range(M):
    A,B,C = map(int, stdin.readline().split())
    floyd[A-1][B-1] = min(floyd[A-1][B-1], C)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and floyd[i][k] + floyd[k][j] < floyd[i][j]:
                floyd[i][j] = floyd[i][k] + floyd[k][j]

for row in floyd:
    for i in range(N):
        if row[i] == 2e9:
            row[i] = 0 
    print(*row)