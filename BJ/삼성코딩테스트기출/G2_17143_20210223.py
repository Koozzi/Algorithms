from copy import deepcopy

N, M, S = map(int, input().split())
shark_info = [list(map(int, input().split())) for i in range(S)]
shark_info = sorted(shark_info, key=lambda x:-x[4])
board = [[[] for j in range(M)]for i in range(N)]
move_dir = [[-1,0],[1,0],[0,1],[0,-1]]
for num, shark in enumerate(shark_info):
    shark[0] -= 1
    shark[1] -= 1
    shark[3] -= 1
    if shark[3] == 0 or shark[3] == 1: shark[2] %= ((N-1)*2)
    elif shark[3] == 2 or shark[3] == 3: shark[2] %= ((M-1)*2)
    board[shark[0]][shark[1]] = [num, shark[2], shark[3], shark[4]]
    shark.append(True)

def move_shark(num):
    cnt = 0
    while cnt < shark_info[num][2]:
        ni = shark_info[num][0] + move_dir[shark_info[num][3]][0]
        nj = shark_info[num][1] + move_dir[shark_info[num][3]][1]
        if not 0 <= ni < N or not 0 <= nj < M:
            if shark_info[num][3] == 0: shark_info[num][3] = 1
            elif shark_info[num][3] == 1: shark_info[num][3] = 0
            elif shark_info[num][3] == 2: shark_info[num][3] = 3
            elif shark_info[num][3] == 3: shark_info[num][3] = 2
            shark_info[num][0] += move_dir[shark_info[num][3]][0]
            shark_info[num][1] += move_dir[shark_info[num][3]][1]
        else:
            shark_info[num][0] = ni
            shark_info[num][1] = nj
        cnt += 1
    return shark_info[num]

answer = 0
for person in range(M):
    
    # 지면과 가장 가까운 상어 Get
    for i in range(N):
        if board[i][person]:
            num = board[i][person][0]
            shark_info[num][5] = False
            answer += board[i][person][3]
            board[i][person] = []
            break 

    # 상어야 움직이자
    new_board = [[[] for j in range(M)]for i in range(N)]
    for num, shark in enumerate(shark_info):
        if not shark[5]: continue
        I, J, Sp, Di, Sz, L = move_shark(num)
        if new_board[I][J]: # 이미 다른 상어가 존재 -> 내가 가면 먹힘
            shark[5] = False
        else: # 빈 자리이면 내가 먼저 가서 자리를 잡고 있는다.
            new_board[I][J] = [num, Sp, Di, Sz]
    board = deepcopy(new_board)    

print(answer)