import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
ans = []

def solve(start):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
    else:
        for i in range(start+1, N+1):
            ans.append(i)
            solve(i)
            ans.pop()

solve(0)