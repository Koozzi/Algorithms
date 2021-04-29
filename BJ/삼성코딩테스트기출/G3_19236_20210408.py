'''
시작 15:07
제출 16:07
종료
'''

from copy import deepcopy

def fish_move():

    for num in range(1,17):
        
        I,J,D,L = fish_info[num]
        if not L: continue
        
        next_i, next_j = 0, 0
        for _ in range(8):
            next_i = I + move[D][0]
            next_j = J + move[D][1]

            if not 0 <= next_i < 4 or not 0 <= next_j < 4:
                D = (D + 1) % 8
                continue
            if fish_board[next_i][next_j] == -1:
                D = (D + 1) % 8
                continue

            break

        fish_info[num] = [next_i,next_j,D,True]
        next_fish_num = fish_board[next_i][next_j]

        if next_fish_num == 0:
            fish_board[I][J] = 0
            fish_board[next_i][next_j] = num
            fish_info[num] = [next_i, next_j, D, True]
        elif next_fish_num > 0:
            fish_info[num][:3] = [next_i,next_j,D]
            fish_info[next_fish_num][:2] = [I,J]
            fish_board[I][J] = next_fish_num
            fish_board[next_i][next_j] = num

def get_shark_can_ead(shark_i, shark_j, shark_d):
    shark_can_eat = []
    I, J = shark_i, shark_j
    while True:
        I += move[shark_d][0]
        J += move[shark_d][1]
        if not 0 <= I < 4 or not 0 <= J < 4:
            break
        if fish_board[I][J] > 0:
            fish_num = fish_board[I][J]
            fish_d = fish_info[fish_num][2]
            shark_can_eat.append([fish_num,I,J,fish_d])
    return shark_can_eat

def solve(fish_num_sum):
    global fish_info, fish_board, shark_i,shark_j, shark_d, answer

    fish_move()
    shark_can_eat = get_shark_can_ead(shark_i, shark_j, shark_d)
    
    if not shark_can_eat:
        answer = max(answer, fish_num_sum)
        return

    for next_fish_num, next_i, next_j, next_d in shark_can_eat:
        copied_fish_board = deepcopy(fish_board)
        copied_fish_info = deepcopy(fish_info)
        init_i, init_j, init_d = shark_i, shark_j, shark_d

        shark_i, shark_j, shark_d = next_i, next_j, next_d
        fish_info[next_fish_num][3] = False
        fish_board[init_i][init_j] = 0
        fish_board[next_i][next_j] = -1

        solve(fish_num_sum + next_fish_num)

        shark_i, shark_j, shark_d = init_i, init_j, init_d
        fish_board = copied_fish_board
        fish_info = copied_fish_info

move = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
fish_board = [[0 for _ in range(4)] for _ in range(4)]
fish_info = [[0,0] for _ in range(17)]

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        fish_num = row[j*2]
        fish_dir = row[j*2+1]
        fish_board[i][j] = fish_num
        fish_info[fish_num] = [i,j,fish_dir-1,True]

first_fish_num = fish_board[0][0]
shark_i, shark_j, shark_d = 0, 0, fish_info[first_fish_num][2]
fish_info[first_fish_num][3] = False
fish_board[0][0] = -1
answer = first_fish_num
solve(first_fish_num)
print(answer)