# def solve(cnt):
#     if cnt == M:
#         num = ''.join(map(str, answer))
#         if num not in answer_set:
#             answer_set.add(num)
#             print(*answer)
#         return

#     for i in range(N):
#         answer.append(numbers[i])
#         solve(cnt + 1)
#         answer.pop()

# N, M = map(int, input().split())
# numbers = sorted(list(map(int, input().split())))
# answer_set = set()
# answer = []

# solve(0)
from itertools import product

N, M = map(int, input().split())
numbers = set(map(int, input().split()))
prods = sorted(product(numbers, repeat=M))

for prod in prods:
    print(' '.join(map(str, prod)))

