from collections import deque

N, K = map(int, input().split())
robot = deque([False for i in range(N*2)])
belt = deque(list(map(int, input().split())))
answer, cnt = 0, 0

while True:

    answer += 1

    # Step1
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = False

    #Step2
    for i in range(N-2, -1, -1):
        if robot[i] and belt[i+1] > 0 and not robot[i+1]:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1

            if belt[i+1] == 0:
                cnt += 1
        robot[N-1] = False
    
    # Step3
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

        if belt[0] == 0:
            cnt += 1

    #Step4
    if cnt >= K:
        break

print(answer)