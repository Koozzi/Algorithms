def solve(cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(N):
        answer.append(i + 1)
        solve(cnt + 1)
        answer.pop()

N, M = map(int, input().split())
new_list = [i+1 for i in range(N)]
answer = []

solve(0)