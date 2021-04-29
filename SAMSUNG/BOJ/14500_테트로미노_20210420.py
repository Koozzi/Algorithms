t = [
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [0, 2], [0, 3]],

    [[1, 0], [0, 1], [1, 1]],

    [[1, 0], [2, 0], [2, 1]],
    [[0, -1], [0, -2], [1, -2]],
    [[-1, 0], [-2, 0], [-2, -1]],
    [[0, 1], [0, 2], [-1, 2]],

    [[1, 0], [2, 0], [2, -1]],
    [[0, -1], [0, -2], [-1, -2]],
    [[-1, 0], [-2, 0], [-2, 1]],
    [[0, 1], [0, 2], [1, 2]],

    [[0, 1], [1, 1], [0, 2]],
    [[1, 0], [1, -1], [2, 0]],
    [[0, -1], [0, -2], [-1, -1]],
    [[-1, 0], [-2, 0], [-1, 1]],

    [[1, 0], [1, 1], [2, 1]],
    [[0, -1], [1, -1], [1, -2]],
    [[1, 0], [1, -1], [2, -1]],
    [[0, -1], [-1, -1], [-1, -2]]
]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        for idx in range(len(t)):
            _sum, count = board[i][j], 0
            for di, dj in t[idx]:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < N and 0 <= next_j < M:
                    _sum += board[next_i][next_j]
                    count += 1

            if count == 3:
                answer = max(answer, _sum)

print(answer)
