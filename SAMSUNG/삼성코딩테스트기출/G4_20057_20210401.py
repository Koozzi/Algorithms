
'''
18:15
19:15
'''

sand = [
    [(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),(-1,-1,0.1),(1,-1,0.1),(0,-2,0.05)], 
    [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(2,0,0.05)],
    [(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),(-1,1,0.1),(1,1,0.1),(0,2,0.05)],
    [(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),(-2,0,0.05),(0,-2,0.02),(0,2,0.02)]
]

def spread_sand(I,J,D):
    global answer

    init_sand = board[I][J]
    for di, dj, per in sand[D]:
        next_i = I + di
        next_j = J + dj
        next_sand = int(init_sand * per)
        board[I][J] -= next_sand
        
        if 0 <= next_i < N and 0 <= next_j < N:
            board[next_i][next_j] += next_sand
        else:
            answer += next_sand
    
    alpha_i, alpha_j = I+move[D][0], J+move[D][1]
    if 0 <= alpha_i < N and 0 <= alpha_j < N:
        board[alpha_i][alpha_j] += board[I][J]
    else:
        answer += board[I][J]

    board[I][J] = 0
    

answer = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[0,-1],[1,0],[0,1],[-1,0]]
I, J, D = N // 2, N // 2, 0

move_cnt = 1
while True:
    for _ in range(2):
        for t in range(move_cnt):
            I += move[D][0]
            J += move[D][1]  
            spread_sand(I,J,D)
            if I == 0 and J == 0:
                print(answer)
                exit()
        D = (D + 1) % 4
    move_cnt += 1