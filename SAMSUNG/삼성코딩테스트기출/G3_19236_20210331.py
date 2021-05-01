# 16:25
# 
# 

from copy import deepcopy

def fish_move():
    for current_fish_num in range(1, 17):
        if not fish_info[current_fish_num][2]: continue
        I,J = fish_info[current_fish_num][:2]
        D = board[I][J][1]

        for _ in  range(8):
            next_i = I + move[D][0]
            next_j = J + move[D][1]  

            # 경계 밖으로 나가면 방향 돌려
            if not 0 <= next_i < 4 or not 0 <= next_j < 4:
                D = (D + 1) % 8
                continue

            # 상어 만나면 방향 돌려
            if board[next_i][next_j][0] == -1:
                D = (D + 1) % 8
                continue
            
            next_fish_num, next_fish_d = board[next_i][next_j]
            if next_fish_num > 0:
                fish_info[next_fish_num] = [I, J, True]
                board[I][J] = [next_fish_num, next_fish_d]
            elif next_fish_num == 0:
                board[I][J] = [0,0]
            fish_info[current_fish_num] = [next_i, next_j, True]
            board[next_i][next_j] = [current_fish_num, D]
            break  

def shark_can_eat(i,j,d):
    tmp = []
    while True:
        i += move[d][0]
        j += move[d][1]
        if not 0 <= i < 4 or not 0 <= j < 4:
            break
        if board[i][j][0] > 0 :
            tmp.append([i,j])
    return tmp

def solve(fish_sum):
    global shark_i, shark_j, shark_d, answer, board, fish_info

    fish_move()
    tmp = shark_can_eat(shark_i, shark_j, shark_d)

    if len(tmp) == 0:
        answer = max(answer, fish_sum)
        return

    for I, J in tmp:
        copied_i, copied_j, copied_d = shark_i, shark_j, shark_d
        copied_board, copied_fish_info = deepcopy(board), deepcopy(fish_info)
        fish_num, fish_dir = board[I][J]           # 상어가 잡아먹을 물고기의 번호와 방향
        board[shark_i][shark_j] = [0,0]            # 원래 있던 상어 자리를 빈칸으로 만들어준다.
        board[I][J] = [-1, fish_dir]               # 현재 위치에 board에 상어의 정보를 넣는다.
        fish_info[fish_num][2] = False             # 해당 물고기를 죽인다
        shark_i, shark_j, shark_d = I, J, fish_dir # 상어의 정보를 갱신한다.
        solve(fish_sum + fish_num)
        board, fish_info = copied_board, copied_fish_info
        shark_i, shark_j, shark_d = copied_i, copied_j, copied_d

if __name__=="__main__":
    move = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    fish_info = [[] for _ in range(17)]
    board = [[[0,0] for j in range(4)] for i in range(4)]

    for i in range(4):
        row = list(map(int, input().split()))
        for j in range(4):
            board[i][j] = [row[j*2], row[j*2+1]-1]
            fish_info[row[j*2]] = [i,j,True]

    shark_i, shark_j, shark_d = 0, 0, board[0][0][1]
    fish_info[ board[0][0][0] ][2] = False
    first_fish_num = board[0][0][0]
    board[0][0][0] = -1
    answer = 0

    solve(first_fish_num)

    print(answer)

'''
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
'''