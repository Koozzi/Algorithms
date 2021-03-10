def get_shark(j):
    global N
    for i in range(N):
        if board[i][j]:
            value = board[i][j][2]
            board[i][j] = []
            return value

def next_location(i,j,shark):
    global N, M
    s,d,z = shark

    if d <= 2: s %= (2 * N - 2)
    else: s %= (2 * M - 2)

    for _ in range(s):
        if d == 1:
            if i == 0: d = 2
            i += move[d][0]
        elif d == 2:
            if i == N-1: d = 1
            i += move[d][0]
        elif d == 3:
            if j == M-1: d = 4
            j += move[d][1]
        elif d == 4:
            if j == 0: d = 3
            j += move[d][1]

    return i, j, d

def shark_move():
    global N, M
    new_board = [[[] for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if not board[i][j]: continue
            next_i, next_j, d = next_location(i,j,board[i][j])
            if new_board[next_i][next_j]:
                if new_board[next_i][next_j][2] < board[i][j][2]:
                    new_board[next_i][next_j] = board[i][j]
                    new_board[next_i][next_j][1] = d
            else:
                new_board[next_i][next_j] = board[i][j]
                new_board[next_i][next_j][1] = d
                
    return new_board

move = [[],[-1,0],[1,0],[0,1],[0,-1]]
N, M, S = map(int, input().split())
board = [[[] for j in range(M)] for i in range(N)]

for num in range(S):
    i, j, s, d, z = map(int, input().split())
    board[i-1][j-1] = [s,d,z]

answer = 0
for j in range(M):
    value = get_shark(j)
    if value: answer += value
    board = shark_move()

print(answer)