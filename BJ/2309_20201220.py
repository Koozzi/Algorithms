from itertools import combinations

heights = []
for i in range(9):
    heights.append(int(input()))

heights.sort()

comb_heights = list(combinations(heights, 7))
for comb in comb_heights:
    if sum(comb) == 100:
        for i in comb:
            print(i)
        exit()