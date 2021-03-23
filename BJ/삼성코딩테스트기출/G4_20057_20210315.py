def neet_to_change(I, J):
    global N
    if I == J and I > N//2 and J > N//2: return True
    if I == J+1 and I <= N //2 and J < N//2: return True
    if I + J == N-1 and I != J: return True
    return False
spread_sand = [
    [(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),(-1,-1,0.1),(1,-1,0.1),(0,-2,0.05)], 
    [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(2,0,0.05)],
    [(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),(-1,1,0.1),(1,1,0.1),(0,2,0.05)],
    [(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),(-2,0,0.05),(0,-2,0.02),(0,2,0.02)]
]
move_dir = [[0,-1],[1,0],[0,1],[-1,0]]

N = int(input())
board = [ list(map(int, input().split())) for i in range(N) ]

I, J, D = N//2, N//2, 0

answer = 0
while True:

    if I == 0 and J == 0:
        break

    I += move_dir[D][0]
    J += move_dir[D][1] 

    if board[I][J] == 0:
        if neet_to_change(I, J):
            D = (D + 1) % 4
        continue

    sum_sand = 0
    for sand in spread_sand[D]:
        next_i = I + sand[0]
        next_j = J + sand[1]
        add_sand = int(board[I][J] * sand[2])
        
        sum_sand += add_sand
        if 0 <= next_i < N and 0 <= next_j < N:
            board[next_i][next_j] += add_sand
        else:
            answer += add_sand

    board[I][J] -= sum_sand

    alpha_i = I + move_dir[D][0]
    alpha_j = J + move_dir[D][1]
    if 0 <= alpha_i < N and 0 <= alpha_j < N:
        board[alpha_i][alpha_j] += board[I][J]
    else:
        answer += board[I][J]
    
    board[I][J] = 0

    if neet_to_change(I, J):
        D = (D + 1) % 4

print(answer)