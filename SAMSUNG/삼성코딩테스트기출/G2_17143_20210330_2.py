# 23:12
# 23:50
# 오타 조심

def get_nearest_shark(idx):
    global answer
    for i in range(N):
        if board[i][idx]:
            answer += board[i][idx][2]
            board[i][idx] = []
            break

def next_location(shark_i,shark_j,shark):
    speed, direction, size = shark

    if direction == 0 or direction == 1:
        speed %= (N-1)*2
        for _ in range(speed):
            if shark_i == N-1: direction = 0
            elif shark_i == 0: direction = 1
            shark_i += move[direction][0]

    elif direction == 2 or direction == 3:
        speed %= (M-1)*2
        for _ in range(speed):
            if shark_j == M-1: direction = 3
            elif shark_j == 0: direction = 2
            shark_j += move[direction][1]
    
    return shark_i, shark_j, direction

def shark_move():
    new_board = [[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                next_i, next_j, board[i][j][1] = next_location(i,j,board[i][j])
                if new_board[next_i][next_j]:
                    if new_board[next_i][next_j][2] < board[i][j][2]:
                        new_board[next_i][next_j] = board[i][j]
                elif not new_board[next_i][next_j]:
                    new_board[next_i][next_j] = board[i][j]

    return new_board

if __name__=="__main__":
    answer = 0
    N, M, K = map(int, input().split())
    move = [[-1,0],[1,0],[0,1],[0,-1]]
    board = [[[] for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        I, J, S, D, Z = map(int, input().split())
        board[I-1][J-1] = [S,D-1,Z]
    
    for j in range(M):
        get_nearest_shark(j)
        board = shark_move()    
    
    print(answer)