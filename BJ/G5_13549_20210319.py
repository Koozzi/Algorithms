from collections import deque

def find_sister(start_node, end_node):
    time = [2e9 for _ in range(100001)]
    time[start_node] = 0
    q = deque([start_node])
    while q:
        current_node = q.popleft()
        next_node_1 = current_node - 1
        next_node_2 = current_node + 1
        next_node_3 = current_node * 2

        if next_node_1 >= 0:
            if time[current_node] + 1 < time[next_node_1]:
                time[next_node_1] = time[current_node] + 1
                q.append(next_node_1)
        
        if next_node_2 <= 100000:
            if time[current_node] + 1 < time[next_node_2]:
                time[next_node_2] = time[current_node] + 1
                q.append(next_node_2)
        
        if next_node_3 <= 100000:
            if time[current_node] < time[next_node_3]:
                time[next_node_3] = time[current_node]
                q.append(next_node_3)

    return time[end_node]

N, K = map(int, input().split())
print(find_sister(N,K))