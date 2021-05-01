'''
시작 16:24
제출 16:40
종료
'''

def operate(board):
    max_len = 0
    new_board = [[] for _ in range(len(board))]

    for idx, row in enumerate(board):
        number_cnt_dictionary = {}
        for num in row:
            if num == 0: continue
            if num in number_cnt_dictionary:
                number_cnt_dictionary[num] += 1
            elif num not in number_cnt_dictionary:
                number_cnt_dictionary[num] = 1
        max_len = max(max_len, len(number_cnt_dictionary)*2)
            
        new_row = []
        for num, cnt in number_cnt_dictionary.items():
            new_row.append([num, cnt])
        new_row.sort(key=lambda x:(x[1], x[0]))

        for num, cnt in new_row:
            new_board[idx].append(num)
            new_board[idx].append(cnt)

    for row in new_board:
        for _ in range(max_len - len(row)):
            row.append(0)

    return new_board
    

I, J, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

if I-1 < 3 and J-1 < 3:
    if board[I-1][J-1] == K:
        print(0)
        exit()

for t in range(101):

    if I-1 < len(board) and J-1 < len(board[0]):
        if board[I-1][J-1] == K:
            print(t)
            exit()

    if len(board) >= len(board[0]):
        board = operate(board)
    elif len(board) < len(board[0]):
        board = list(map(list, zip(*board)))
        board = operate(board)
        board = list(map(list, zip(*board)))
    
print(-1)