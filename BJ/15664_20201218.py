# def solve(cnt):
#     if cnt == M:
#         num = ''.join(map(str, answer))
#         if num not in answer_set:
#             answer_set.add(num)
#             print(*answer)
#         return

#     for i in range(N):
#         if used[i] == True: continue
#         if numbers[i] < answer[-1]: continue
#         answer.append(numbers[i])
#         used[i] = True
#         solve(cnt + 1)
#         used[i] = False
#         answer.pop()
    

# N, M = map(int,input().split())
# numbers = sorted(list(map(int, input().split())))
# used = [False for _ in range(N)]
# answer_set = set()
# answer = []

# for i in range(N):
#     answer.append(numbers[i])
#     used[i] = True
#     solve(1)
#     used[i] = False
#     answer.pop()

from itertools import combinations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
combs = sorted(list(set(combinations(numbers, M))))

for comb in combs:
    print(' '.join(map(str,comb)))