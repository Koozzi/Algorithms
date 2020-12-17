def solve(start, cnt):
    if cnt == M:
        # print(*answer)
        # print(" ".join(map(str, answer)))
        return 

    for i in range(start, N):
        answer.append(new_list[i])
        solve(i+1, cnt+1)
        answer.pop()

N, M = map(int, input().split())
new_list = [i+1 for i in range(N)]
answer = []

solve(0, 0)