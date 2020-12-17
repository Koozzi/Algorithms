def solve(cnt):
    if cnt == M:
        print(*answer)
        return

    for i in range(len(numbers)):
        if numbers[i] < answer[-1]: continue
        answer.append(numbers[i])
        solve(cnt + 1)
        answer.pop()

N, M = map(int, input().split())
numbers = sorted(set(map(int, input().split())))
answer = []

for i in range(len(numbers)):
    answer.append(numbers[i])
    solve(1)
    answer.pop()