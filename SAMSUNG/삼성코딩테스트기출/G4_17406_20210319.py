from itertools import permutations
from copy import deepcopy

def rotate(copied_board, I, J, s):

    top_left, top_right = copied_board[I-s][J-s], copied_board[I-s][J+s]
    down_left, down_right = copied_board[I+s][J-s], copied_board[I+s][J+s]

    for j in range(J+s-1, J-s, -1):
        copied_board[I-s][j+1] = copied_board[I-s][j]
    for i in range(I+s-1, I-s, -1):
        copied_board[i+1][J+s] = copied_board[i][J+s]
    for j in range(J-s+1, J+s):
        copied_board[I+s][j-1] = copied_board[I+s][j]
    for i in range(I-s+1, I+s):
        copied_board[i-1][J-s] = copied_board[i][J-s]

    copied_board[I-s][J-s+1] = top_left
    copied_board[I-s+1][J+s] = top_right
    copied_board[I+s][J+s-1] = down_right
    copied_board[I+s-1][J-s] = down_left

    return copied_board

answer = 2e9
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
rotates = [list(map(int, input().split())) for i in range(K)]
permute_rotates = permutations(rotates)

for rotates in permute_rotates:

    copied_board = deepcopy(board)
    for I, J, S in rotates:
        for s in range(1, S+1):
            copied_board = rotate(copied_board, I-1, J-1, s)

    min_row = 2e9
    for row in copied_board:
        min_row = min(min_row, sum(row))
    answer = min(answer, min_row)

print(answer)