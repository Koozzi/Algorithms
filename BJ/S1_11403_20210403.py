'''
시작 10:42
제출 10:58
종료 10:58
'''
from collections import deque

def check(start):
    q = deque([start])
    while q:
        c = q.popleft()
        for n in relation[c]:
            if answer[start][n] == 0:
                answer[start][n] = 1
                q.append(n)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
relation = [[] for _ in range(N)]
visit = [False for _ in range(N)]
answer = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            relation[i].append(j)

for start in range(N):
    check(start)

for i in answer:
    print(*i)