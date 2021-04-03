'''
00:40
01:20
'''
from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    N, K = map(int, stdin.readline().split())
    time = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    answer = [0 for _ in range(N+1)]

    for _ in range(K):
        A, B = map(int, stdin.readline().split())
        graph[A].append(B)
        indegree[B] += 1

    q = deque([])    
    for idx in range(1, N+1):
        if indegree[idx] == 0:
            q.append(idx)
        answer[idx] = time[idx-1]
    
    while q:
        num = q.popleft()
        
        for next_num in graph[num]:
            indegree[next_num] -= 1
            if indegree[next_num] == 0:
                q.append(next_num)
            answer[next_num] = max(answer[next_num], time[next_num-1] + answer[num])
    
    W = int(stdin.readline())
    print(answer[W])