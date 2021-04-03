'''
시작 01:06
제출 01:32
종료 02:27

오래걸린 이유
1. 문제 이해 부족
2. 방향성이 없는 그래프인데, graph에 한 방향만 넣어줬음
   (이게 시발 제일 시간 많이 잡아먹음)
'''
from sys import stdin
from collections import deque

N = int(stdin.readline())
graph = [[] for _ in range(N)] 
floyd = [[2e9 for _ in range(N)] for _ in range(N)]

K = int(stdin.readline())
for _ in range(K):
    A, B = map(int, stdin.readline().split())
    floyd[A-1][B-1] = floyd[B-1][A-1] = 1
    graph[A-1].append(B-1)
    graph[B-1].append(A-1) 

visit = [False for _ in range(N)]
groups, group_cnt = [], 0
for num in range(N):
    if not visit[num]:
        groups.append([])
        groups[group_cnt].append(num)
        visit[num] = True
        q = deque([num])
        while q:
            c = q.popleft()
            for n in graph[c]:
                if not visit[n]:
                    groups[group_cnt].append(n)
                    visit[n] = True
                    q.append(n)
        group_cnt += 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and floyd[i][k] + floyd[k][j] < floyd[i][j]:
                floyd[i][j] = floyd[i][k] + floyd[k][j]

answer = []
for group in groups:  
    leader, min_num = 0, 2e9
    for num in group:
        max_num = 0
        for j in range(N):
            if floyd[num][j] != 2e9 and floyd[num][j] > max_num:
                max_num = floyd[num][j]
        if max_num < min_num:
            min_num = max_num
            leader = num

    answer.append(leader+1)

print(len(groups))
answer.sort()
for a in answer:
    print(a)