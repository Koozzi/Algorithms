from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False for _ in range(N)])
answer = 0
while True:
    answer += 1

    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            robot[i], robot[i + 1] = False, True
            belt[i + 1] -= 1
    robot[-1] = False

    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    zero_count = 0
    for num in belt:
        if num == 0:
            zero_count += 1

    if K <= zero_count:
        break

print(answer)
