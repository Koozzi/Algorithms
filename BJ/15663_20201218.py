from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
permutes = sorted(list(set(permutations(numbers, M))))

for permute in permutes:
    print(' '.join(map(str, permute)))