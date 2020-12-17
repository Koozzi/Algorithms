def solve(cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(N):
        answer.append(numbers[i])
        solve(cnt + 1)
        answer.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answer = []

solve(0)