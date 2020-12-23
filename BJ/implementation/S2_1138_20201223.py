N = int(input())
left_list = list(map(int, input().split()))
answer = [0 for _ in range(N)]

for i, left in enumerate(left_list):
    for idx in range(N):
        if answer[idx] == 0 and left == 0:
            answer[idx] = i + 1
            break
        elif answer[idx] == 0:
            left -= 1

print(*answer)