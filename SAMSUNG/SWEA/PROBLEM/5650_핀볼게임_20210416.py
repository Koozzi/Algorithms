"""
20:44

"""
direction_block = [
    [0, 0, 0, 0, 0, 0],
    [0, 3, 2, 4, 3, 3],
    [0, 4, 4, 3, 1, 4],
    [0, 2, 1, 1, 4, 1],
    [0, 1, 3, 2, 2, 2],
]


def next_wormhole(i, j, wormhole_number):
    for wi, wj in wormhole[wormhole_number]:
        if wi != i or wj != j:
            return wi, wj


def get_max_score(start_i, start_j, start_d):

    score = 0
    d = start_d
    i = start_i + move[d][0]
    j = start_j + move[d][1]

    while True:

        if i == start_i and j == start_j:
            return score

        if 0 <= i < N and 0 <= j < N:

            if board[i][j] == -1:
                return score

            if 1 <= board[i][j] <= 5:
                d = direction_block[d][board[i][j]]
                score += 1

            elif board[i][j] >= 6:
                i, j = next_wormhole(i, j, board[i][j])

        else:
            if d == 1: d = 3
            elif d == 2: d = 4
            elif d == 3: d = 1
            elif d == 4: d = 2
            score += 1

        i += move[d][0]
        j += move[d][1]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [[], [-1, 0], [0, 1], [1, 0], [0, -1]]

    wormhole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                wormhole[board[i][j]].append([i, j])

    answer = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for d in range(1, 5):
                    answer = max(answer, get_max_score(i, j, d))

    print("#{} {}".format(t, answer))


