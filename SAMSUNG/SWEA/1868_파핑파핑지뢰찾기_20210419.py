from collections import deque


def bfs(start_i, start_j):
    q = deque([[start_i, start_j]])
    while q:
        current_i, current_j = q.popleft()

        for di, dj in move:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] == '.':
                visit[next_i][next_j] = True
                next_count = count_boom(next_i, next_j)
                if next_count == 0:
                    q.append([next_i, next_j])


def count_boom(_i, _j):
    count = 0
    for di, dj in move:
        I = _i + di
        J = _j + dj
        if 0 <= I < N and 0 <= J < N:
            if board[I][J] == '*':
                count += 1

    return count


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    answer = 0

    start_index = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                start_index.append([i, j, count_boom(i, j)])

    start_index.sort(key=lambda x: x[2])
    for i, j, c in start_index:
        if not visit[i][j]:
            visit[i][j] = True
            answer += 1
            if c == 0:
                bfs(i, j)

    print("#{} {}".format(t, answer))