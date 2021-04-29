def rotate_board(_board):
    new_board = []
    for b in zip(*_board):
        new_board.append(list(reversed(b)))

    return new_board


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    board_90 = rotate_board(board)
    board_180 = rotate_board(board_90)
    board_270 = rotate_board(board_180)

    print("#{}".format(t))
    for _90, _180, _270 in zip(board_90, board_180, board_270):
        print(''.join(_90) + ' ' + ''.join(_180) + ' ' + ''.join(_270) )

"""
2
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
"""