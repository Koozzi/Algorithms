'''
시작 17:21
제출 17:42
종료
'''

def array_operate():

    max_len = 0
    new_board = []
    for idx, row in enumerate(board):
        num_info = {}
        for num in row:
            if num == 0: continue
            if num in num_info:
                num_info[num] += 1
            elif num not in num_info:
                num_info[num] = 1

        row_list = []
        for key, value in num_info.items():
            row_list.append([key, value])
        row_list.sort(key=lambda x:(x[1], x[0]))
        max_len = max(max_len, len(row_list)*2)
        
        new_board.append([])
        for A, B in row_list:
            new_board[idx].append(A)
            new_board[idx].append(B)

    for row in new_board:
        for _ in range(max_len-len(row)):
            row.append(0)
    
    return new_board
    

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

if N-1 < 3 and M - 1 < 3:
    if board[N-1][M-1] == K:
        print(0)
        exit()

answer = 0

while True:
    answer += 1
    if answer == 101:
        answer = -1
        break

    if len(board) >= len(board[0]):
        board = array_operate()
    else:
        board = list(map(list, zip(*board)))
        board = array_operate()
        board = list(map(list, zip(*board)))
    
    if N-1 < len(board) and M-1 < len(board[0]):
        if board[N-1][M-1] == K:
            break

print(answer)