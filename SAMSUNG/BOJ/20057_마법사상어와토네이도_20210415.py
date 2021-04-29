spread_sand = [
    [[-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02]],
    [[0,-2,0.02],[-1,-1,0.01],[0,-1,0.07],[1,-1,0.1],[2,0,0.05],[-1,1,0.01],[0,1,0.07],[1,1,0.1],[0,2,0.02]],
    [[-2,0,0.02],[-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],[0,2,0.05],[1,-1,0.01],[1,0,0.07],[1,1,0.1],[2,0,0.02]],
    [[0,-2,0.02],[-1,-1,0.1],[0,-1,0.07],[1,-1,0.01],[-2,0,0.05],[-1,1,0.1],[0,1,0.07],[1,1,0.01],[0,2,0.02]]
]


def change_direction_point(i, j):
    if (i == j and i > N//2 and j > N//2) or (i + j == N-1 and i != j) or (j+1 == i and i <= N//2 and j < N//2):
        return True
    return False


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]

i, j, d = N//2, N//2, 0
spread_sand_out = 0

while True:
    i += move[d][0]
    j += move[d][1]

    current_sand_amount = board[i][j]
    board[i][j] = 0
    spread_sand_amount = 0
    for di, dj, rate in spread_sand[d]:
        current_spread_amount = int(current_sand_amount * rate)
        spread_sand_amount += current_spread_amount

        next_i = i + di
        next_j = j + dj

        if 0 <= next_i < N and 0 <= next_j < N:
            board[next_i][next_j] += current_spread_amount
        else:
            spread_sand_out += current_spread_amount

    current_sand_amount -= spread_sand_amount

    alpha_i = i + move[d][0]
    alpha_j = j + move[d][1]

    if 0 <= alpha_i < N and 0 <= alpha_j < N:
        board[alpha_i][alpha_j] += current_sand_amount
    else:
        spread_sand_out += current_sand_amount

    if change_direction_point(i, j):
        d = (d + 1) % 4

    if i == 0 and j == 0:
        break

print(spread_sand_out)