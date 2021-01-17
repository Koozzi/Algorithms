from collections import deque
from sys import stdin

def dust_spread(N, M, board):
    move_dir = [[-1,0],[1,0],[0,1],[0,-1]]

    new_board = [[0 for i in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if 5 <= board[i][j] <= 1000:
                spread_num = board[i][j] // 5
                for n in range(4):
                    next_i = i + move_dir[n][0]
                    next_j = j + move_dir[n][1]

                    if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                        continue

                    if board[next_i][next_j] == -1:
                        continue 

                    new_board[next_i][next_j] += spread_num
                    board[i][j] -= spread_num

    for i in range(N):
        for j in range(M):
            new_board[i][j] += board[i][j]

    return new_board

def air_cleaner(N, M, board, air_cleaner_i):
    new_board = [[0 for j in range(M)] for i in range(N)]
    
    # 공기 청정기 시계방향
    move_dir = [[0,1],[1,0],[0,-1],[-1,0]]
    current_i = air_cleaner_i
    current_j = 1
    direction = 0

    while True:

        if current_i == air_cleaner_i and current_j == M-1 \
            or current_i == N-1 and current_j == M-1 \
                or current_i == N-1 and current_j == 0:
            direction += 1

        next_i = current_i + move_dir[direction][0]
        next_j = current_j + move_dir[direction][1]

        if next_i == air_cleaner_i and next_j == 0:
            break

        new_board[next_i][next_j] = board[current_i][current_j]

        current_i = next_i
        current_j = next_j 
    
    # 공기 청정기 반시계방향
    move_dir = [[0,1],[-1,0],[0,-1],[1,0]]
    current_i = air_cleaner_i - 1
    current_j = 1
    direction = 0

    while True:

        if current_i == air_cleaner_i - 1 and current_j == M-1 \
            or current_i == 0 and current_j == M-1 \
                or current_i == 0 and current_j == 0:
            direction += 1

        next_i = current_i + move_dir[direction][0]
        next_j = current_j + move_dir[direction][1]

        if next_i == air_cleaner_i - 1 and next_j == 0:
            break

        new_board[next_i][next_j] = board[current_i][current_j]

        current_i = next_i
        current_j = next_j

    # for i in new_board:
    #     print(i)

    for i in range(N):
        for j in range(M):
            if (0 < i < air_cleaner_i - 1 and 0 < j < M-1) or (air_cleaner_i < i < N-1 and 0 < j < M-1):
                new_board[i][j] = board[i][j]

    return new_board

def solution(N, M, T, board):

    air_cleaner_i = 0
    for i in range(N):
        if board[i][0] == -1:
            air_cleaner_i = i

    for t in range(T):
        print("퍼진뒤")
        board = dust_spread(N, M, board)
        for i in board:
            print(i)
        
        print("돌려")
        board = air_cleaner(N, M, board, air_cleaner_i)
        for i in board:
            print(i)

    dust_sum = 0
    for row in board:
        for dust in row:
            dust_sum += dust 

    return dust_sum

if __name__=="__main__":
    R, C, T = map(int, stdin.readline().split())

    board = []
    for i in range(R):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    print(solution(R, C, T, board))