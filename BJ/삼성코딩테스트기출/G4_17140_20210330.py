# 16:44
# 17:36
# Asterisk(*) 과 Zip을 활용해서 Pythonic하게 코드를 작성하자

def operation():
    max_len = 0
    new_board = []
    for row in board:
        new_row, dic = [], {}

        for num in row:
            if num == 0: continue
            if num in dic:
                dic[num] += 1
            elif num not in dic:
                dic[num] = 1
        max_len = max(max_len, len(dic)*2)

        for key, value in dic.items():
            new_row.append([key,value])
        new_row.sort(key=lambda x:(x[1], x[0]))

        _new_row = []
        for num1, num2 in new_row:
            _new_row.append(num1)
            _new_row.append(num2)
        new_board.append(_new_row)
    
    for row in new_board:
        for _ in range(max_len - len(row)):
            row.append(0)
    
    return new_board

def rotate():
    N = len(board[0])
    M = len(board)
    new_board = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(M):
        for j in range(N):
            new_board[j][M-1-i] = board[i][j]

    return new_board

if __name__=="__main__":
    answer = 0
    I, J, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(3)]

    if I <= 3 and J <= 3:
        if board[I-1][J-1] == K:
            print(0)
            exit()

    while True:

        if len(board) >= len(board[0]):
            board = operation()
        elif len(board) < len(board[0]):
            board = list(map(list, zip(*board)))
            board = operation()
            board = list(map(list, zip(*board)))

        answer += 1
        if answer == 101:
            answer = -1
            break

        if len(board) >= I and len(board[0]) >= J:
            if board[I-1][J-1] == K:
                break

    print(answer)