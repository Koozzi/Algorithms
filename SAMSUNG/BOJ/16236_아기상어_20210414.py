from collections import deque


def find_fish(start_i, start_j):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    _fish = []
    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j]:
                    if board[next_i][next_j] <= shark_s:
                        visit[next_i][next_j] = True
                        q.append([next_i, next_j, current_d + 1])
                        if 0 < board[next_i][next_j] < shark_s:
                            _fish.append([current_d + 1, next_i, next_j])

    _fish.sort()
    return _fish


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

shark_i, shark_j, shark_s = 0, 0, 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_i, shark_j = i, j

answer, shark_tmp = 0, 0

while True:
    fish = find_fish(shark_i, shark_j)

    if not fish:
        break

    # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다
    shark_tmp += 1
    if shark_tmp == shark_s:
        shark_tmp = 0
        shark_s += 1

    distance, fish_i, fish_j = fish[0]

    board[fish_i][fish_j] = 0
    board[shark_i][shark_j] = 0
    shark_i, shark_j = fish_i, fish_j
    board[shark_i][shark_j] = 9
    answer += distance

print(answer)


