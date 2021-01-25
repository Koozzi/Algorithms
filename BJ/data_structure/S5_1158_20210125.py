from collections import deque

def solution(N, K):
    L = list(range(1, N+1))
    q = deque(L)
    ans = []

    idx = 0
    while q:
        idx += 1
        if idx % K == 0:
            ans.append(q[0])
            q.popleft()
        else:
            q.append(q[0])
            q.popleft()

    print('<', end='')
    for i in range(N-1):
        print(ans[i], end=', ')
    print(ans[-1], end='')
    print('>')

def solution2(N, K):
    L = list(range(1, N+1))
    idx = 0
    print("<", end="")
    while L:
        idx = (idx+K-1) % len(L)
        print(L[idx], end="")
        L = L[:idx] + L[idx+1:]
        if not L: break
        print(", ", end="")
    print(">")

def solution3(N, K):
    L = list(range(1, N+1))
    idx = 0
    print("<", end="")
    for i in range(N-1):
        idx = (idx+K-1) % len(L)
        print(L[idx], end=", ")
        L.pop(idx)
    print("{}>".format(L[0]))

if __name__=="__main__":
    N, K = map(int, input().split())

    solution3(N, K)
