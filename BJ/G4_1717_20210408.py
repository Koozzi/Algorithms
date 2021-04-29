from sys import stdin

def find_parent(target):
    
    while parent[target] != -1:
        target = parent[target]

    return target

def union(A, B):
    
    A = find_parent(A)
    B = find_parent(B)

    min_num = min(A,B)
    max_num = max(A,B)

    if max_num != min_num:
        parent[min_num] = max_num

N, M = map(int, stdin.readline().split())
parent = [-1 for i in range(N+1)]

for _ in range(M):

    flag, A, B = map(int, stdin.readline().split())

    if flag:
        if find_parent(A) == find_parent(B):
            print("YES")
        else:
            print('NO')
    
    else:
        union(A, B)

    print(A,B,parent)