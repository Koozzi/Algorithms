from collections import deque


# 특별한 부분에 도형이 쌓여있는지 체크하고
# 쌓여있는 만큼 밀어내는 함수
def middle(current_board, state):
    if state == 'green':
        current_board = list(map(list, zip(*current_board)))

    count = 0
    for j in range(2):
        for i in range(4):
            if current_board[i][j] == 1:
                count += 1
                break

    for _ in range(count):
        for i in range(4):
            q = deque(current_board[i])
            q.pop()
            q.appendleft(0)
            current_board[i] = list(q)

    if state == 'green':
        current_board = list(map(list, zip(*current_board)))

    return current_board


# t, x, y가 주어지면 green과 blue에 샇을 위치
def stack_block(current_board, state, t, x, y):
    x1, y1, x2, y2 = 0, 0, 0, 0

    if state == 'green':
        if t == 1:
            x1, x2 = 1, 1
            y1, y2 = y, y
        elif t == 2:
            x1, x2 = 1, 1
            y1, y2 = y, y + 1
        elif t == 3:
            x1, x2 = 0, 1
            y1, y2 = y, y

        for i in range(2, 6):
            if current_board[i][y1] or current_board[i][y2]:
                break
            x1, x2 = i, i
            if t == 3:
                x1 -= 1

    if state == 'blue':
        if t == 1:
            x1, x2 = x, x
            y1, y2 = 1, 1
        elif t == 2:
            x1, x2 = x, x
            y1, y2 = 0, 1
        elif t == 3:
            x1, x2 = x, x + 1
            y1, y2 = 1, 1

        for j in range(2, 6):
            if current_board[x1][j] or current_board[x2][j]:
                break
            y1, y2 = j, j
            if t == 2:
                y1 -= 1

    return x1, y1, x2, y2


def green_go_down_one(start_i):
    for j in range(4):
        for i in range(start_i, 0, -1):
            green_board[i][j] = green_board[i-1][j]
        green_board[0][j] = 0


def blue_go_down(start_j):
    for i in range(4):
        for j in range(start_j, 0, -1):
            blue_board[i][j] = blue_board[i][j-1]
        blue_board[i][0] = 0


N = int(input())
red_board = [[0 for _ in range(4)] for _ in range(4)]
blue_board = [[0 for _ in range(6)] for _ in range(4)]
green_board = [[0 for _ in range(4)] for _ in range(6)]
score = 0

for _ in range(N):
    t, x, y = map(int, input().split())
    x1, y1, x2, y2 = stack_block(blue_board, 'blue', t, x, y)
    blue_board[x1][y1] = 1
    blue_board[x2][y2] = 1
    y_list = list(set([y1, y2]))

    for j in y_list:
        all_same = True
        for i in range(4):
            if blue_board[i][j] == 0:
                all_same = False
                break
        if all_same:
            score += 1
            for i in range(4):
                blue_board[i][j] = 0

            blue_go_down(j)

    blue_board = middle(blue_board, 'blue')

    x1, y1, x2, y2 = stack_block(green_board, 'green', t, x, y)
    green_board[x1][y1] = 1
    green_board[x2][y2] = 1
    x_list = list(set([x1, x2]))

    for i in x_list:
        all_same = True
        for j in range(4):
            if green_board[i][j] == 0:
                all_same = False
                break

        if all_same:
            score += 1
            for j in range(4):
                green_board[i][j] = 0

            green_go_down_one(i)

    green_board = middle(green_board, 'green')

# Answer section
block_count = 0
for i in range(6):
    for j in range(4):
        if green_board[i][j]:
            block_count += 1
for i in range(4):
    for j in range(6):
        if blue_board[i][j]:
            block_count += 1
print(score)
print(block_count)

"""
9
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
3 0 3
3 0 3
"""