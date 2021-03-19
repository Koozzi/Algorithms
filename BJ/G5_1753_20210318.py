from heapq import heappop, heappush
from collections import deque

def dijkstra(start_node):
    distance = [2e9 for i in range(V+1)]
    distance[start_node] = 0
    heap = []
    heappush(heap, [0,start_node])
    while heap:
        weight, current_node = heappop(heap)
        for next_node, next_weight in relation[current_node]:
            if weight + next_weight < distance[next_node]:
                distance[next_node] = weight + next_weight
                heappush(heap, [weight + next_weight, next_node])
    
    for num in distance[1:]:
        if num == 2e9: print('INF')
        else: print(num)

V, E = map(int, input().split())
start_node = int(input())
relation = [[] for i in range(V+1)]
for _ in range(E):
    A, B, D = map(int, input().split())
    relation[A].append([B,D])

dijkstra(start_node)