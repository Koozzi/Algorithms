from copy import deepcopy


def fish_move(): # fish_info != fish_info[1:]
    # for fish_num, fish in enumerate(fish_info[1:], start=1):
        # i, j, l = fish

    for fish_num in range(1, 17):
        i, j, l = fish_info[fish_num]

        if not l: continue

        d = board[i][j][1]
        for _ in range(8):
            next_i = i + move[d][0]
            next_j = j + move[d][1]
            if 0 <= next_i < 4 and 0 <= next_j < 4:
                # 빈 칸으로 가는 경우
                if board[next_i][next_j][0] == 0:
                    board[i][j] = [0, 0]
                    board[next_i][next_j] = [fish_num, d]
                    fish_info[fish_num] = [next_i, next_j, True]
                    break
                # 다른 물고기와 자리는 바꾸는 경우
                elif board[next_i][next_j][0] > 0:
                    next_fish_num, next_d = board[next_i][next_j]
                    board[next_i][next_j] = [fish_num, d]
                    board[i][j] = [next_fish_num, next_d]
                    fish_info[next_fish_num] = [i, j, True]
                    fish_info[fish_num] = [next_i, next_j, True]
                    break
            d = (d + 1) % 8

        # print(fish_num, "After fish move")
        # for i in board:
        #     print(i)


def get_shark_can_eat():
    shark_can_eat = []
    i, j, d = shark_i, shark_j, shark_d
    while True:
        i += move[d][0]
        j += move[d][1]

        if not 0 <= i < 4 or not 0 <= j < 4:
            break

        if board[i][j][0] > 0:
            shark_can_eat.append([i, j])

    return shark_can_eat


def solve(fish_sum):
    global answer, board, fish_info, shark_i, shark_j, shark_d

    answer = max(answer, fish_sum)

    fish_move()
    shark_can_eat = get_shark_can_eat()

    if not shark_can_eat:
        return

    # print("Current shark locaion", shark_i, shark_j, shark_d)
    # for i, j in shark_can_eat:
    #     print(i, j, board[i][j])
    # print()
    for fish_i, fish_j in shark_can_eat:
        copied_board = deepcopy(board)
        copied_fish_info = deepcopy(fish_info)
        copied_shark_i, copied_shark_j, copied_shark_d = shark_i, shark_j, shark_d

        fish_num, fish_dir = board[fish_i][fish_j]
        fish_info[fish_num][2] = False
        board[shark_i][shark_j] = [0, 0]
        shark_i, shark_j, shark_d = fish_i, fish_j, fish_dir
        board[shark_i][shark_j] = [-1, shark_d]

        solve(fish_sum + fish_num)

        board = copied_board
        fish_info = copied_fish_info
        shark_i, shark_j, shark_d = copied_shark_i, copied_shark_j, copied_shark_d


fish_info = [[0, 0, False] for _ in range(17)]
board = [[[0, 0] for _ in range(4)] for _ in range(4)]
move = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [row[j*2], row[j*2+1]-1]
        fish_info[row[j*2]] = [i, j, True]

first_fish_num, first_fish_dir = board[0][0]
shark_i, shark_j, shark_d = 0, 0, first_fish_dir
fish_info[first_fish_num][2] = False
board[shark_i][shark_j] = [-1, shark_d]
answer = first_fish_num
# fish_move()
solve(first_fish_num)
print(answer)

"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
33
"""