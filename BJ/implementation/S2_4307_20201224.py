import sys

T = int(input())

for t in range(T):
    l, n = map(int, input().split())

    fast_time = 0
    slow_time = 0

    for _ in range(n):
        # ant_location = int(input())
        # 그냥 input으로 받으면 시간초과난다.
        # 이 문제에서는 input()함수를 최대 (10만 X t) 번 호출될 수 있다.
        # 상당히 느림
        ant_location = int(sys.stdin.readline())

        fast = min(ant_location, l - ant_location)
        slow = max(ant_location, l - ant_location)

        fast_time = max(fast_time, fast)
        slow_time = max(slow_time, slow)

    print(fast_time, slow_time)