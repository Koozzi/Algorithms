def rotate_board(current_board):
    new_board = []
    max_len = 0
    for row in current_board:
        dic = {}
        for num in row:
            if num == 0: continue
            if num in dic:
                dic[num] += 1
            elif num not in dic:
                dic[num] = 1

        tmp_list = []
        for num, cnt in dic.items():
            tmp_list.append([num, cnt])

        tmp_list.sort(key=lambda x: (x[1], x[0]))

        new_list = []
        for num, cnt in tmp_list:
            new_list.append(num)
            new_list.append(cnt)

        max_len = max(max_len, len(new_list))
        new_board.append(new_list)

    for i in range(len(new_board)):
        for _ in range(max_len - len(new_board[i])):
            new_board[i].append(0)

    return new_board


I, J, K = map(int, input().split())
I -= 1; J -= 1

board = [list(map(int, input().split())) for _ in range(3)]

if 0 <= I < 3 and 0 <= J < 3:
    if board[I][J] == K:
        print(0)
        exit()

for t in range(1, 101):

    if len(board) >= len(board[0]):
        board = rotate_board(board)

    elif len(board) < len(board[0]):
        board = list(map(list, zip(*board)))
        board = rotate_board(board)
        board = list(map(list, zip(*board)))

    # print("After operate")
    # for b in board:
    #     print(b)

    if 0 <= I < len(board) and 0 <= J < len(board[0]):
        if board[I][J] == K:
            print(t)
            exit()

print(-1)