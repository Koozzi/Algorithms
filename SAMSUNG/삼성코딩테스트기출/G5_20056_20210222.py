from copy import deepcopy

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for i in range(M)]
board = [[[]for j in range(N)] for i in range(N)]

for fireball in fireballs:
    i,j,m,s,d = fireball
    board[i-1][j-1].append([m,s,d])

move_dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

for k in range(K):
    new_board_move = [[[]for j in range(N)] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for info in board[i][j]:
                    m,s,d = info
                    next_i, next_j = (i + s * move_dir[d][0]) % N, (j + s * move_dir[d][1]) % N
                    new_board_move[next_i][next_j].append([m,s,d])

    new_board_make = [[[]for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if len(new_board_move[i][j]) > 1:
                total_m, total_s, total_cnt = 0, 0, len(new_board_move[i][j])
                for info in new_board_move[i][j]:
                    m,s,d = info
                    total_m += m
                    total_s += s

                direction_check = True
                for idx in range(1,total_cnt):
                    if new_board_move[i][j][idx][2] % 2 != new_board_move[i][j][idx-1][2] % 2:
                        direction_check = False
                        break

                direction = [0,0,0,0]
                if direction_check: direction = [0,2,4,6]
                else: direction = [1,3,5,7]

                new_m = total_m // 5
                new_s = total_s // total_cnt

                if new_m != 0:
                    for d in range(4):
                        new_d = direction[d]
                        new_board_make[i][j].append([new_m, new_s, new_d])
            
            if len(new_board_move[i][j]) == 1:
                new_board_make[i][j].append(new_board_move[i][j][0])
    
    board = deepcopy(new_board_make)

answer = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for fireball in board[i][j]:
                answer += fireball[0]

print(answer)