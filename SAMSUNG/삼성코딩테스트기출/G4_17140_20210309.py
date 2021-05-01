def my_sort(l):
    dic = {}
    for num in l:
        if num == 0: continue
        if num in dic: dic[num] += 1
        else: dic[num] = 1
    
    new_list = []
    for key,item in dic.items():
        new_list.append([key, item])
    new_list.sort(key=lambda x:(x[1], x[0]))

    return_list = []
    for item in new_list:
        return_list.append(item[0])
        return_list.append(item[1])

    return return_list

def r_operator():
    new_board = []
    new_list = []
    max_len = 0

    for row in board:
        l = my_sort(row)
        if len(l) > 100: l = l[:100]
        max_len = max(max_len, len(l))
        new_list.append(l)
    
    for l in new_list:
        append_cnt = max_len - len(l)
        for _ in range(append_cnt):
            l.append(0)
        new_board.append(l)

    return new_board

def c_operator():
    r_len, c_len = len(board), len(board[0])
    new_list = []
    max_len = 0

    for j in range(c_len):
        col = []
        for i in range(r_len):
            col.append(board[i][j])
        l = my_sort(col)
        if len(l) > 100: l = l[:100]
        max_len = max(max_len, len(l))
        new_list.append(l)

    r_len, c_len = max_len, len(board[0])
    new_board = [[0 for j in range(c_len)] for i in range(r_len)]
    for j, l in enumerate(new_list):
        append_cnt = max_len - len(l)        
        for _ in range(append_cnt):
            l.append(0)
        for i in range(r_len):
            new_board[i][j] = l[i]

    return new_board

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(3)]

if N < 4 and M < 4:
    if board[N-1][M-1] == K:
        print(0)
        exit()

answer = 0
while True:
    if len(board) > N-1 and len(board[0]) > M-1:
        if board[N-1][M-1] == K: break

    if answer > 100:
        answer = -1
        break

    if len(board) >= len(board[0]):
        board = r_operator()
    else:
        board = c_operator()

    answer += 1

print(answer)