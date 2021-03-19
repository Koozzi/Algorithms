from heapq import heappop, heappush

def dijkstra(start_node, end_node):
    total_weight = [ 2e9 for _ in range(N+1) ]
    total_weight[start_node] = 0
    heap = [[0, start_node]]
    while heap:
        current_weight, current_node = heappop(heap)
        for next_node, next_weight in relation[current_node]:
            if current_weight + next_weight < total_weight[next_node]:
                total_weight[next_node] = current_weight + next_weight
                heappush(heap, [total_weight[next_node], next_node])

    return total_weight[end_node]

N = int(input())
M = int(input())
relation = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, W = map(int, input().split())
    relation[A].append([B,W])
start_node, end_node = map(int, input().split())
print(dijkstra(start_node, end_node))