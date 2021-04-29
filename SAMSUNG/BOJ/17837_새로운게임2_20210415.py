def change_direction(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3


def move_horse(horse_num, answer):
    i, j, d = horse_info[horse_num]

    horse_idx = horse_board[i][j].index(horse_num)
    moving_horse = horse_board[i][j][horse_idx:]
    horse_board[i][j] = horse_board[i][j][:horse_idx]

    next_i = i + move[d][0]
    next_j = j + move[d][1]

    if color_board[next_i][next_j] == 1:
        moving_horse = list(reversed(moving_horse))

    horse_board[next_i][next_j] += moving_horse

    if len(horse_board[next_i][next_j]) > 3:
        print(answer)
        exit()

    for h in moving_horse:
        horse_info[h][0] = next_i
        horse_info[h][1] = next_j


def total_horse_move(answer):

    for horse_num in range(1, K+1):
        i, j, d = horse_info[horse_num]

        next_i = i + move[d][0]
        next_j = j + move[d][1]

        if 0 <= next_i < N and 0 <= next_j < N:
            if color_board[next_i][next_j] == 2:
                d = change_direction(d)
        else: d = change_direction(d)
        horse_info[horse_num][2] = d

        next_i = i + move[d][0]
        next_j = j + move[d][1]

        if 0 <= next_i < N and 0 <= next_j < N:
            if color_board[next_i][next_j] != 2:
                move_horse(horse_num, answer)


N, K = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
horse_board = [[[] for _ in range(N)] for _ in range(N)]
horse_info = [[]]
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]

for horse_num in range(1, K+1):
    i, j, d = map(int, input().split())
    horse_board[i-1][j-1].append(horse_num)
    horse_info.append([i-1, j-1, d])

for t in range(1, 1001):
    total_horse_move(t)

print(-1)
