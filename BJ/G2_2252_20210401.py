from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
dependency = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
q = deque([])

for _ in range(K):
    A, B = map(int, stdin.readline().split())
    dependency[A].append(B)
    indegree[B] += 1

for num in range(1, N+1):
    if indegree[num] == 0:
        q.append(num)

while q:
    current = q.popleft()
    print(current, end=" ")
    for prev in dependency[current]:
        indegree[prev] -= 1
        if indegree[prev] == 0:
            q.append(prev)