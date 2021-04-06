'''
시작 14:03
제출 15:16
종료
'''

def decrease_smell():
    for i in range(N):
        for j in range(N):
            if smell_board[i][j][1] > 0:
                smell_board[i][j][1] -= 1
                if smell_board[i][j][1] == 0:
                    smell_board[i][j][0] = 0

def make_new_smell():
    for shark_num, shark in enumerate(shark_info[1:], start=1):
        I,J,D,L = shark
        if not L: continue
        smell_board[I][J] = [shark_num, K]

def remain_only_one_shark():
    shark_cnt = 0
    for i in range(N):
        for j in range(N):
            if shark_board[i][j] != 0:
                shark_cnt += 1
    
    if shark_cnt  == 1: return True
    else: return False

def shark_move():

    new_shark_board = [[0 for _ in range(N)] for _ in range(N)]

    for shark_num, shark in enumerate(shark_info[1:], start=1):
        I,J,D,L = shark
        if not L: continue

        # print(shark_num, "번의 상어가 움직입니다.")
        
        # 현재 상어 번호와 방향에 따른 우선순위임
        current_priority = shark_priority[shark_num][D]
        # print(D, current_priority)
        # 현재 우선순위를 따져서 냄새가 없는 곳을 찾아야 한다.
        founnd_next_location = False
        for next_direction in current_priority:
            next_i = I + move[next_direction][0]
            next_j = J + move[next_direction][1]
            if 0 <= next_i < N and 0 <= next_j < N:
                owner, smell_cnt = smell_board[next_i][next_j]
                if owner == 0:
                    if new_shark_board[next_i][next_j] == 0:
                        new_shark_board[next_i][next_j] = shark_num
                        shark_info[shark_num] = [next_i, next_j, next_direction, True]
                        # print(shark_num,"번의 상어가 우선순위 방향에서 빈 칸을 찾았습니다.")
                    elif new_shark_board[next_i][next_j] != 0:
                        shark_info[shark_num] = [next_i, next_j, next_direction, False]
                        # print(shark_num,"번의 상어는 디졌습니다.")

                    founnd_next_location = True
                    break
        
        if founnd_next_location:
            continue

        # 냄새가 비어있는 곳을 찾지 못했다면
        # 우선순위를 따져서 자신의 냄사가 있는 쪽으로 다시 돌아간다.
        for next_direction in current_priority:
            next_i = I + move[next_direction][0]
            next_j = J + move[next_direction][1]
            if 0 <= next_i < N and 0 <= next_j < N:
                owner, smell_cnt = smell_board[next_i][next_j]
                if owner == shark_num:
                    new_shark_board[next_i][next_j] = shark_num
                    shark_info[shark_num] = [next_i, next_j, next_direction, True]
                    # print("우선순위 방향에서 나의 냄새가 있는 칸을 찾았습니다.")
                    break

    # print("상어가 움직였습니다.")
    # for i in new_shark_board:
    #     print(i)    

    return new_shark_board

move = [[],[-1,0],[1,0],[0,-1],[0,1]]
N, M, K = map(int, input().split())
shark_board = [list(map(int, input().split())) for _ in range(N)]
smell_board = [[[0,0] for _ in range(N)] for _ in range(N)]
init_direction = list(map(int, input().split()))
shark_info = [[] for _ in range(M+1)]
shark_priority = [[[] for _ in range(5)] for _ in range(M+1)]

for i in range(N):
    for j in range(N):
        if shark_board[i][j] == 0: continue
        shark_num = shark_board[i][j]
        shark_dir = init_direction[shark_num-1]
        shark_info[shark_num] = [i,j,shark_dir,True]

for num in range(1,M+1):
    for d in range(1,5):
        shark_priority[num][d] = list(map(int, input().split()))

for t in range(1,1001):
    decrease_smell()
    make_new_smell()

    # print("상어가 움직이기 전 냄새의 상황입니다.")
    # for i in smell_board:
    #     print(i)

    shark_board = shark_move()
    if remain_only_one_shark():
        print(t)
        exit()

print(-1)