'''
15:00
15:15
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
pipe = [[[0,0,0] for _ in range(N)] for _ in range(N)]

pipe[0][1][0] = 1
for j in range(2, N):
    if board[0][j] == 0:
        pipe[0][j][0] = pipe[0][j-1][0]

for i in range(1, N):
    for j in range(2, N):
        if board[i][j] == 0:
            pipe[i][j][0] = pipe[i][j-1][0] + pipe[i][j-1][2]
            pipe[i][j][1] = pipe[i-1][j][1] + pipe[i-1][j][2]
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            pipe[i][j][2] = sum(pipe[i-1][j-1])

print(sum(pipe[N-1][N-1]))