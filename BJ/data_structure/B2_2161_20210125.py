from collections import deque

def solution(N, L):
    q = deque(L)

    while N > 1:
        print(q[0], end=' ')
        q.popleft()
        q.append(q[0])
        q.popleft()
        N -= 1

    print(q[0])

if __name__ == "__main__":
    N = int(input())
    L = list(range(1, N+1))

    solution(N, L)