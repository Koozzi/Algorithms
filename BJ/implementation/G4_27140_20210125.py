def operate(board):
    N = len(board)
    M = len(board[0])
    
    tmp_list = []
    max_len = 0
    
    for i in range(N):
        dictionary = {}
        for j in range(M):
            num = board[i][j]
            if num == 0: continue
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        num_info = list(dictionary.items())
        num_info = sorted(num_info, key=lambda x:(x[1], x[0]))
        tmp_list.append(num_info)
        max_len = max(max_len, len(num_info)*2)

    if max_len > 100: max_len = 100
    result_board = [[0 for j in range(max_len)] for i in range(N)]
    for i in range(len(tmp_list)):
        for j in range(len(tmp_list[i])):
            result_board[i][j*2] = tmp_list[i][j][0]
            result_board[i][j*2+1] = tmp_list[i][j][1]

    return result_board

def solution(R, C, K, board):
    
    time = 0
    if R < 3 and C < 3 and board[R][C] == K:
        return time

    while True:

        if len(board) >= len(board[0]):
            board = operate(board)
        else:
            board = list(map(list, zip(*board)))
            board = operate(board)
            board = list(map(list, zip(*board)))

        time += 1
        if time > 100: return -1
        if R < len(board) and C < len(board[0]):
            if board[R][C] == K: return time

if __name__ == "__main__":
    R, C, K = map(int, input().split())
    R, C = R - 1, C - 1

    board = [list(map(int, input().split())) for i in range(3)]

    print(solution(R, C, K, board))