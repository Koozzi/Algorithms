def solve(start, cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(start, N):
        answer.append(number[i])
        solve(i + 1, cnt + 1)
        answer.pop()

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
answer = []

solve(0, 0)