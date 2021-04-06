'''
시작 17:07
제출 17:52
종료
'''

spread_sand = [
    [[-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02]],
    [[0,-2,0.02],[-1,-1,0.01],[0,-1,0.07],[1,-1,0.1],[2,0,0.05],[-1,1,0.01],[0,1,0.07],[1,1,0.1],[0,2,0.02]],
    [[-2,0,0.02],[-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],[0,2,0.05],[1,-1,0.01],[1,0,0.07],[1,1,0.1],[2,0,0.02]],
    [[0,-2,0.02],[-1,-1,0.1],[0,-1,0.07],[1,-1,0.01],[-2,0,0.05],[-1,1,0.1],[0,1,0.07],[1,1,0.01],[0,2,0.02]]
]


def change_direction(center_i,center_j,I,J):

    if (I + J == N-1 and I != J) \
        or I == J and I > center_i and J > center_j \
            or I == J+1 and I <= center_i and J < center_j:
            return True

    return False

def start_move(I, J):
    global answer

    center_i,center_j = I,J
    
    D = 0
    while True:

        if I == 0 and J == 0:
            break

        init_i, init_j = I, J

        I += move[D][0]
        J += move[D][1]

        spread_sand_sum, spread_sand_out = 0, 0
        current_sand = board[I][J]

        for di, dj, rate in spread_sand[D]:
            next_i = I + di 
            next_j = J + dj   
            amount_spread_sand = int(current_sand * rate)
            spread_sand_sum += amount_spread_sand
            if not 0 <= next_i < N or not 0 <= next_j < N:
                spread_sand_out += amount_spread_sand
                continue
            board[next_i][next_j] += amount_spread_sand

        alpha_i = I + move[D][0]
        alpha_j = J + move[D][1]

        board[init_i][init_j] = 0
        if not 0 <= alpha_i < N or not 0 <= alpha_j < N:
            spread_sand_out += current_sand - spread_sand_sum
        else:
            board[alpha_i][alpha_j] += current_sand - spread_sand_sum

        if change_direction(center_i,center_j,I,J):
            D = (D + 1) % 4
            
        answer += spread_sand_out
        
N =  int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[0,-1],[1,0],[0,1],[-1,0]]
answer = 0
start_move(N//2, N//2)
print(answer)