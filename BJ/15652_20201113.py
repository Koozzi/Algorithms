import sys
input = sys.stdin.readline()

N, M = map(int, input.split())

ans = []

def solve():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
        if i >= ans[len(ans) - 1]:
            ans.append(i)
            solve()
            ans.pop()

for i in range(1, N+1):
    ans.append(i)
    solve()
    ans.pop()