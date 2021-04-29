from collections import deque
from sys import stdin


N, M = map(int, stdin.readline().split())
belt = deque(list(map(int, stdin.readline().split())))
robot = deque([False for _ in range(N)])
answer = 0

while True:

    answer += 1

    # 벨트가 한 칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = False

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(N-1, 0, -1):
        if belt[i] > 0 and not robot[i] and robot[i-1]:
            robot[i-1], robot[i] = False, True
            belt[i] -= 1
    robot[N-1] = False

    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if belt[0] > 0 and not robot[0]:
        robot[0] = True
        belt[0] -= 1

    zero_count = 0
    for num in belt:
        if num == 0:
            zero_count += 1

    if zero_count >= M:
        break

print(answer)