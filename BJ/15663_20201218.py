from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
permutes = sorted(list(set(permutations(numbers, M))))

for permute in permutes:
    print(' '.join(map(str, permute)))

# def solve(cnt):
#     if cnt == M:
#         num = ''.join(map(str,answer))
#         if num not in set_ans:
#             set_ans.add(num)
#             print(*answer)
#             return
        
#     for i in range(N):
#         if used[i] == True: continue
#         answer.append(numbers[i])
#         used[i] = True
#         solve(cnt + 1)
#         used[i] = False
#         answer.pop()
        
# N, M = map(int, input().split())
# numbers = sorted(list(map(int, input().split())))
# used = [False for i in range(N)]
# set_ans = set()
# answer = []

# solve(0)