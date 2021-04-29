from sys import stdin

def find_parent(target):
    while parent_city[target] != -1:
        target = parent_city[target]
    return target

def union(A,B):
    A = find_parent(A)
    B = find_parent(B)
    
    min_city = min(A, B)
    max_city = max(A, B)
    
    if min_city != max_city:
        parent_city[min_city] = max_city

N = int(stdin.readline())
M = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
travel = list(map(int, stdin.readline().split()))
parent_city = [-1 for _ in range(N+1)]

for i in range(N):
    for j in range(i):
        if board[i][j] == 1:
            union(i+1, j+1)

destination = find_parent(travel[0])
for num in travel[1:]:
    if find_parent(num) != destination:
        print("NO")
        exit()

print("YES")