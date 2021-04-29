def woman(num, switch):

    middle_idx = num - 1
    if switch[middle_idx]: switch[middle_idx] = 0
    else: switch[middle_idx] = 1

    for d in range(1, N):
        left_idx = middle_idx - d
        right_idx = middle_idx + d
        
        if left_idx == -1 or right_idx == N:
            break

        if switch[left_idx] != switch[right_idx]:
            break

        if switch[left_idx]:
            switch[left_idx] = 0
            switch[right_idx] = 0
        else:
            switch[left_idx] = 1
            switch[right_idx] = 1

    return switch

def man(num, switch):

    for idx in range(num-1, N, num):
        if switch[idx]: switch[idx] = 0
        else: switch[idx] = 1

    return switch

N = int(input())
switch = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    A, B = map(int, input().split())

    if A == 1: switch = man(B, switch)
    elif A == 2: switch = woman(B, switch)

if N <= 20: print(*switch)
else:
    for idx, num in enumerate(switch):
        print(num, end=" ")
        if idx % 20 == 19:
            print()