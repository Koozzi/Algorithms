def move(horse_list, current_horse_idx, move_horse_list, next_i, next_j):
    borad_horse[next_i][next_j] += move_horse_list
    borad_horse[horse_info[num][0]][horse_info[num][1]] = horse_list[:current_horse_idx]
    for horse_num in borad_horse[next_i][next_j]:
        horse_info[horse_num][0] = next_i
        horse_info[horse_num][1] = next_j

def change_direction(num):
    if horse_info[num][2] == 0: horse_info[num][2] = 1
    elif horse_info[num][2] == 1: horse_info[num][2] = 0
    elif horse_info[num][2] == 2: horse_info[num][2] = 3
    elif horse_info[num][2] == 3: horse_info[num][2] = 2

def move_horse(num):
    global N

    horse_list = borad_horse[horse_info[num][0]][horse_info[num][1]]
    current_horse_idx = horse_list.index(num)
    move_horse_list = horse_list[current_horse_idx:]

    next_i = horse_info[num][0] + move_dir[horse_info[num][2]][0]
    next_j = horse_info[num][1] + move_dir[horse_info[num][2]][1]

    if not 0 <= next_i < N or not 0 <= next_j < N:
        change_direction(num)
        
        next_i = horse_info[num][0] + move_dir[horse_info[num][2]][0]
        next_j = horse_info[num][1] + move_dir[horse_info[num][2]][1]

        if 0 <= next_i < N and 0 <= next_j < N:
            if board_color[next_i][next_j] == 0:
                move(horse_list, current_horse_idx, move_horse_list, next_i, next_j)
                
            elif board_color[next_i][next_j] == 1:
                move_horse_list.reverse()
                move(horse_list, current_horse_idx, move_horse_list, next_i, next_j)
           
    elif board_color[next_i][next_j] == 0: 
        move(horse_list, current_horse_idx, move_horse_list, next_i, next_j)
    
    elif board_color[next_i][next_j] == 1:
        move_horse_list.reverse()
        move(horse_list, current_horse_idx, move_horse_list, next_i, next_j)
    
    elif board_color[next_i][next_j] == 2:
        change_direction(num)

        next_i = horse_info[num][0] + move_dir[horse_info[num][2]][0]
        next_j = horse_info[num][1] + move_dir[horse_info[num][2]][1]

        if 0 <= next_i < N and 0 <= next_j < N:
            if board_color[next_i][next_j] == 0:
                move(horse_list, current_horse_idx, move_horse_list, next_i, next_j)
                
            elif board_color[next_i][next_j] == 1:
                move_horse_list.reverse()
                move(horse_list, current_horse_idx, move_horse_list, next_i, next_j)
    
    return horse_info[num][0], horse_info[num][1]
        


N, K = map(int, input().split())
board_color = [list(map(int, input().split())) for i in range(N)]
borad_horse = [[[] for j in range(N)] for i in range(N)]
horse_info = [list(map(int, input().split())) for i in range(K)]
move_dir = [[0,1],[0,-1],[-1,0],[1,0]]
for num, horse in enumerate(horse_info):
    horse[0] -= 1
    horse[1] -= 1
    horse[2] -= 1
    borad_horse[horse[0]][horse[1]].append(num)

for turn in range(1,1001):

    for num, horse in enumerate(horse_info):
        next_i, next_j = move_horse(num)
        if len(borad_horse[next_i][next_j]) > 3:
            print(turn)
            exit()

print(-1)