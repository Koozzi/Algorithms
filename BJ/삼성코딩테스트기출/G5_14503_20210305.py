from sys import stdin

N, M = map(int, stdin.readline().split())
i, j, d = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
move = [[-1,0],[0,1],[1,0],[0,-1]]
answer = 0 

'''
board[i][j] = -1 : 청소완료
board[i][j] = 0  : 청소안함
board[i][j] = 1  : 벽
'''

while True:
    
    # Step 1
    if board[i][j] == 0:
        board[i][j] = -1
        answer += 1    

    # Step 2
    find_dirty_section = False
    for _ in range(4):
        d -= 1
        if d == -1: d = 3
        next_i, next_j = i + move[d][0], j + move[d][1]
        if not 0 <= next_i < N or not 0 <= next_j < M:
            continue
        if board[next_i][next_j] == -1 or board[next_i][next_j] == 1:
            continue
        if board[next_i][next_j] == 0:
            find_dirty_section = True
            i, j = next_i, next_j
            break
    
    # Step 3,4
    if not find_dirty_section:
        next_i, next_j = i - move[d][0], j - move[d][1]
        if not 0 <= next_i < N or not 0 <= next_j < M:
            break
        if board[next_i][next_j] == 1:
            break
        i, j = next_i, next_j

print(answer)