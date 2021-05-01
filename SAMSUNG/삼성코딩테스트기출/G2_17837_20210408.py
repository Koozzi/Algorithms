'''
시작 01:32
제출 01:57
종료
'''

def change_direction(D):
    if D == 0: return 1
    elif D == 1: return 0
    elif D == 2: return 3
    elif D == 3: return 2

def horse_move(horse_num,answer):
    
    I, J, D = horse_info[horse_num]

    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if 0 <= next_i < N and 0 <= next_j < N:
        if color_board[next_i][next_j] == 2:
            D = change_direction(D)
    else:
        D = change_direction(D)

    horse_info[horse_num][2] = D
    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if 0 <= next_i < N and 0 <= next_j < N:
        if color_board[next_i][next_j] != 2:
            go_to_next_location(horse_num, answer)

def go_to_next_location(horse_num, answer):

    I, J, D = horse_info[horse_num]

    horse_index = horse_board[I][J].index(horse_num)
    moving_horse = horse_board[I][J][horse_index:]
    horse_board[I][J] = horse_board[I][J][:horse_index]

    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if color_board[next_i][next_j] == 1:
        moving_horse = list(reversed(moving_horse))
    horse_board[next_i][next_j] += moving_horse
    
    for h in moving_horse:
        horse_info[h][0] = next_i
        horse_info[h][1] = next_j

    if len(horse_board[next_i][next_j]) > 3:
        print(answer)
        exit()

move = [[0,1],[0,-1],[-1,0],[1,0]]
N, K = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
horse_board = [[[] for _ in range(N)] for _ in range(N)]
horse_info = [[]]

for k in range(1,K+1):
    I, J, D = map(int, input().split())
    horse_info.append([I-1,J-1,D-1])
    horse_board[I-1][J-1].append(k)

for t in range(1, 1001):
    for horse_num in range(1,K+1):
        horse_move(horse_num,t)

print(-1)