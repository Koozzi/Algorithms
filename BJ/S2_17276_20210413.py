from sys import stdin

def rotate(board, M, rotate_count):

    next_location = []
    for i in range(N):
        for j in range(N):
            
            next_i, next_j = i, j
            for _ in range(rotate_count):
                if next_i == next_j:
                    if M == 45: next_j = N // 2
                    else: next_i = N // 2
                elif next_i + next_j == N-1:
                    if M == 45: next_i = N // 2
                    else: next_j = N // 2
                elif next_i == N // 2:
                    if M == 45: next_i = next_j
                    else: next_i = N-1 - next_j
                elif next_j == N // 2:
                    if M == 45: next_j = N-1 - next_i
                    else: next_j = next_i
    
            next_location.append([next_i, next_j, board[i][j]])

    for I, J, num in next_location:
        board[I][J] = num

    return board

T = int(stdin.readline())
for t in range(T):
    N, M = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(N)]
    
    if M != 0:
        rotate_count = abs(M // 45)
        if M > 0: M = 45
        else: M = -45
        board = rotate(board, M, rotate_count)

    for row in board:
        print(*row)