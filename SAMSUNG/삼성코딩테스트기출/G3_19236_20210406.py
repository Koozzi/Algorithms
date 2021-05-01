'''
시작 12:06
제출 12:53
종료
'''

from copy import deepcopy

def get_next_location(shark_i, shark_j, shark_d):
    next_location = []

    while True:
        shark_i += move[shark_d][0]
        shark_j += move[shark_d][1]

        if not 0 <= shark_i < 4 or not 0 <= shark_j < 4:
            break

        if board[shark_i][shark_j][0] == 0:
            continue
        next_location.append([shark_i, shark_j])

    return next_location

def fish_move():
    for fish_num in range(1, 17):
        I,J,D,L = fish_info[fish_num]
        if not L: continue

        for _ in range(8):
            next_i = I + move[D][0]
            next_j = J + move[D][1]

            if not 0 <= next_i < 4 or not 0 <= next_j < 4:
                D = (D + 1) % 8
                continue

            # 상어가 있는 자리로는 이동할 수 없다.
            if board[next_i][next_j][0] == -1:
                D = (D + 1) % 8
                continue

            # 빈칸으로는 이동할 수 있다.
            if board[next_i][next_j][0] == 0:
                fish_info[fish_num] = [next_i, next_j, D, True]
                board[next_i][next_j] = [fish_num, D]
                board[I][J] = [0,0]
                break

            # 다른 물고기와 위치를 교환할 수 있다.
            elif 0 < board[next_i][next_j][0]:
                next_fish_num, next_fish_dir = board[next_i][next_j]
                board[next_i][next_j] = [fish_num, D]
                board[I][J] = [next_fish_num, next_fish_dir]
                fish_info[fish_num] = [next_i, next_j, D, True]
                fish_info[next_fish_num] = [I, J, next_fish_dir, True]
                break

def solve(fish_num_sum):
    global board, fish_info, answer, shark_i, shark_j, shark_d
    
    answer = max(answer, fish_num_sum)

    fish_move()
    next_location = get_next_location(shark_i, shark_j, shark_d)
    
    for next_i, next_j in next_location:
        copied_board, copied_fish_info = deepcopy(board), deepcopy(fish_info)
        init_i, init_j, init_d = shark_i, shark_j, shark_d

        next_fish_num, next_fish_dir = board[next_i][next_j]
        fish_info[next_fish_num][3] = False
        board[next_i][next_j] = [-1, next_fish_dir]
        board[shark_i][shark_j] = [0,0]
        shark_i, shark_j, shark_d = next_i, next_j, next_fish_dir

        solve(fish_num_sum + next_fish_num)

        board, fish_info = copied_board, copied_fish_info
        shark_i, shark_j, shark_d = init_i, init_j, init_d

move = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
board = [[[0,0] for _ in range(4)] for _ in range(4)]
fish_info = [[] for _ in range(17)]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0,8,2):
        num, direction = row[j], row[j+1]
        fish_info[num] = [i,j//2,direction-1,True]
        board[i][j//2] = [num, direction-1]

first_fish_num, first_fish_dir = board[0][0]
fish_info[first_fish_num][3] = False
board[0][0] = [-1, first_fish_dir]
shark_i, shark_j, shark_d = 0, 0, first_fish_dir
answer = first_fish_num
solve(first_fish_num)
print(answer)