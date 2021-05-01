# 12:55
# 13:43
# 시뮬레이션 설계를 잘못함

def clean(I,J):
    board[I][J] = -1

def robot_move_left(I,J,D):
    next_d = D - 1
    if next_d == -1: next_d = 3
    next_i = I + move_dir[next_d][0]
    next_j = J + move_dir[next_d][1]

    return next_i, next_j, next_d

def robot_move_back(I, J, D):
    next_i, next_j = 0, 0

    if D == 0:
        next_i = I + move_dir[2][0]
        next_j = J + move_dir[2][1]
    elif D == 1:
        next_i = I + move_dir[3][0]
        next_j = J + move_dir[3][1]
    elif D == 2:
        next_i = I + move_dir[0][0]
        next_j = J + move_dir[0][1]
    elif D == 3:
        next_i = I + move_dir[1][0]
        next_j = J + move_dir[1][1] 
    
    return next_i, next_j

def solve(I, J, D):
    board[I][J] = -1
    answer = 1

    while True:

        # 현재 위치를 청소한다.
        clean(I,J)

        # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
        found_dirty_spot = False
        next_i, next_j, next_d = 0, 0, D
        for _ in range(4):
            next_d = next_d - 1
            if next_d == -1: next_d = 3
            next_i = I + move_dir[next_d][0]
            next_j = J + move_dir[next_d][1]
            if board[next_i][next_j] == 0:
                I, J, D = next_i, next_j, next_d
                found_dirty_spot = True
                answer += 1
                break
    
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
        # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if found_dirty_spot:
            continue

        # Step 2-c
        # 로봇을 뒤로 이동한다.
        I, J = robot_move_back(I, J, D)

        # 그런데 이동한 위치가 벽이라면 로봇의 작동을 멈춘다.
        if board[I][J] == 1:
            break

    return answer

if __name__=="__main__":
    N, M = map(int, input().split())
    I, J, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cleaned = [[False for j in range(M)] for i in range(N)]
    move_dir = [[-1,0],[0,1],[1,0],[0,-1]]
    print(solve(I, J, D))