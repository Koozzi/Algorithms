'''
시작 02:31
제출 02:50
종료
'''

from sys import stdin
# from sys import setrecursionlimit

from collections import deque

# setrecursionlimit(10**5)

def bfs(start_node):
    global answer, end_node

    visit = [False for _ in range(N+1)]
    visit[start_node] = True        
    q = deque([[start_node,0]])

    while q:
        current_node, current_weight = q.popleft()
        for next_node, w in graph[current_node]:
            if not visit[next_node]:
                visit[next_node] = True  
                q.append([next_node, current_weight+w])
                if current_weight + w > answer:
                    answer = current_weight + w 
                    end_node = next_node
                    
# def dfs(start_node, current_node):
#     global answer, end_node
    
#     for next_node, w in graph[current_node]:
#         if dfs_weight[next_node] == 0 and next_node != start_node:
#             dfs_weight[next_node] = dfs_weight[current_node] + w
#             if answer < dfs_weight[current_node] + w:
#                 answer = dfs_weight[current_node] + w
#                 end_node = next_node
#             dfs(start_node, next_node)

answer, end_node = 0, 0
N = int(stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A,B,C = map(int, stdin.readline().split())
    graph[A].append([B,C])
    graph[B].append([A,C])

bfs(1)
bfs(end_node)

#dfs_weight = [0 for _ in range(N+1)]
#dfs(1,1)
#dfs_weight = [0 for _ in range(N+1)]
#dfs(end_node,end_node)

print(answer)