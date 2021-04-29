'''
시작 14:32
제출 14:52
종료
'''

spread_sand = [
    [[-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02]],
    [[0,-2,0.02],[-1,-1,0.01],[0,-1,0.07],[1,-1,0.1],[2,0,0.05],[-1,1,0.01],[0,1,0.07],[1,1,0.1],[0,2,0.02]],
    [[-2,0,0.02],[-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],[0,2,0.05],[1,-1,0.01],[1,0,0.07],[1,1,0.1],[2,0,0.02]],
    [[0,-2,0.02],[-1,-1,0.1],[0,-1,0.07],[1,-1,0.01],[-2,0,0.05],[-1,1,0.1],[0,1,0.07],[1,1,0.01],[0,2,0.02]]
]

def change_direction(I,J,D):
    init_i, init_j = N//2, N//2

    if I+J == N-1 and I != J \
        or I == J and I > init_i and J > init_j \
            or I == J+1 and I <= init_i and J < init_j:
            return (D + 1) % 4
    
    return D

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[0,-1],[1,0],[0,1],[-1,0]]
out_of_board_sand_amount = 0
I, J, D = N//2, N//2, 0
while True:

    I += move[D][0]
    J += move[D][1]

    init_sand_amount = board[I][J]
    current_sand_sum = 0

    for di, dj, rate in spread_sand[D]:
        next_i = I + di
        next_j = J + dj

        spread_sand_amount = int(init_sand_amount * rate)
        current_sand_sum += spread_sand_amount

        if 0 <= next_i < N and 0 <= next_j < N:
            board[next_i][next_j] += spread_sand_amount
        else:
            out_of_board_sand_amount += spread_sand_amount

    # alpha자리에 넘겨줄 모래의 양을 구하자
    # 만약에 alpha자리가 격자 밖으로 나가는 경우에는 무시하고
    # out_of_board_sand_amound에 더해줌
    sand_left = init_sand_amount - current_sand_sum
    board[I][J] = 0

    alpha_i = I + move[D][0]
    alpha_j = J + move[D][1]

    if 0 <= alpha_i < N and 0 <= alpha_j < N:
        board[alpha_i][alpha_j] += sand_left
    else:
        out_of_board_sand_amount += sand_left

    if I == 0 and J == 0:
        break

    D = change_direction(I,J,D)

print(out_of_board_sand_amount)