move_sand =[
    [(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),(-1,-1,0.1),(1,-1,0.1),(0,-2,0.05)],
    [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(2,0,0.05)],
    [(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),(-1,1,0.1),(1,1,0.1),(0,2,0.05)],
    [(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),(-2,0,0.05),(0,-2,0.02),(0,2,0.02)]
]
move_alpha = [[0,-1],[1,0],[0,1],[-1,0]]

def solve(I,J,D):
    global N, board, answer
    if board[I][J] < 1: return

    v = []
    for m in move_sand[D]:
        v.append(int(board[I][J] * m[2]))

    for idx, m in enumerate(move_sand[D]):
        i,j = I+m[0], J+m[1]
        if 0 <= i < N and 0 <= j < N:
            board[i][j] += v[idx]
        else:
            answer += v[idx]
        board[I][J] -= v[idx]
    
    alpha_i, alpha_j = I + move_alpha[D][0], J + move_alpha[D][1]
    if 0 <= alpha_i < N and 0 <= alpha_j < N:
        board[alpha_i][alpha_j] += board[I][J]
    else:
        answer += board[I][J]
    board[I][J] = 0       
            
            
N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
move_dir = [[0,-1],[1,0],[0,1],[-1,0]]
answer, I, J, D = 0, N//2, N//2, 0
while True:

    if I == 0 and J == 0:
        break

    I, J = I + move_dir[D][0], J + move_dir[D][1]

    solve(I,J,D) 

    if I+J == N-1 and I != J:
        D = (D + 1) % 4
    elif I == J and I > N//2 and J > N//2:
        D = (D + 1) % 4
    elif (I-1) == J and I-1 < N//2 and J < N//2:
        D = (D + 1) % 4

print(answer)