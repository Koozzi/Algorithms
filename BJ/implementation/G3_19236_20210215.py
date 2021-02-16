from copy import deepcopy

move_i = [-1, -1, 0, 1, 1, 1, 0, -1]
move_j = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(shark_i, shark_j, shark_d, shark_e):
    # 상어i, 상어i, 상어방향, 상어가 먹은 물고기
    global board, fish, answer
    move_fish(shark_i, shark_j)
    while True:
        next_i, next_j = shark_i + move_i[shark_d], shark_j + move_j[shark_d]
        
        if next_i < 0 or next_j < 0 or next_i >= 4 or next_j >= 4:
            answer = max(answer, shark_e)
            return

        if not board[next_i][next_j]:
            shark_i, shark_j = next_i, next_j
            continue
        
        copied_board, copied_fish = deepcopy(board), deepcopy(fish)
        tmp1, tmp2 = fish[board[next_i][next_j][0]], board[next_i][next_j]
        fish[board[next_i][next_j][0]], board[next_i][next_j] = [], []
        dfs(next_i, next_j, tmp2[1], shark_e + tmp2[0])
        board, fish = copied_board, copied_fish
        fish[board[next_i][next_j][0]], board[next_i][next_j] = tmp1, tmp2
        shark_i, shark_j = next_i, next_j

def move_fish(shark_i, shark_j):
    for i in range(1,17):
        if not fish[i]: continue
        fish_i, fish_j = fish[i][0], fish[i][1]
        
        for _ in range(9):
            next_i, next_j = fish_i + move_i[ board[fish_i][fish_j][1] ], fish_j + move_j[ board[fish_i][fish_j][1] ]
            if next_i < 0 or next_j < 0 or next_i >= 4 or next_j >= 4 or (next_i == shark_i and next_j == shark_j):
                board[fish_i][fish_j][1] = (board[fish_i][fish_j][1] + 1) % 8
                continue
            
            if board[next_i][next_j]:
                fish[board[next_i][next_j][0]] = [fish_i, fish_j]
            board[next_i][next_j], board[fish_i][fish_j] = board[fish_i][fish_j], board[next_i][next_j]
            fish[i] = [next_i, next_j]

            break          

board = [[] for _ in range(4)] # fish_num, fish_dir
fish = [[] for _ in range(17)] # fish_I, fish_J
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0,8,2):
        board[i].append([ tmp[j], tmp[j+1]-1 ])
        fish[tmp[j]] = [i,j//2]

answer = 0
shark_dir, shark_eat = board[0][0][1], board[0][0][0]
fish[board[0][0][0]], board[0][0] = [], []

dfs(0,0,shark_dir,shark_eat)
print(answer)