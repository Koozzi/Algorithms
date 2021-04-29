def operate():
    max_len = 0
    for i in range(len(board)):
        dic = {}
        for num in board[i]:
            if num == 0:
                continue
            if num in dic:
                dic[num] += 1
            elif num not in dic:
                dic[num] = 1

        tmp_list = []
        for key, value in dic.items():
            tmp_list.append([key, value])
        tmp_list.sort(key=lambda x: (x[1], x[0]))

        new_list = []
        for key, value in tmp_list:
            new_list.append(key)
            new_list.append(value)
        max_len = max(max_len, len(new_list))

        board[i] = new_list

    for i in range(len(board)):
        for _ in range(max_len - len(board[i])):
            board[i].append(0)


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

if N - 1 < len(board) and M - 1 < len(board[0]):
    if board[N - 1][M - 1] == K:
        print(0)
        exit()

for answer in range(1, 101):

    if len(board) >= len(board[0]):
        operate()
    elif len(board) < len(board[0]):
        board = list(map(list, zip(*board)))
        operate()
        board = list(map(list, zip(*board)))

    if N - 1 < len(board) and M - 1 < len(board[0]):
        if board[N - 1][M - 1] == K:
            print(answer)
            exit()

print(-1)
