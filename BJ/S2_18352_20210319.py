from heapq import heappop, heappush
from collections import deque

def dijkstra2(start_node):
    distance = [2e9 for _ in range(N+1)]
    distance[start_node] = 0
    q = deque([start_node])
    while q:
        current_node = q.popleft()
        for next_node, weight in relation[current_node]:
            if distance[current_node] + weight < distance[next_node]:
                distance[next_node] = distance[current_node] + weight
                q.append(next_node)

    flag = False
    for city, dist in enumerate(distance[1:], start=1):
        if dist == K:
            flag = True
            print(city)
        
    if not flag:
        print(-1)

# 간선의 weight가 모두 달랐다면 아래 함수가 더 빨랐을 것.
def dijkstra(start_node):
    distance = [2e9 for _ in range(N+1)]
    distance[start_node] = 0
    heap = [[0, start_node]]
    while heap:
        current_weight, current_node = heappop(heap)
        for next_node, next_weight in relation[current_node]:
            if current_weight + next_weight < distance[next_node]: 
                distance[next_node] = current_weight + next_weight
                heappush(heap, [distance[next_node], next_node])

    flag = False
    for city, dist in enumerate(distance[1:], start=1):
        if dist == K:
            flag = True
            print(city)
        
    if not flag:
        print(-1)
    

N, M, K, X = map(int, input().split())
relation = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    relation[A].append([B,1])

dijkstra2(X)