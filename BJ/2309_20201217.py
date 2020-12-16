import sys
from itertools import combinations

l = []
for i in range(9):
    l.append(int(sys.stdin.readline()))

comb_list = list(combinations(l, 7))
for nums in comb_list:
    if sum(nums) == 100:
        nums = list(nums)
        nums.sort()
        for i in nums:
            print(i)
        exit() 