# 11:30
# 12:07
# 문제의 조건을 꼼꼼히 따질 것

from copy import deepcopy

def move_dice(I,J,D):
    
    next_i = I + move_dir[D][0]
    next_j = J + move_dir[D][1]
    new_dice = deepcopy(dice)

    if D == 1:    # 동
        new_dice[5] = dice[0] # 위 -> 오
        new_dice[1] = dice[5] # 오 -> 아
        new_dice[4] = dice[1] # 아 -> 왼      
        new_dice[0] = dice[4] # 왼 -> 위
    elif D == 2:  # 서
        new_dice[4] = dice[0] # 위 -> 왼
        new_dice[1] = dice[4] # 왼 -> 아
        new_dice[5] = dice[1] # 아 -> 오
        new_dice[0] = dice[5] # 오 -> 위
    elif D == 3:  # 북
        new_dice[3] = dice[0] # 위 -> 뒤
        new_dice[1] = dice[3] # 뒤 -> 아
        new_dice[2] = dice[1] # 아 -> 앞
        new_dice[0] = dice[2] # 앞 -> 위
    elif D == 4:  # 남
        new_dice[2] = dice[0] # 위 -> 앞
        new_dice[1] = dice[2] # 앞 -> 아
        new_dice[3] = dice[1] # 아 -> 뒤
        new_dice[0] = dice[3] # 뒤 -> 앞

    return next_i, next_j, new_dice

if __name__=="__main__":
    move_dir = [[],[0,1],[0,-1],[-1,0],[1,0]]
    N, M, I, J, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    move_info = list(map(int, input().split()))
    dice = [0 for _ in range(6)]
    
    for D in move_info:
        
        if not 0 <= I+move_dir[D][0] < N or not 0 <= J+move_dir[D][1] < M:
            #  바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며
            #  출력도 하면 안 된다.
            continue

        I, J, dice = move_dice(I,J,D)
        # 현재 주사위의 위치를 변경
        # 주사위 현재 상태 변경

        if board[I][J] == 0:
            board[I][J] = dice[1] # 주사위의 바닥면이 현재 칸에 복사됨
            
        elif board[I][J] != 0:
            dice[1] = board[I][J] # 칸에 쓰여 있는 수가 주사위의 바닥면에 복사됨
            board[I][J] = 0       # 칸에 쓰여 있는 수는 0이 된다.
        
        print(dice[0])