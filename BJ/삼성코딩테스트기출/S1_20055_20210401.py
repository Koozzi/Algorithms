'''
15:55
16:15
'''
from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
belt = deque(list(map(int, stdin.readline().split())))
robot = deque([False for _ in range(N)])

# 올라가는 idx : 0
# 내려오는 idx : N-1

answer, t = 0, 0
while True:
    answer += 1

    # 벨트가 한 칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = False

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for idx in range(N-2, -1, -1):
        if robot[idx] and not robot[idx+1] and belt[idx+1] > 0:
            robot[idx] = False
            robot[idx+1] = True
            belt[idx+1] -= 1
            if belt[idx+1] == 0:
                t += 1

    robot[N-1] = False

    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            t += 1
    
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 
    # 그렇지 않다면 1번으로 돌아간다.
    if t >= K:
        break

print(answer)
    