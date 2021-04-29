from collections import deque

def BFS(start_node):
    visit = [False for _ in range(N+1)]
    visit[start_node] = True
    q = deque([start_node])
    spread_count = 0
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)
                spread_count += 1
    
    return spread_count

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

print(BFS(1))