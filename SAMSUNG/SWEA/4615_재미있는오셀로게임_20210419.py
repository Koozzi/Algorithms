def find_direction(start_i, start_j, _color):

    possible_d = []
    for d in range(8):
        I, J = start_i, start_j
        while True:
            I += move[d][0]
            J += move[d][1]
            
            if not 1 <= I <= N or not 1 <= J <= N:
                break

            if board[I][J] == '.':
                break

            if board[I][J] == _color:
                possible_d.append(d)
                break

    return possible_d


def make_init_board(size):
    init_board = [['.' for _ in range(size + 1)] for _ in range(size + 1)]
    init_index = size // 2
    init_board[init_index][init_index] = 'W'
    init_board[init_index + 1][init_index] = 'B'
    init_board[init_index][init_index + 1] = 'B'
    init_board[init_index + 1][init_index + 1] = 'W'
    return init_board


def flip(start_i, start_j, d, _color):
    I, J = start_i, start_j
    while True:
        I += move[d][0]
        J += move[d][1]
        if board[I][J] == _color:
            break
        board[I][J] = _color


T = int(input())
for t in range(1, T+1):
    move = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    N, M = map(int, input().split())
    board = make_init_board(N)
    for _ in range(M):
        # 1 : black / 2 : white
        j, i, color = map(int, input().split())

        if color == 1: color = 'B'
        elif color == 2: color = 'W'

        board[i][j] = color
        possible_erase_direction = find_direction(i, j, color)
        for d in possible_erase_direction:
            flip(i, j, d, color)

    black, white = 0, 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 'B': black += 1
            elif board[i][j] == 'W': white += 1

    print("#{} {} {}".format(t, black, white))


"""
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
"""