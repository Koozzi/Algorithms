import sys

N, M = map(int, sys.stdin.readline().split())

used = [False] * (N+1)
ans = []

def solve():
    if len(ans) == M:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    else:
        for i in range(1, N+1):
            if used[i] == False:
                ans.append(i)
                used[i] = True
                solve()
                used[i] = False
                ans.pop()

solve()