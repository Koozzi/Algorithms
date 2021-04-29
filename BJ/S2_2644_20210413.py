from collections import deque

def BFS(start_node, end_node):
    visit = [False for _ in range(N+1)]
    visit[start_node] = True
    q = deque([[start_node, 0]])
    while q:
        current_node, current_depth = q.popleft()

        if current_node == end_node:
            return current_depth

        for next_node in graph[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append([next_node, current_depth+1])
    
    return -1

N = int(input())
X, Y = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)   
    graph[B].append(A)

print(BFS(X, Y))