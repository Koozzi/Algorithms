from itertools import permutations
from copy import deepcopy

def get_value(copied_board):
    global N
    value = sum(copied_board[0])
    for i in range(1, N):
        value = min(value, sum(copied_board[i]))
    return value

def rotate(copied_board,I,J,S):
    global N
    
    for s in range(1, S+1):
        left_top, left_down = copied_board[I-s][J-s], copied_board[I+s][J-s]
        right_top, rigth_down = copied_board[I-s][J+s], copied_board[I+s][J+s]

        for j in range(J+s-1, J-s, -1):
            copied_board[I-s][j+1] = copied_board[I-s][j]
        for i in range(I+s-1, I-s, -1):
            copied_board[i+1][J+s] = copied_board[i][J+s]
        for j in range(J-s+1, J+s):
            copied_board[I+s][j-1] = copied_board[I+s][j]
        for i in range(I-s+1, I+s):
            copied_board[i-1][J-s] = copied_board[i][J-s]
        
        copied_board[I-s][J-s+1] = left_top
        copied_board[I-s+1][J+s] = right_top
        copied_board[I+s][J+s-1] = rigth_down
        copied_board[I+s-1][J-s] = left_down

    return copied_board

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
rotate_init = [list(map(int, input().split())) for i in range(K)]
rotate_info = list(permutations(rotate_init, K))
answer = 5000

for rotate_order in rotate_info:
    copied_board = deepcopy(board)
    for I,J,S in rotate_order:
        copied_board = rotate(copied_board,I-1,J-1,S)

    answer = min(answer, get_value(copied_board))

print(answer)

'''
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
'''