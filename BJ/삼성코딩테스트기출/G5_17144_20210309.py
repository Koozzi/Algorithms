def air_cleaner():
    global N, M
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                return i, j
def spread():
    global N, M     

    dust_info = []
    for i in range(N):
        for j in  range(M):
            if 0 < board[i][j] <= 1000:
                dust_info.append([i,j,board[i][j]])
    
    for dust in dust_info:
        spread_dust = dust[2] // 5
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = dust[0] + move[0]
            next_j = dust[1] + move[1]
            
            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue

            if board[next_i][next_j] == -1:
                continue
            
            board[next_i][next_j] += spread_dust
            board[dust[0]][dust[1]] -= spread_dust

def air_clean(cleaner_i, cleaner_j):
    global N, M
    
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    I, J, D = cleaner_i-1, cleaner_j, 0
    while True:
        if not 0 <= I + move[D][0] < cleaner_i+1 or not 0 <= J + move[D][1] < M:
            D = (D + 1) % 4
        
        if I + move[D][0] == cleaner_i and J + move[D][1] == cleaner_j:
            board[I][J] = 0
            break

        board[I][J] = board[I + move[D][0]][J + move[D][1]]
        I, J = I + move[D][0], J + move[D][1]

    move = [[1,0],[0,1],[-1,0],[0,-1]]
    I, J, D = cleaner_i+2, cleaner_j, 0
    while True:
        if not cleaner_i+1 <= I + move[D][0] < N or not 0 <= J + move[D][1] < M:
            D = (D + 1) % 4
        
        if I + move[D][0] == cleaner_i+1 and J + move[D][1] == cleaner_j:
            board[I][J] = 0
            break

        board[I][J] = board[I + move[D][0]][J + move[D][1]]
        I, J = I + move[D][0], J + move[D][1]

def get_dust_sum():
    answer = 0
    for row in board: 
        answer += sum(row)
    return answer + 2

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
cleaner_i, cleaner_j = air_cleaner()

for t in range(T):
    spread()
    air_clean(cleaner_i, cleaner_j)

print(get_dust_sum())