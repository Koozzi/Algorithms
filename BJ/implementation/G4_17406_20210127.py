from sys import stdin
from copy import deepcopy
from itertools import permutations

def rotate(board, operatation):
    move_dir = [[1,0],[0,1],[-1,0],[0,-1]]

    for operate in operatation:
        r, c, s = operate[0], operate[1], operate[2]
        top_left_i, top_left_j = r-s, c-s
        down_right_i, down_right_j = r+s, c+s

        while True:    
            if top_left_i == down_right_i or top_left_j == down_right_j:
                break

            current_i, current_j, current_d = top_left_i, top_left_j, 1

            tmp1, tmp2 = board[current_i-1][current_j-1], 0
            moved = False
            while True:
                current_i += move_dir[current_d][0]
                current_j += move_dir[current_d][1]
                tmp2 = board[current_i-1][current_j-1]
                board[current_i-1][current_j-1] = tmp1
                tmp1 = tmp2

                if current_i == down_right_i and current_j == top_left_j:
                    current_d = 2
                    
                elif current_i == down_right_i and current_j == down_right_j:
                    current_d = 3
        
                elif current_i == top_left_i and current_j == down_right_j:
                    current_d = 0

                if moved and current_i == top_left_i and current_j == top_left_j:
                    break

                if not moved: moved = True

            top_left_i += 1
            top_left_j += 1
            down_right_i -= 1
            down_right_j -= 1
            
    return board

def operate_board(board):
    min_value = 2e9
    for row in board:
        min_value = min(min_value, sum(row))
    
    return min_value

def solution(N, M, K, board, operation):
    value_of_array = 2e9
    operation_permutation = list(permutations(operation, K))

    for operate in operation_permutation:
        copied_board = deepcopy(board)
        rotated_board = rotate(copied_board, operate)
        value_of_array = min(value_of_array, operate_board(rotated_board))
        
    return value_of_array

if __name__=="__main__":
    N, M, K = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(N)]
    operate = [list(map(int, stdin.readline().split())) for _ in range(K)]

    print(solution(N, M, K, board, operate))