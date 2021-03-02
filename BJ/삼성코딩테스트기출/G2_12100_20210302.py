from copy import deepcopy

def push(input_list):
    global N
    return_list = [0 for i in range(N)]
    input_idx = N-1
    for i in range(N-1, -1, -1):
        if input_list[i] != 0:
            return_list[input_idx] = input_list[i]
            input_idx -= 1
    return return_list

def combine(input_list):
    global answer
    for i in range(N-1,0,-1):
        if input_list[i] != 0 and input_list[i] == input_list[i-1]:
            input_list[i] += input_list[i]
            input_list[i-1] = 0
            
    return_list = push(input_list)
    answer = max(answer, max(return_list))
    return return_list

def move_list(input_list):
    return combine(push(input_list))

def move_board(input_board, direction):
    global N
    return_board = [[0 for j in range(N)] for i in range(N)]

    if direction == 0: # 우
        for i in range(N):
            return_board[i] = move_list(input_board[i])

    elif direction == 1: # 좌
        for i in range(N):
            input_board[i].reverse()
            return_board[i] = move_list(input_board[i])
            return_board[i].reverse()

    elif direction == 2: # 상
        for j in range(N):
            input_list = [0 for i in range(N)]
            for i in range(N):
                input_list[i] = input_board[i][j]
            input_list.reverse()
            input_list = move_list(input_list)
            input_list.reverse()
            for i in range(N):
                return_board[i][j] = input_list[i]
                
    elif direction == 3: # 하
        for j in range(N):
            input_list = [0 for i in range(N)]
            for i in range(N):
                input_list[i] = input_board[i][j]
            input_list = move_list(input_list)
            for i in range(N):
                return_board[i][j] = input_list[i]

    return return_board

def solve(cnt):
    global board, answer, directions
    if cnt == 5: return
    for i in range(4):
        copied_board = deepcopy(board)
        board = move_board(board, i)
        solve(cnt+1)
        board = copied_board

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
answer = 0
solve(0)
print(answer)

# board = move_board(board, 3)
# for i in board:
#     print(i)
# board = move_board(board, 1)
# for i in board:
#     print(i)
# board = move_board(board, 2)
# for i in board:
#     print(i)
# board = move_board(board, 0)
# for i in board:
#     print(i)
# board = move_board(board, 2)
# for i in board:
#     print(i)
