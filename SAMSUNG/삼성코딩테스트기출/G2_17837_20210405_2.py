
def change_direction(D):
    if D == 0: return 1
    elif D == 1: return 0
    elif D == 2: return 3
    elif D == 3: return 2

def horse_move(horse_num):
    
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

def solve(horse_num):
    
    I,J,D = horse_info[horse_num]

    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if 0 <= next_i < N and 0 <= next_j < N:
        if color_board[next_i][next_j] == 2:
            D = change_direction(D)
            horse_info[horse_num][2] = D
    else:
        D = change_direction(D)
        horse_info[horse_num][2] = D
    
    next_i = I + move[D][0]
    next_j = J + move[D][1]

    if 0 <= next_i < N and 0 <= next_j < N:
        if color_board[next_i][next_j] != 2:
            horse_move(horse_num)

move = [[0,1],[0,-1],[-1,0],[1,0]]
N, M = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
horse_board = [[[] for _ in range(N)] for _ in range(N)]
horse_info = [[]]
for num in range(1,M+1):
    I,J,D = map(int, input().split())
    horse_board[I-1][J-1].append(num)
    horse_info.append([I-1, J-1, D-1])

for t in range(1,1001):
    for num in range(1,M+1):
        solve(num)

print(-1)