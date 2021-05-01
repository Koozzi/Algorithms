# 22:55
# 00:05
#

'''
1. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 
2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동
3. 자신의 냄새를 그 칸에 뿌린다
4. 냄새는 상어가 k번 이동하고 나면 사라진다.

이동방향
1. 인접한 칸 중 아무 냄새가 없는 칸
    1-1. 자신의 냄새가 있는 칸    
2. 가능한 칸이 여러 개 있으면, 우선순위를 따름

이동 후, 한 칸에 여러 마리의 상어가 있으면
번호가 가장 작은 상어 빼고 다 디짐
'''

def decrease_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j] != [0,0]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = [0,0]

def new_smell():
    for shark_num, shark in enumerate(shark_info[1:], start=1):
        if not shark[3]: continue
        smell[shark[0]][shark[1]] = [shark_num, K]

def shark_move():
    global shark_dead_count
    new_borad = [[0 for _ in range(N)] for _ in range(N)]
    for shark_num, shark in enumerate(shark_info[1:], start=1):
        
        I,J,D,live = shark
        if not live: continue

        no_smell_possible = [] # 인접한 칸 중 아무 냄새가 없는 칸을 찾아보자
        my_smell_possible = [] # 인접한 칸 중 자신 냄새가 있는 칸을 찾아보자

        for next_d in shark_priority[shark_num][D]:
            next_i = I + move[next_d][0]
            next_j = J + move[next_d][1]

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if smell[next_i][next_j] == [0,0]:
                no_smell_possible.append([next_i, next_j, next_d])
            elif smell[next_i][next_j][0] == shark_num:
                my_smell_possible.append([next_i, next_j, next_d])
            
        if no_smell_possible:
            next_i, next_j, next_d = no_smell_possible[0]

            # 나보다 강한 상어가 먼저 자리를 차지하고 있다.
            # 나는 그냥 죽어야 한다.
            if new_borad[next_i][next_j] != 0:
                shark_info[shark_num][3] = False
                shark_dead_count += 1
                continue
            
            new_borad[next_i][next_j] = shark_num
            shark_info[shark_num] = [next_i, next_j, next_d, True]
        
        elif not no_smell_possible and my_smell_possible:
            next_i, next_j, next_d = my_smell_possible[0]
            new_borad[next_i][next_j] = shark_num
            shark_info[shark_num] = [next_i, next_j, next_d, True]

    return new_borad

if __name__=="__main__":
    N, M, K = map(int, input().split())
    shark_info = [[0,0] for _ in range(M+1)]
    smell = [[[0,0] for _ in range(N)] for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    init_direction = list(map(int, input().split()))

    shark_priority = [[]]
    for shark_num in range(1,M+1):
        shark_priority.append([])
        for direction in range(4):
            direction_priority = list(map(int, input().split()))
            for d in range(4): direction_priority[d] -= 1
            shark_priority[shark_num].append(direction_priority)

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                shark_info[board[i][j]] = [i,j]

    for idx,d in enumerate(init_direction):
        shark_info[idx+1].append(d-1)
        shark_info[idx+1].append(True)

    answer, shark_dead_count = 0, 0
    while True:
        answer += 1
        if answer == 1001:
            answer = -1
            break

        decrease_smell()
        new_smell()
        board = shark_move()

        if shark_dead_count == M-1:
            break

    print(answer)