"""
시작 23:21
종료 23:43
"""
from collections import deque


def find_password():
    for idx in range(0, N, C):
        p = ''
        for sub_idx in range(idx, idx+C):
            p += q[sub_idx]
        password.add(p)


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    C = N // 4
    q = deque(list(input()))
    password = set([])

    for _ in range(C+1):
        q.rotate(1)
        find_password()

    password = list(password)
    password.sort(reverse=True)
    answer = int(password[K-1], 16)
    print("#{} {}".format(t, answer))