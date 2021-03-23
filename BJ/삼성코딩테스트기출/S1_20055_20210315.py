from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int , input().split())))
robot_on_belt = deque([False for i in range(N)])
answer, cnt = 0, 0
while True:
    answer += 1
    belt.rotate(1)
    robot_on_belt.rotate(1)
    robot_on_belt[N-1] = False

    for i in range(N-2, -1, -1):
        if not robot_on_belt[i]: continue # 현재 위치에 로봇이 있어야 함
        if robot_on_belt[i+1]: continue   # 다음 위치에 로봇이 없어야 함
        if belt[i+1] == 0: continue       # 다음 위치에 내구도가 1 이상이어야 함
        robot_on_belt[i] = False
        robot_on_belt[i+1] = True
        belt[i+1] -= 1
        if belt[i+1] == 0:
            cnt += 1

    robot_on_belt[N-1] = False            # 내려가는 위치에 있는 로봇은
                                          # 반드시 내려가야 한다.  

    if not robot_on_belt[0] and belt[0] > 0:
        robot_on_belt[0] = True 
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    
    if cnt >= K:
        break

print(answer)