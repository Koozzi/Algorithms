from collections import deque
from sys import stdin

def BFS(start_node):
    visit = [False for _ in range(N+1)]
    visit[start_node] = True
    q = deque([start_node])
    spread_count = 1
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)
                spread_count += 1
    
    return spread_count


N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[B].append(A)

max_hack_count = 0
start_computer = []
for computer in range(1, N+1):
    
    spread_count = BFS(computer)
    
    if max_hack_count < spread_count:
        max_hack_count = spread_count
        start_computer = [computer]
    elif max_hack_count == spread_count:
        start_computer.append(computer)

print(*start_computer)