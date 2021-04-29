from collections import deque


def next_location(next_i, next_j, di, dj):
    move_count = 0

    while True:
        next_i += di
        next_j += dj

        if board[next_i][next_j] == '#':
            next_i -= di
            next_j -= dj
            break

        move_count += 1

        if board[next_i][next_j] == 'O':
            break

    return next_i, next_j, move_count


def bfs():
    visit = [[[[False for _ in range(M)]for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visit[red_i][red_j][blue_i][blue_j] = True
    q = deque([[red_i, red_j, blue_i, blue_j, 0]])

    while q:
        c_red_i, c_red_j, c_blue_i, c_blue_j, move_count = q.popleft()

        if move_count == 10:
            return -1

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_red_i, next_red_j, red_count = next_location(c_red_i, c_red_j, di, dj)
            next_blue_i, next_blue_j, blue_count = next_location(c_blue_i, c_blue_j, di, dj)

            if board[next_blue_i][next_blue_j] == 'O':
                continue

            if board[next_red_i][next_red_j] == 'O':
                return move_count + 1

            if next_red_i == next_blue_i and next_red_j == next_blue_j:

                # 빨간 공이 파란 공보다 더 많이 움직였을 때
                if red_count > blue_count:
                    next_red_i -= di
                    next_red_j -= dj

                # 파란 공이 빨간 공보다 더 많이 움직였을 때
                elif red_count < blue_count:
                    next_blue_i -= di
                    next_blue_j -= dj

            if not visit[next_red_i][next_red_j][next_blue_i][next_blue_j]:
                visit[next_red_i][next_red_j][next_blue_i][next_blue_j] = True
                q.append([next_red_i, next_red_j, next_blue_i, next_blue_j, move_count + 1])

    return -1


N, M = map(int, input().split())
board = [input() for _ in range(N)]

red_i, red_j, blue_i, blue_j = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_i, red_j = i, j
        elif board[i][j] == 'B':
            blue_i, blue_j = i, j

print(bfs())