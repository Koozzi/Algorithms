def change_direction(D):
    if D == 0: return 1
    elif D == 1: return 0
    elif D == 2: return 3
    elif D == 3: return 2

def move_horse(k,I,J,next_i,next_j,color):
    l = board_horse[I][J]
    idx = l.index(k)
    moveing_horse = l[idx:]
    board_horse[I][J] = l[:idx]
    if color == 1: moveing_horse.reverse()
    board_horse[next_i][next_j] += moveing_horse
    for h in moveing_horse:
        horse_info[h][1], horse_info[h][2] = next_i, next_j

N, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
board_horse = [[[] for j in range(N)] for i in range(N)]
move = [[0,1],[0,-1],[-1,0],[1,0]]
horse_info = []
answer = -1

for k in range(K):
    I, J, D = map(int, input().split())
    horse_info.append([k,I-1,J-1,D-1])
    board_horse[I-1][J-1].append(k) 

for t in range(1,1001):
    for k,I,J,D in horse_info:

        next_i, next_j = I + move[D][0], J + move[D][1]
        if not 0 <= next_i < N or not 0 <= next_j < N:
            horse_info[k][3] = D = change_direction(D)
            next_i, next_j = I + move[D][0], J + move[D][1]
            if not 0 <= next_i < N or not 0 <= next_j < N: continue
            if board[next_i][next_j] == 2: continue
            else: move_horse(k,I,J,next_i,next_j,board[next_i][next_j])

        elif board[next_i][next_j] == 2:
            horse_info[k][3] = D = change_direction(D)
            next_i, next_j = I + move[D][0], J + move[D][1]            
            if not 0 <= next_i < N or not 0 <= next_j < N: continue
            if board[next_i][next_j] == 2: continue
            else: move_horse(k,I,J,next_i,next_j,board[next_i][next_j])
        else:
            move_horse(k,I,J,next_i,next_j,board[next_i][next_j])
    
        if len(board_horse[next_i][next_j]) >= 4:
            answer = t
            break
    
    if answer != -1:
        break

print(answer)