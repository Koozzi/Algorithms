from collections import deque
from sys import stdin

def BFS(start_node):
    visit[start_node] = True
    q = deque([start_node])
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)
                parent[next_node] = current_node

N = int(stdin.readline())
graph = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

BFS(1)

for my_parent in parent[2:]:
    print(my_parent)