import sys

N = int(input())
size_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i, pres in enumerate(size_info):
    rank = 1
    for j, target in enumerate(size_info):
        if i == j: continue
        if pres[0] < target[0] and pres[1] < target[1]:
            rank += 1
            
    print(rank, end=" ")