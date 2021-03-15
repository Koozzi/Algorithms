def fireball_sum_divide(tmp_board):
    global N
    final_board = [[[] for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if len(tmp_board[i][j]) > 1:
                
                _M, _S = 0, 0

                for M, S, D in tmp_board[i][j]:
                    _M += M
                    _S += S

                _M //= 5
                _S //= len(tmp_board[i][j])

                direction_check = True
                for k in range(1, len(tmp_board[i][j])):
                    if tmp_board[i][j][k-1][2] % 2 != tmp_board[i][j][k][2] % 2:
                        direction_check = False
                        break
                
                D_list = []
                if direction_check: D_list = [0, 2, 4, 6]
                else: D_list = [1, 3, 5, 7]

                if _M != 0:
                    for _D in D_list:
                        final_board[i][j].append([_M, _S, _D])

            elif len(tmp_board[i][j]) == 1:
                final_board[i][j].append(tmp_board[i][j][0])

    return final_board

def fireball_move():
    global N

    tmp_board = [[[] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if not board[i][j]: continue
            for M, S, D in board[i][j]:
                next_i = (i + S * move[D][0]) % N
                next_j = (j + S * move[D][1]) % N
                tmp_board[next_i][next_j].append([M,S,D])

    return fireball_sum_divide(tmp_board)
    
N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for i in range(M)]
board = [[[] for j in range(N)] for i in range(N)]
move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

for I, J, M, S, D in fireball:
    board[I-1][J-1].append([M,S,D])

for _ in range(K):
    board = fireball_move()

answer = 0
for i in range(N):
    for j in range(N):
        for M,S,D in board[i][j]:
            answer += M

print(answer)