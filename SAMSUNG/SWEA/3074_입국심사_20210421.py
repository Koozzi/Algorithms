T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    answer = 0
    times = []
    for _ in range(N):
        times.append(int(input()))

    left, right = 0, min(times) * M

    while left <= right:
        mid = (left + right) // 2

        people = 0
        for time in times:
            people += mid // time

        if M <= people:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print("#{} {}".format(t, answer))
