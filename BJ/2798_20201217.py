import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
picked = list(combinations(card, 3))

ans = 0
for nums in picked:
    card_sum = sum(nums)
    if card_sum <= M:
        ans = max(ans, card_sum)

print(ans)
