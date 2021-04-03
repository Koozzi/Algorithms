from collections import deque
from sys import stdin

N = int(stdin.readline())

answer = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
to_graph = [[] for _ in range(N+1)]
from_graph = [[] for _ in range(N+1)]

K = int(stdin.readline())
for _ in range(K):
    A, B, D = map(int, stdin.readline().split())
    to_graph[A].append([B,D])
    from_graph[B].append([A,D])
    indegree[B] += 1

S, E = map(int, stdin.readline().split())

q = deque([S])
while q:
    now = q.popleft()
    for _next, time in to_graph[now]:
        indegree[_next] -= 1
        if indegree[_next] == 0:
            q.append(_next)
        answer[_next] = max(answer[_next], answer[now] + time)

check = [False for _ in range(N+1)]
check[E] = True
q.append(E)
cnt = 0
while q:
    now = q.popleft()
    for _back, time in from_graph[now]:
        if answer[now] - answer[_back] == time:
            cnt += 1
            if not check[_back]:
                check[_back] = True
                q.append(_back)

print(max(answer))
print(cnt)