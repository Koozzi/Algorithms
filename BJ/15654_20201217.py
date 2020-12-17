from itertools import permutations

N, M = map(int, input().split())
new_list = list(map(int, input().split()))
new_list.sort()

permutes = list(permutations(new_list, M))
for permute in permutes:
    print(*permute)