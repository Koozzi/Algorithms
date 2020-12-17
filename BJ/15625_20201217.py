def solve(start, cnt):
    if cnt == M:
        # print(*answer)
        print(' '.join(map(str, answer)))
        return

    for i in range(start, N):
        answer.append(i+1)
        solve(i, cnt+1)
        answer.pop()

N, M = map(int, input().split())
new_list = [i+1 for i in range(N)]
answer = []

solve(0, 0)