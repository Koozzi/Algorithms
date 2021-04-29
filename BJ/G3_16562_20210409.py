from sys import stdin

def find_parent(target):
    while parent[target] != ROOT:
        target = parent[target]
    return target

def union(A,B):
    A = find_parent(A)
    B = find_parent(B)

    if price[A] < price[B]:
        parent[B] = A
    elif price[B] < price[A]:
        parent[A] = B
    else:
        min_num = min(A,B)
        max_num = max(A,B)
        if min_num != max_num:
            parent[max_num] = min_num

ROOT = -1
N, M, K = map(int, stdin.readline().split())
price = list(map(int, stdin.readline().split()))
parent = [-1 for _ in range(N)]
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    union(A-1,B-1)

total_price = 0
for _price, _parent in zip(price, parent):
    if _parent == -1:
        total_price += _price

if total_price <= K: print(total_price)
else: print("Oh no")