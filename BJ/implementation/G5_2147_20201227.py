def change_direction_left(d):
    if d == 'E': return 'N'
    if d == 'N': return 'W'
    if d == 'W': return 'S'
    if d == 'S': return 'E'

def change_direction_right(d):
    if d == 'E': return 'S'
    if d == 'S': return 'W'
    if d == 'W': return 'N'
    if d == 'N': return 'E'

def robot_move(robot_i, robot_j, current_d, robot_num, robot_info, A, B):
    next_i, next_j = 0, 0
    if current_d == 'E': 
        next_i = robot_i
        next_j = robot_j + 1
    if current_d == 'S':
        next_i = robot_i + 1
        next_j = robot_j
    if current_d == 'W':
        next_i = robot_i
        next_j = robot_j - 1
    if current_d == 'N':
        next_i = robot_i - 1
        next_j = robot_j
    
    if next_i < 1 or next_j < 1 or next_i > B or next_j > A:
        print("Robot {0} crashes into the wall".format(robot_num))
        exit()

    for i in range(len(robot_info)):
        if i == 0 or i == robot_num: continue
        if robot_info[i][0] == next_i and robot_info[i][1] == next_j:
            print("Robot {0} crashes into robot {1}".format(robot_num, i))
            exit()
    
    return next_i, next_j


A, B = map(int, input().split())
N, M = map(int, input().split())

robot_info = [[]]
for i in range(N):
    I, J, direction = input().split()
    I, J = int(J), int(I)
    I = B + 1 - I

    robot_info.append([I, J, direction])

for i in range(M):
    robot_num, command, command_cnt = input().split()
    robot_num, command_cnt = int(robot_num), int(command_cnt)

    for _ in range(command_cnt):

        current_i = robot_info[robot_num][0]
        current_j = robot_info[robot_num][1]
        current_d = robot_info[robot_num][2]

        if command == 'L':
            robot_info[robot_num][2] = change_direction_left(current_d)
        if command == 'R':
            robot_info[robot_num][2] = change_direction_right(current_d)
        if command == 'F':
            robot_info[robot_num][0], robot_info[robot_num][1] = robot_move(current_i, current_j, current_d, robot_num, robot_info, A, B)
            
            
print('OK')