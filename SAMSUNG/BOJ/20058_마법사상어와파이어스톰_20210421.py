from collections import deque


def rotate_board(current_board):
    _new_board = []
    for l in zip(*current_board):
        _new_board.append(list(reversed(list(l))))
    return _new_board


def remove_ice(current_board):
    _new_board = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            ice_count = 0
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < 2**N and 0 <= next_j < 2**N:
                    if current_board[next_i][next_j] > 0:
                        ice_count += 1

            _new_board[i][j] = board[i][j]
            if ice_count < 3 and _new_board[i][j] > 0:
                _new_board[i][j] -= 1

    return _new_board


def get_ice_section(start_i, start_j):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    count = 1
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < 2**N and 0 <= next_j < 2**N:
                if board[next_i][next_j] > 0 and not visit[next_i][next_j]:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])
                    count += 1

    return count


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
commands = list(map(int, input().split()))

for L in commands:

    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            new_board = [[0 for _ in range(2**L)] for _ in range(2**L)]
            for sub_i in range(i, i + 2**L):
                for sub_j in range(j, j + 2**L):
                    new_board[sub_i-i][sub_j-j] = board[sub_i][sub_j]

            new_board = rotate_board(new_board)

            for sub_i in range(i, i + 2**L):
                for sub_j in range(j, j + 2**L):
                    board[sub_i][sub_j] = new_board[sub_i-i][sub_j-j]

    # print("After rotate")
    # for b in board:
    #     print(b)

    board = remove_ice(board)
    # print("After melt")
    # for b in board:
    #     print(b)

total_ice_amount = 0
for row in board:
    total_ice_amount += sum(row)

max_ice_section = 0
visit = [[False for _ in range(2**N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if not visit[i][j] and board[i][j] > 0:
            max_ice_section = max(max_ice_section, get_ice_section(i, j))

print(total_ice_amount)
print(max_ice_section)
