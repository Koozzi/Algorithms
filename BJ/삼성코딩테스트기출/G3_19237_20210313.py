def remove_smell():
    for i in range(N):
        for j in range(N):
            if board_smell[i][j][0] != -1 and board_smell[i][j][1] != 0:
                board_smell[i][j][1] -= 1
                if board_smell[i][j][1] == 0:
                    board_smell[i][j][0] = -1

def make_new_smell():
    global K
    for num, shark in enumerate(shark_info):
        I, J, live, direction = shark
        if not live: continue
        board_smell[I][J][0] = num
        board_smell[I][J][1] = K 

def get_next_location(num,I,J,direction):
    global N

    priority_direction = shark_dir[num][direction]
    
    for move in priority_direction:
        next_i, next_j = I + move_dir[move][0], J + move_dir[move][1]
        if not 0 <= next_i < N or not 0 <= next_j < N:
            continue
        if board_smell[next_i][next_j][0] == -1:
            shark_info[num][3] = move
            return next_i, next_j
    
    for move in priority_direction:
        next_i, next_j = I + move_dir[move][0], J + move_dir[move][1]
        if not 0 <= next_i < N or not 0 <= next_j < N:
            continue
        if board_smell[next_i][next_j][0] == num:
            shark_info[num][3] = move
            return next_i, next_j

def shark_move():
    global N, live_cnt

    # 상어가 도착할 후보지를 정한다.
    board_tmp = [[-1 for j in range(N)] for i in range(N)]
    for num, shark in enumerate(shark_info):
        I, J, live, direction = shark
        if not live: continue
        
        next_i, next_j = get_next_location(num, I, J, direction)

        if board_tmp[next_i][next_j] == -1:            # 이동하려는 칸이 빈칸인 경우
            shark[0], shark[1] = next_i, next_j
            board_tmp[next_i][next_j] = num

        elif -1 < board_tmp[next_i][next_j] < num:     # 이동하려는 칸에 나보다 
            shark[2] = False                           # 우선순위의 높은 상어가 존재하는 경우
            live_cnt -= 1

move_dir = [[-1,0],[1,0],[0,-1],[0,1]]
N, M, K = map(int, input().split())
board_smell = [[[-1,0] for j in range(N)] for i in range(N)]
shark_info = [[] for i in range(M)]
live_cnt = M

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] != 0:
            shark_info[row[j]-1] = [i,j,True]

init_dir = list(map(int, input().split()))
for idx, _dir in enumerate(init_dir):
    shark_info[idx].append(_dir-1)

shark_dir = [ [[] for d in range(4)] for m in range(M)]
for i in range(M):
    for j in range(4):
        shark_dir[i][j] = list(map(int, input().split()))
        for k in range(4):
            shark_dir[i][j][k] -= 1

answer = 0
while True:
    if answer == 1001: break
    if live_cnt == 1: break

    remove_smell()
    make_new_smell()
    shark_move()

    answer += 1

if answer == 1001: print(-1)
else: print(answer)