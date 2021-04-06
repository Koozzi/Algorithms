from sys import stdin

N, K = map(int, stdin.readline().split())
dp = [1 for _ in range(N+1)]
dependency = [[] for _ in range(N+1)]

for _ in range(K):
    A, B = map(int, stdin.readline().split())
    dependency[B].append(A)

for current in range(1, N+1):
    if not dependency[current]:
        dp[current] = 1
        continue

    max_num = 0
    for prev in dependency[current]:
    
        max_num = max(max_num, dp[prev])
    
    dp[current] = max_num + 1

print(*dp[1:])