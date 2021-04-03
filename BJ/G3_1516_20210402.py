'''
02:11
02:26
'''

from sys import stdin
from collections import deque

N = int(stdin.readline())

time = [0 for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for num in range(1, N+1):
    starcraft = list(map(int, stdin.readline().split()))
    answer[num] = time[num] = starcraft[0]
    for prev_num in starcraft[1:len(starcraft)-1]:
        graph[prev_num].append(num)
        indegree[num] += 1

q = deque([])
for num in range(1, N+1):
    if indegree[num] == 0:
        q.append(num)

while q:
    now = q.popleft()

    for _next in graph[now]:
        indegree[_next] -= 1
        if indegree[_next] == 0:
            q.append(_next)
        answer[_next] = max(answer[_next], answer[now] + time[_next])

for num in answer[1:]:
    print(num)