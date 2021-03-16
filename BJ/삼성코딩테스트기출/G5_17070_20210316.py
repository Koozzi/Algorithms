N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
pipe = [[[0,0,0] for j in range(N)] for i in range(N)]

pipe[0][1][0] = 1
for j in range(2, N):
    if board[0][j] == 1: break
    pipe[0][j][0] = pipe[0][j-1][0]

for i in range(1, N):
    for j in range(2, N):
        if board[i][j] == board[i][j-1] == board[i-1][j] == 0:
            pipe[i][j][2] = sum(pipe[i-1][j-1])
        if board[i][j] == 0:
            pipe[i][j][0] = pipe[i][j-1][0] + pipe[i][j-1][2]
            pipe[i][j][1] = pipe[i-1][j][1] + pipe[i-1][j][2]

print(sum(pipe[N-1][N-1]))