from collections import deque


def bfs(start_i, start_j):
    _moved = False
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    current_section = [[start_i, start_j]]
    section_cnt, section_sum = 1, board[start_i][start_j]
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j]:
                    if L <= abs(board[next_i][next_j] - board[current_i][current_j]) <= R:
                        visit[next_i][next_j] = True
                        q.append([next_i, next_j])
                        current_section.append([next_i, next_j])
                        section_sum += board[next_i][next_j]
                        section_cnt += 1
                        _moved = True

    population = section_sum // section_cnt
    for i, j in current_section:
        board[i][j] = population
    return _moved


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while True:
    visit = [[False for _ in range(N)] for _ in range(N)]
    moved = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if bfs(i, j):
                    moved = True

    if moved:
        answer += 1

    elif not moved:
        print(answer)
        break
