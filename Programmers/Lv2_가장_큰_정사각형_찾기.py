def solution(board):
    answer = 0

    height = len(board)
    width = len(board[0])

    if height == 1 or width == 1:
        if any(board): return 1
        else: return 0

    new_board = [[0 for _ in range(width)] for _ in range(height)]

    new_board[0][0] = board[0][0]
    for i in range(1, height):
        new_board[i][0] = board[i][0]
    for j in range(1, width):
        new_board[0][j] = board[0][j]

    for i in range(1, height):
        for j in range(1, width):
            if board[i][j] == 0: continue
            new_board[i][j] = 1 + min(new_board[i-1][j], min(new_board[i-1][j-1], new_board[i][j-1]))
            answer = max(answer, new_board[i][j])

    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9
print(solution([[0,0,1,1],[1,1,1,1]])) # 4
print(solution([[0,0,0,0],[0,0,0,0]])) # 0
print(solution([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])) # 16
print(solution([[1,1,1,1]])) # 1
print(solution([[1,1,1,1,],[1,1,1,1]])) # 4