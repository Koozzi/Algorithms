# 12:36
#
#

def change_horse_direction(D):
    if D == 0: D = 1
    elif D == 1: D = 0
    elif D == 2: D = 3
    elif D == 3: D = 2
    return D

def single_move_shark(horse_num,I,J,next_i,next_j,color,answer):
    idx = horse_chess[I][J].index(horse_num)
    moving_horses = horse_chess[I][J][idx:]
    horse_chess[I][J] = horse_chess[I][J][:idx]

    if color == 1:
        moving_horses = list(reversed(moving_horses))

    horse_chess[next_i][next_j] += moving_horses
    for H in moving_horses:
        horse_info[H][0], horse_info[H][1] = next_i, next_j 

    if len(horse_chess[next_i][next_j]) > 3:
        print(answer)
        exit()

def total_move_horse(horse_num, answer):
    I,J,D = horse_info[horse_num]

    if 0 <= I+move[D][0] < N and 0 <= J+move[D][1] < N:
        if board[I+move[D][0]][J+move[D][1]] == 2:
            D = change_horse_direction(D)
            horse_info[horse_num][2] = D
    else:
        D = change_horse_direction(D)
        horse_info[horse_num][2] = D            

    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if 0 <= next_i < N and 0 <= next_j < N:
        if board[next_i][next_j] != 2: 
            single_move_shark(horse_num,I,J,next_i,next_j,board[next_i][next_j],answer)

if __name__=="__main__":
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [[0,1],[0,-1],[-1,0],[1,0]]
    horse_chess = [[[] for _ in range(N)] for _ in range(N)]
    
    horse_info = []
    for horse_num in range(K):
        I, J, D = map(int, input().split())
        horse_chess[I-1][J-1].append(horse_num)
        horse_info.append([I-1, J-1, D-1])
    
    for t in range(1, 1001):
        for horse_num in range(K):
            total_move_horse(horse_num, t)

    print(-1)