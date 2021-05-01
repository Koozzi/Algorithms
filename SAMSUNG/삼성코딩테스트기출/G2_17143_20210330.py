# 15:38
# 15:36
#

def get_nearest_shark(idx):
    global answer

    for i in range(N):
        if board[i][j]:
            answer += board[i][j][2]
            board[i][idx] = []
            break

def next_locationn(I,J,shark):
    speed, direction, size = shark
    if direction == 0 or direction == 1:
        speed = speed % ((N-1)*2)
        for _ in range(speed):
            if I == N-1: direction = 0
            elif I == 0: direction = 1
            I += move[direction][0]

    elif direction == 2 or direction == 3:
        speed = speed % ((M-1)*2)
        for _ in range(speed):
            if J == M-1: direction = 3
            elif J == 0: direction = 2
            J += move[direction][1]

    return I, J, direction

def shark_move():
    new_board = [[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                next_i, next_j, next_d = next_locationn(i,j,board[i][j])
                board[i][j][1] = next_d
                if not new_board[next_i][next_j]:
                    new_board[next_i][next_j] = board[i][j]
                elif new_board[next_i][next_j]:
                    if new_board[next_i][next_j][2] < board[i][j][2]:
                        new_board[next_i][next_j] = board[i][j]

    return new_board

if __name__=="__main__":
    answer = 0
    move = [[-1,0],[1,0],[0,1],[0,-1]] 
    N, M, S = map(int, input().split())
    board = [[[] for _ in range(M)] for _ in range(N)]
    for _ in range(S):
        I, J, S, D, Z = map(int, input().split())
        board[I-1][J-1] = [S,D-1,Z]

    for j in range(M):
        get_nearest_shark(j)
        board = shark_move()
    
    print(answer)