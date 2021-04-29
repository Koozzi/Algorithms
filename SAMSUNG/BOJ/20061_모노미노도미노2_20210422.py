def stack_block(t, x, y):
    if t == 1:
        # 파란색 부분
        blue_y = 9
        for j in range(5, 10):
            if board[x][j] == 1:
                blue_y = j - 1
                break
        board[x][blue_y] = 1

        # 초록색 부분
        green_x = 9
        for i in range(5, 10):
            if board[i][y] == 1:
                green_x = i - 1
                break
        board[green_x][y] = 1

    elif t == 2:
        blue_y = 9
        for j in range(5, 10):
            if board[x][j] == 1:
                blue_y = j - 1
                break
        board[x][blue_y - 1] = 1
        board[x][blue_y] = 1

        green_x = 9
        for i in range(5, 10):
            if board[i][y] == 1 or board[i][y+1] == 1:
                green_x = i - 1
                break
        board[green_x][y] = 1
        board[green_x][y + 1] = 1

    elif t == 3:
        blue_y = 9
        for j in range(5, 10):
            if board[x][j] == 1 or board[x+1][j] == 1:
                blue_y = j - 1
                break
        board[x][blue_y] = 1
        board[x + 1][blue_y] = 1

        green_x = 9
        for i in range(5, 10):
            if board[i][y] == 1:
                green_x = i - 1
                break
        board[green_x - 1][y] = 1
        board[green_x][y] = 1


    # print("After stack block")
    # for i in board:
    #     print(i)


def green_go_down(start_x, size):
    for _x in range(start_x, 1, -1):
        for j in range(4):
            board[_x][j] = board[_x - size][j]


def blue_go_right(start_y, size):
    for _y in range(start_y, 1, -1):
        for i in range(4):
            board[i][_y] = board[i][_y - size]


def erase_block():
    global score

    y_size, last_y = 0, 0
    for j in range(4, 10):
        _sum = 0
        for i in range(4):
            _sum += board[i][j]

        if _sum == 4:
            for i in range(4):
                board[i][j] = 0
            y_size += 1
            last_y = j


    x_size, last_x = 0, 0
    for i in range(4, 10):
        _sum = 0
        for j in range(4):
            _sum += board[i][j]

        if _sum == 4:
            for j in range(4):
                board[i][j] = 0
            x_size += 1
            last_x = i

    # print("After erase block")
    # for i in board:
    #     print(i)

    score += (y_size + x_size)
    blue_go_right(last_y, y_size)
    green_go_down(last_x, x_size)

    # print("After remove block and pushed")
    # for i in board:
    #     print(i)


def special():
    # blue
    count = 0
    for j in range(4, 6):
        for i in range(4):
            if board[i][j]:
                count += 1
                break

    for j in range(9, 3, -1):
        for i in range(4):
            board[i][j] = board[i][j - count]


    # green
    count = 0
    for i in range(4, 6):
        for j in range(4):
            if board[i][j]:
                count += 1
                break

    for i in range(9, 3, -1):
        for j in range(4):
            board[i][j] = board[i - count][j]


board = [[0 for _ in range(10)] for _ in range(10)]

for i in range(4, 10):
    for j in range(4, 10):
        board[i][j] = 7

score = 0
K = int(input())
for _ in range(K):
    t, x, y = map(int, input().split())
    stack_block(t, x, y)    # 블록을 초록, 파란 부분에 쌓는다.
    erase_block()           # 행이나 열이 꽉 차있는 경우를 체크하고 그 칸 수만큼 내련준다.
    special()

    # print(t, x, y)
    # for i in board:
    #     print(i)

block_conut = 0
for i in range(6, 10):
    for j in range(4):
        if board[i][j]:
            block_conut += 1

for j in range(6, 10):
    for i in range(4):
        if board[i][j]:
            block_conut += 1

print(score)
print(block_conut)


"""
8
1 1 1
2 3 0
3 2 2
3 2 3
3 1 3
2 0 0
3 2 0
3 1 2
"""