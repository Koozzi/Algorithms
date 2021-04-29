from copy import deepcopy


def fish_move():
    for fish_num in range(1, 17):
        i, j, l = fish_info[fish_num]
        if not l: continue

        d = fish_board[i][j][1]

        for _ in range(8):
            next_i = i + move[d][0]
            next_j = j + move[d][1]
            if 0 <= next_i < 4 and 0 <= next_j < 4:
                if fish_board[next_i][next_j][0] > 0:
                    next_fish_num, next_fish_dir = fish_board[next_i][next_j]
                    fish_board[next_i][next_j] = [fish_num, d]
                    fish_board[i][j] = [next_fish_num, next_fish_dir]
                    fish_info[fish_num] = [next_i, next_j, True]
                    fish_info[next_fish_num] = [i, j, True]
                    break

                elif fish_board[next_i][next_j][0] == 0:
                    fish_board[i][j] = [0, 0]
                    fish_board[next_i][next_j] = [fish_num, d]
                    fish_info[fish_num] = [next_i, next_j, True]
                    break

            d = (d + 1) % 8

        # print(fish_num, "After fish move")
        # for f in fish_board:
        #     print(f)


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


def solve(fish_sum):
    global answer, fish_board, fish_info, shark_i, shark_j, shark_d

    answer = max(answer, fish_sum)

    fish_move()

    for fish_i, fish_j in get_shark_can_eat():
        copied_board = deepcopy(fish_board)
        copied_fish_info = deepcopy(fish_info)
        copied_i, copied_j, copied_d = shark_i, shark_j,shark_d

        fish_num, fish_dir = fish_board[fish_i][fish_j]
        fish_info[fish_num][2] = False
        fish_board[shark_i][shark_j] = [0, 0]
        shark_i, shark_j, shark_d = fish_i, fish_j, fish_dir
        fish_board[shark_i][shark_j] = [-1, shark_d]

        solve(fish_sum + fish_num)

        fish_board = copied_board
        fish_info = copied_fish_info
        shark_i, shark_j, shark_d = copied_i, copied_j, copied_d


fish_board = [[[0, 0] for _ in range(4)] for _ in range(4)]
fish_info = [[0, 0, True] for _ in range(17)]
move = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        fish_board[i][j] = [ row[j*2], row[j*2+1]-1 ]
        fish_info[row[j*2]] = [i, j, True]

first_fish_num, first_fish_dir = fish_board[0][0]
shark_i, shark_j, shark_d = 0, 0, first_fish_dir
fish_info[first_fish_num][2] = False
fish_board[shark_i][shark_j] = [-1, shark_d]
answer = first_fish_num
solve(first_fish_num)
print(answer)