def solve(start, cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(start, N):
        answer.append(numbers[i])
        solve(i, cnt + 1)
        answer.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answer = []

solve(0,0)