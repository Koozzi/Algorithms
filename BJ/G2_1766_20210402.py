'''
01:30

'''

from sys import stdin
from heapq import heappop, heappush

N, K = map(int, stdin.readline().split())

heap = []
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(K):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

for num in range(1, N+1):
    if indegree[num] == 0:
        heappush(heap, num)

while heap:
    now = heappop(heap)
    print(now, end=" ")
    for _next in graph[now]:
        indegree[_next] -= 1
        if indegree[_next] == 0:
            heappush(heap, _next)