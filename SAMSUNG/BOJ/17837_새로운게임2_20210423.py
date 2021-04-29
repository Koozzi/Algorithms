def change_direction(D):
    if D == 1: return 2
    elif D == 2: return 1
    elif D == 3: return 4
    elif D == 4: return 3


def horse_move(horse_num, t):

    i, j, d = horse_info[horse_num]
    horse_index = horse_board[i][j].index(horse_num)
    moving_horse = horse_board[i][j][horse_index:]

    # print("current horse infomation")
    # print("horse number        : ", horse_num)
    # print("index and direction : ", i, j, d)
    # print("current horse board")
    # for b in horse_board:
    #     print(b)

    next_i = i + move[d][0]
    next_j = j + move[d][1]

    if 0 <= next_i < N and 0 <= next_j < N:
        if color_board[next_i][next_j] != 2:
            horse_board[i][j] = horse_board[i][j][:horse_index]
            if color_board[next_i][next_j] == 1:
                moving_horse = list(reversed(moving_horse))
            horse_board[next_i][next_j] += moving_horse

            if len(horse_board[next_i][next_j]) > 3:
                print(t)
                exit()

            for h in horse_board[next_i][next_j]:
                horse_info[h][0] = next_i
                horse_info[h][1] = next_j
    #
    # else:
    #     print("can't move !! ")


def solve(t):
    for horse_num in range(1, K + 1):
        i, j, d = horse_info[horse_num]

        next_i = i + move[d][0]
        next_j = j + move[d][1]

        if 0 <= next_i < N and 0 <= next_j < N:
            if color_board[next_i][next_j] == 2:
                d = change_direction(d)
                horse_info[horse_num][2] = d
        else:
            d = change_direction(d)
            horse_info[horse_num][2] = d

        horse_move(horse_num, t)


move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
N, K = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
horse_board = [[[] for _ in range(N)] for _ in range(N)]
horse_info = [[]]

for horse_num in range(1, K + 1):
    i, j, d = map(int, input().split())
    horse_board[i-1][j-1].append(horse_num)
    horse_info.append([i-1, j-1, d])

answer = -1
for t in range(1, 1001):
    solve(t)
    pass

print(answer)
