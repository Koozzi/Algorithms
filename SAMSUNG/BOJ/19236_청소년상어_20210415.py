from copy import deepcopy


def fish_move():
    for fish_num in range(1, 17):
        i, j, d, l = fish_info[fish_num]
        if not l: continue

        next_i = i + move[d][0]
        next_j = j + move[d][1]

        for _ in range(8):
            if 0 <= next_i < 4 and 0 <= next_j < 4:
                if fish_board[next_i][next_j][0] != -1:
                    if fish_board[next_i][next_j][0] > 0:
                        next_fish_num, next_fish_dir = fish_board[next_i][next_j]
                        fish_board[i][j] = [next_fish_num, next_fish_dir]
                        fish_board[next_i][next_j] = [fish_num, d]
                        fish_info[fish_num][0], fish_info[fish_num][1] = next_i, next_j
                        fish_info[next_fish_num][0], fish_info[next_fish_num][1] = i, j
                        break

                    elif fish_board[next_i][next_j][0] == 0:
                        fish_board[i][j] = [0, 0]
                        fish_board[next_i][next_j] = [fish_num, d]
                        fish_info[fish_num][0], fish_info[fish_num][1] = next_i, next_j
                        break

            d = (d + 1) % 8
            fish_info[fish_num][2] = d
            next_i = i + move[d][0]
            next_j = j + move[d][1]


def get_shark_can_eat():
    shark_can_eat = []
    I, J = shark_i, shark_j
    while True:
        I += move[shark_d][0]
        J += move[shark_d][1]

        if not 0 <= I < 4 or not 0 <= J < 4:
            break

        if fish_board[I][J][0] > 0:
            shark_can_eat.append([I, J])

    return shark_can_eat


def solve(shark_eat_sum):
    global answer, fish_board, fish_info, shark_i, shark_j, shark_d

    answer = max(answer, shark_eat_sum)

    fish_move()
    shark_can_eat = get_shark_can_eat()

    if not shark_can_eat:
        return

    for fish_i, fish_j in shark_can_eat:
        copied_fish_board = deepcopy(fish_board)
        copied_fish_info = deepcopy(fish_info)
        copied_shark_i, copied_shark_j, copied_shark_d = shark_i, shark_j, shark_d

        fish_num, fish_dir = fish_board[fish_i][fish_j]
        fish_info[fish_num][3] = False
        fish_board[shark_i][shark_j] = [0, 0]
        shark_i, shark_j, shark_d = fish_i, fish_j, fish_dir
        fish_board[shark_i][shark_j] = [-1, shark_d]

        solve(shark_eat_sum + fish_num)

        fish_board = copied_fish_board
        fish_info = copied_fish_info
        shark_i, shark_j, shark_d = copied_shark_i, copied_shark_j, copied_shark_d



move = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fish_board = [[[0, 0] for _ in range(4)] for _ in range(4)]
fish_info = [[0, 0, 0, False] for _ in range(17)]

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        fish_num, fish_dir = row[j*2], row[j*2+1]
        fish_board[i][j] = [fish_num, fish_dir-1]
        fish_info[fish_num] = [i, j, fish_dir-1, True]

first_fish_num, first_fish_dir = fish_board[0][0]
shark_i, shark_j, shark_d = 0, 0, first_fish_dir
fish_info[first_fish_num][3] = False
fish_board[shark_i][shark_j][0] = -1
answer = first_fish_num

solve(first_fish_num)

print(answer)