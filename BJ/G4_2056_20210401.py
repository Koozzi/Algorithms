N = int(input())

dp = [0] * (N+1)

for num in range(1, N+1):
    s = list(map(int, input().split()))

    if s[1] == 0:
        dp[num] = s[0]
        continue

    max_value = 0
    for before in s[2:]:
        max_value = max(max_value, dp[before])
    
    dp[num] = s[0] + max_value

print(max(dp))