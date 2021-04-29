'''
시작 16:00
제출 16;47
종료
'''

def decrease_shark_smell():
    for i in range(N):
        for j in range(N):
            if smell_board[i][j][1] > 0:
                smell_board[i][j][1] -= 1
                if smell_board[i][j][1] == 0:
                    smell_board[i][j][0] = 0

def add_new_shark_smell():
    for shark_num, shark in enumerate(shark_info[1:], start=1):
        I,J,D,L = shark
        if not L: continue
        smell_board[I][J] = [shark_num, K]

def check_left_shark():
    count = 0
    for i in range(N):
        for j in range(N):
            if shark_board[i][j] > 0:
                count += 1
    
    if count > 1: return False
    return True

move = [[-1,0],[1,0],[0,-1],[0,1]]
N, M, K = map(int, input().split())
shark_board = [list(map(int, input().split())) for _ in range(N)]
smell_board = [[[0,0] for _ in range(N)] for _ in range(N)]
shark_info = [[] for _ in range(M+1)]

for i in range(N):
    for j in range(N):
        if shark_board[i][j] > 0:
            shark_num = shark_board[i][j]
            shark_info[shark_num] = [i,j,0,True]

shark_directions = list(map(lambda x:int(x)-1, input().split()))
for num, d in enumerate(shark_directions):
    shark_info[num+1][2] = d

shark_priority = [[]]
for shark_num in range(1,M+1):
    priority = [list(map(lambda x:int(x)-1, input().split())) for _ in range(4)]    
    shark_priority.append(priority)

def shark_move():
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    for shark_num, shark in enumerate(shark_info[1:], start=1):
        I,J,D,L = shark
        if not L: continue
        
        shark_move_priority = shark_priority[shark_num][D]

        found_empty_place = False
        next_i, next_j = 0, 0
        for next_d in shark_move_priority:
            next_i = I + move[next_d][0]
            next_j = J + move[next_d][1]
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if smell_board[next_i][next_j] == [0,0]:
                found_empty_place = True
                if new_board[next_i][next_j] == 0:
                    new_board[next_i][next_j] = shark_num
                    shark_info[shark_num] = [next_i, next_j, next_d, True]
                else:
                    shark_info[shark_num] = [next_i, next_j, next_d, False]
                break
                
        if found_empty_place:
            continue

        for next_d in shark_move_priority:
            next_i = I + move[next_d][0]
            next_j = J + move[next_d][1]
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if smell_board[next_i][next_j][0] == shark_num:
                new_board[next_i][next_j] = shark_num
                shark_info[shark_num] = [next_i, next_j, next_d, True]
                break
    
    return new_board

for t in range(1,1001):
    
    decrease_shark_smell()
    add_new_shark_smell()
    shark_board = shark_move()
    if check_left_shark():
        print(t)
        exit()

print(-1)