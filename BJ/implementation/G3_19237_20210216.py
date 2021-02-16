move = [[],[-1,0],[1,0],[0,-1],[0,1]]

N, M, K = map(int, input().split())
board = [[] for i in range(N)]
shark = [[] for i in range(M+1)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        board[i].append([row[j], 0])
        if row[j] != 0:
            board[i][j][1] = K
            shark[row[j]]=[i,j]

tmp = list(map(int, input().split()))
for i in range(1,M+1):
    shark[i].append(tmp[i-1])
    shark[i].append(True)

shark_priority = [[[] for j in range(5)] for i in range(M+1)] 
for i in range(1,M+1):
    for j in range(1,5):
        tmp = list(map(int, input().split()))
        shark_priority[i][j] = tmp

dead_cnt = 0
second = 0

while True:
    second += 1
    # 1000초가 넘어가면
    if second > 1000:
        print(-1)
        break

    
    for num in range(1, M+1):
        '''
        shark에는 상어의 위치, 방향 그리고 생존여부에 대한 정보가 들어있다.
        상어가 움직일 수 있는 곳으로 위치정보와 방향을 갱싱한다.
        '''        
        if shark[num][3]: # 현재 상어가 살아있으면
            shark_i, shark_j, shark_d = shark[num][0], shark[num][1], shark[num][2]
            moved = False

            for d in shark_priority[num][shark_d]:
                next_i, next_j = shark_i + move[d][0], shark_j + move[d][1]

                if 0 <= next_i < N and 0 <= next_j < N:
                    if board[next_i][next_j][0] == 0:
                        shark[num] = [next_i, next_j, d, True]
                        moved = True
                        break
            
            # 갈 곳을 못찾아서 본인의 냄새가 있는 곳으로 돌아가야 함
            if not moved:
                for d in shark_priority[num][shark_d]:
                    next_i, next_j = shark_i + move[d][0], shark_j + move[d][1]

                    if 0 <= next_i < N and 0 <= next_j < N:
                        if board[next_i][next_j][0] == num:
                            shark[num] = [next_i, next_j, d, True]
                            moved = True
                            break    

    # 모든 냄새에 -1을 한다.
    for i in range(N):
        for j in range(N):
            if board[i][j][1] > 1: board[i][j][1] -= 1
            elif board[i][j][1] == 1: board[i][j] = [0,0]
            
    for num in range(1, M+1):
        '''
        번호가 낮은 상어부터 냄새를 뿌린다.
        상어가 냄새를 뿌리려고하는데 그 자리에 냄새의 크기가 K이면 그 상어는 죽는다.
        냄새를 뿌릴 때는 무조건 냄새의 크기는 K이며 냄새의 주인은 자기 자신이다.
        '''
        if shark[num][3]: # 현재 상어가 살아있으면
            shark_i, shark_j = shark[num][0], shark[num][1]
            if board[shark_i][shark_j][1] == K:
                # 냄새를 뿌릴려고 했지만 나보다 우선순위인 상어가 먼저 해당 자리에 냄새를 뿌렸음. 
                # 현재 상어는 디져야 함.
                shark[num][3] = False
                dead_cnt += 1
                if dead_cnt == M-1:
                    print(second)
                    exit()
                continue

            board[shark_i][shark_j] = [num, K]