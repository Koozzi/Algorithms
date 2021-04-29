from collections import deque

def BFS(start_node):
    visit[start_node] = True
    q = deque([start_node])
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

answer = 0
for node in range(1, N+1):
    if not visit[node]:
        answer += 1
        BFS(node)

print(answer)