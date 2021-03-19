from heapq import heappop, heappush

def dijkstra(start_node):
    distance = [2e9 for _ in range(10001)]
    distance[start_node] = 0
    heap = [[0, start_node]]
    while heap:
        current_weight, current_node = heappop(heap)
        for next_node, next_weight in relation[current_node]:
            if next_node > 10000: continue
            if current_weight + next_weight < distance[next_node]:
                distance[next_node] = current_weight + next_weight
                heappush(heap, [distance[next_node], next_node])
    
    return distance[D]

N, D = map(int, input().split())
relation = [[[i+1, 1]] for i in range(10001)]
for _ in range(N):
    A, B, W = map(int, input().split())
    relation[A].append([B, W])
    
print(dijkstra(0))