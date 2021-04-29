from copy import deepcopy

def rotate(board,N,M,Q):
    new_board = deepcopy(board)
    I1, J1, I2, J2 = map(lambda x:x-1, Q)
    min_num = board[I1][J1]

    D = 0
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    
    ci, cj = I1+1, J1
    while True:

        # min_num = min(min_num, board[ci][cj])
        
        if (ci == I1 and cj == J2) \
            or (ci == I2 and cj == J2) \
            or (ci == I2 and cj == J1):
            D = (D + 1) % 4

        next_i = ci + move[D][0]
        next_j = cj + move[D][1]
        
        new_board[ci][cj] = board[next_i][next_j]

        ci += move[D][0]
        cj += move[D][1]
        
        if ci == I1 and cj == J1:
            new_board[ci][cj] = board[I1][J1+1]
            break

    return min_num, new_board

def board_init(rows, columns):
    cnt = 1
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt += 1
    return board

def solution(rows, columns, queries):
    
    board = board_init(rows, columns)

    answer = []        
    for Q in queries:
        min_num, board = rotate(board, rows, columns, Q)
        answer.append(min_num)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))