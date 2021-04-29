from sys import stdin

def rotate(tl_i, tl_j, br_i, br_j, rotate_num):
    
    for _ in range(rotate_num):
        prev = board[tl_i][tl_j]
        tmp, D = 0, 0
        I, J = tl_i, tl_j

        while True:    
            I += move[D][0]
            J += move[D][1]

            tmp = board[I][J]
            board[I][J] = prev
            prev = tmp

            if I == br_i and J == tl_j \
                or I == br_i and J == br_j \
                    or I == tl_i and J == br_j:
                    D += 1
            
            if I == tl_i and J == tl_j:
                break
    
    return board

    
move = [[1,0],[0,1],[-1,0],[0,-1]]
N, M, R = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

tl_i, tl_j = 0, 0
br_i, br_j = N-1, M-1

while True:

    if tl_i >= br_i or tl_j >= br_j:
        break
    
    rotate_num = R % (4 + (br_i - tl_i - 1) * 2 + (br_j - tl_j - 1) * 2)
    board = rotate(tl_i, tl_j, br_i, br_j, rotate_num)

    tl_i += 1 ; tl_j += 1
    br_i -= 1 ; br_j -= 1

for row in board:
    print(*row)