'''
시작 16:13
제출 16:24
종료
'''

def shark_move():
    new_board = [[[0,0,0] for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != [0,0,0]:
                speed, direction, size = board[i][j]

                if direction <= 2: speed %= (N-1)*2
                elif direction > 2: speed %= (M-1)*2

                next_i, next_j = i, j

                for _ in range(speed):
                    if direction <= 2:
                        if next_i == N-1: direction = 1
                        elif next_i == 0: direction = 2
                    elif direction > 2:
                        if next_j == M-1: direction = 4
                        elif next_j == 0: direction = 3
                    next_i += move[direction][0]
                    next_j += move[direction][1]
                
                if size > new_board[next_i][next_j][2]:
                    new_board[next_i][next_j] = [speed, direction, size]

    return new_board

def get_nearest_shark(j):
    global answer

    for i in range(N):
        if board[i][j] != [0,0,0]:
            answer += board[i][j][2]
            board[i][j] = [0,0,0]
            break

answer = 0
move = [[],[-1,0],[1,0],[0,1],[0,-1]]
N, M, K = map(int, input().split())
board = [[[0,0,0] for _ in range(M)] for _ in range(N)]
for _ in range(K):
    I, J, S, D, Z = map(int, input().split())
    board[I-1][J-1] = [S, D, Z]

for j in range(M):
    get_nearest_shark(j)
    board = shark_move()

print(answer)