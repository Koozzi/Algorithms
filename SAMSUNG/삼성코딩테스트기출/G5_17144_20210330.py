# 15:04
# 15:32
# 

def get_total_dust():
    answer = 0
    for i in range(N):
        for j in range(M):
            if 0 < board[i][j]:
                answer += board[i][j]
    return answer

def spread_dust():
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1: continue
            spread_sum = 0
            for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                next_i = i + di
                next_j = j + dj
                if not 0 <= next_i < N or not 0 <= next_j < M:
                    continue
                if board[next_i][next_j] == -1:
                    continue
                new_board[next_i][next_j] += (board[i][j] // 5)
                spread_sum += (board[i][j] // 5)
            board[i][j] -= spread_sum
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1: continue
            board[i][j] += new_board[i][j]

def clean_air():
    # 상위
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    current_i, current_j, current_d = cleaner-1, 0, 0
    while True:
        next_i = current_i + move[current_d][0]
        next_j = current_j + move[current_d][1]

        if next_i == 0 and next_j == 0 or \
            next_i == 0 and next_j == M-1 or \
                next_i == cleaner and next_j == M-1:
                current_d += 1
        
        if next_i == cleaner and next_j == 0:
            board[current_i][current_j] = 0
            break

        board[current_i][current_j] = board[next_i][next_j]
        current_i, current_j = next_i, next_j


    # 하위
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    current_i, current_j, current_d = cleaner+2, 0, 0
    while True:
        next_i = current_i + move[current_d][0]
        next_j = current_j + move[current_d][1]

        if next_i == N-1 and next_j == M-1 or \
            next_i == cleaner+1 and next_j == M-1 or \
                next_i == N-1 and next_j == 0:
                current_d += 1
        
        if next_i == cleaner+1 and next_j == 0:
            board[current_i][current_j] = 0
            break

        board[current_i][current_j] = board[next_i][next_j]
        current_i, current_j = next_i, next_j    

if __name__=="__main__":
    N, M, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    cleaner = 0
    for i in range(N):
        if board[i][0] == -1:
            cleaner = i
            break

    for _ in range(T):
        spread_dust()
        clean_air()

    print(get_total_dust())