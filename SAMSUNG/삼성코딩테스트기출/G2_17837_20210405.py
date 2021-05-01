'''
시작 11:36
제출 13:16
종료 
'''

def move_horse(horse_num):

    I,J,D = horse_info[horse_num]
    
    idx = horse_board[I][J].index(horse_num)
    moving_horse = horse_board[I][J][idx:]
    horse_board[I][J] = horse_board[I][J][:idx]

    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if color_board[next_i][next_j] == 1:
        moving_horse = list(reversed(moving_horse))
    horse_board[next_i][next_j] += moving_horse

    for h in moving_horse:
        horse_info[h][0] = next_i
        horse_info[h][1] = next_j

    if len(horse_board[next_i][next_j]) > 3:
        print(t)
        exit()

def change_direction(D):
    if D == 0: D = 1
    elif D == 1: D = 0
    elif D == 2: D = 3
    elif D == 3: D = 2
    return D

def solve(horse_num):

    I,J,D = horse_info[horse_num]

    if 0 <= I+move[D][0] < N and 0 <= J+move[D][1] < N:
        if color_board[I+move[D][0]][J+move[D][1]] == 2:
            D = change_direction(D)
            horse_info[horse_num][2] = D
    else:
        D = change_direction(D)
        horse_info[horse_num][2] = D

    if 0 <= I + move[D][0] < N and 0 <= J + move[D][1] < N:
        if color_board[I+move[D][0]][J+move[D][1]] != 2:
            move_horse(horse_num)

move = [[0,1],[0,-1],[-1,0],[1,0]]
N, M = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
horse_board = [[[] for _ in range(N)] for _ in range(N)]

horse_info = [[]]
for horse_num in range(1,M+1):
    I,J,D = map(int, input().split())
    horse_info.append([I-1,J-1,D-1])
    horse_board[I-1][J-1].append(horse_num)

for t in range(1, 1001):
    for horse_num in range(1,M+1):
        solve(horse_num)

print(-1)