# block_change_direction[d][n]
# 현재 방향과 블록의 번호에 따른 방향 변화
block_change_direction = [
    [0, 2, 1, 3, 2, 2],
    [0, 3, 3, 2, 0, 3],
    [0, 1, 0, 0, 3, 0],
    [0, 0, 2, 1, 1, 1]
]


def check_out_of_board(i, j, d):
    if i < 0:
        return 0, j, 2, 1
    if i > N-1:
        return N-1, j, 0, 1
    if j < 0:
        return i, 0, 1, 1
    if j > N-1:
        return i, N-1, 3, 1
    return i, j, d, 0


def make_wormhole_info():
    tmp_wormhole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 5:
                tmp_wormhole[board[i][j]].append((i, j))

    for w in tmp_wormhole:
        if not w: continue
        wormhole[board[w[0][0]][w[0][1]]][(w[0][0], w[0][1])] = (w[1][0], w[1][1])
        wormhole[board[w[0][0]][w[0][1]]][(w[1][0], w[1][1])] = (w[0][0], w[0][1])


def solve(start_i, start_j, start_d):
    i, j, d = start_i, start_j, start_d
    count = 0
    while True:

        # 블랙홀을 만났을 경우
        if board[i][j] == -1:
            return count

        if 1 <= board[i][j] <= 5:
            d = block_change_direction[d][board[i][j]]
            count += 1

        elif 6 <= board[i][j] <= 10:
            i, j = wormhole[board[i][j]][(i, j)]

        i += move[d][0]
        j += move[d][1]

        i, j, d, c = check_out_of_board(i, j, d)
        count += c

        if i == start_i and j == start_j:
            return count


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    wormhole = [{} for _ in range(11)]
    make_wormhole_info()
    answer = 0

    for i in range(N):
        for j in range(N):
            for d in range(4):
                if board[i][j] == 0:
                    answer = max(answer, solve(i, j, d))

    print("#{} {}".format(t, answer))

"""
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
6
1 1 1 1 1 1
1 1 -1 1 1 1
1 -1 0 -1 1 1
1 1 -1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
"""