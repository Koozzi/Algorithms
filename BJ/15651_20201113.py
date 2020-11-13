import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
ans = []

def solve():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
    else:
        for i in range(1, N+1):
            ans.append(i)
            solve()
            ans.pop()

solve()