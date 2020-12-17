A = int(input())
talk_info = [list(map(int, input().split())) for i in range(A)]
dp = [0] * A

if talk_info[-1][0] == 1:
    dp[A-1] = talk_info[-1][1]

for i in range(A-2, -1, -1):

    time = talk_info[i][0]
    price = talk_info[i][1]
    
    if  i + time > A:
        dp[i] = dp[i+1]
        continue

    if  i + time == A:
        dp[i] = max(price, dp[i+1])
        continue

    dp[i] = max(dp[i+1], dp[i+time] + price)
   
print(max(dp))