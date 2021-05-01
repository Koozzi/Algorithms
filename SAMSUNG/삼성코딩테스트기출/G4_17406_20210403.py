'''
시작 14:05
제출 14:35
종료 
'''
from itertools import permutations
from copy import deepcopy

def rotate(copied_board,I,J,S):
    
    top_left, top_right = copied_board[I-S][J-S], copied_board[I-S][J+S]
    down_left, down_right = copied_board[I+S][J-S], copied_board[I+S][J+S]

    for j in range(J+S-1, J-S, -1):
        copied_board[I-S][j+1] = copied_board[I-S][j]
    for i in range(I+S-1, I-S, -1):
        copied_board[i+1][J+S] = copied_board[i][J+S]
    for j in range(J-S+1, J+S):
        copied_board[I+S][j-1] = copied_board[I+S][j]
    for i in range(I-S+1, I+S):
        copied_board[i-1][J-S] = copied_board[i][J-S]

    copied_board[I-S][J-S+1] = top_left
    copied_board[I-S+1][J+S] = top_right
    copied_board[I+S][J+S-1] = down_right
    copied_board[I+S-1][J-S] = down_left

def get_value_of_array(copied_board):
    value = sum(copied_board[0])    
    for row in copied_board[1:]:
        value = min(value, sum(row))
    return value

answer = 5000
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(K)]

for command in permutations(commands, K):
    copied_board = deepcopy(board)
    for I,J,C in command:
        for c in range(1, C+1):
            rotate(copied_board,I-1, J-1, c)
    answer = min(answer, get_value_of_array(copied_board))

print(answer)