'''
01:45
02:05
'''

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

graph = [[] for _  in range(N+1)]
indegree = [0 for _ in range(N+1)]
answer = []

for _ in range(M):
    playlist = list(map(int, stdin.readline().split()))
    for idx in range(1, playlist[0]):
        graph[playlist[idx]].append(playlist[idx+1])
        indegree[playlist[idx+1]] += 1

q = deque([])
for idx in range(1, N+1):
    if indegree[idx] == 0:
        q.append(idx)

while q:
    now = q.popleft()
    answer.append(now)
    for _next in graph[now]:
        indegree[_next] -= 1
        if indegree[_next] == 0:
            q.append(_next)

if len(answer) != N:
    print(0)
else:
    for num in answer:
        print(num)