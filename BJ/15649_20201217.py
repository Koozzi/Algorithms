from itertools import permutations

N, M = map(int, input().split())
new_list = map(str, range(1, N+1))
permutes = list(map(' '.join, permutations(new_list,M)))
for permute in permutes:
    print(permute)