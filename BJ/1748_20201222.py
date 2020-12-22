N = int(input())

answer = N

for i in range(1, len(str(N))):
    answer += (N - (10 ** i) + 1)

print(answer)