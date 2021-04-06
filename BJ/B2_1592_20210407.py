'''
시작 02:03
제출 02:11
종료
'''

N, M, L = map(int, input().split())
friends = [0 for _ in range(N)]
friends[0] = 1

answer, current = 0, 0
while True:
    if friends[current] % 2 == 0:
        current = (current - L) % N
    else:
        current = (current + L) % N
    answer += 1
    friends[current] += 1
    if friends[current] == M:
        break

print(answer)