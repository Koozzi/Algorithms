from copy import deepcopy
from collections import deque
from sys import stdin


def find_section(_start_i, _start_j, current_board):
    visit[_start_i][_start_j] = True
    q = deque([[_start_i, _start_j]])
    count = 1
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < 2**N and 0 <= next_j < 2**N:
                if not visit[next_i][next_j] and current_board[next_i][next_j] > 0:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])
                    count += 1
    return count


def melt_ice(current_board):
    _new_board = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            ice_count = 0
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < 2 ** N and 0 <= next_j < 2 ** N:
                    if current_board[next_i][next_j] > 0:
                        ice_count += 1

            _new_board[i][j] = current_board[i][j]
            if _new_board[i][j] > 0 and ice_count < 3:
                _new_board[i][j] -= 1

    return _new_board


N, Q = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(2**N)]
sum_of_ice, largest_ice = 0, 0

for L in list(map(int, stdin.readline().split())):
    copied_board = deepcopy(board)

    # 격자마다 90도 회전하기
    for start_i in range(0, 2**N, 2**L):
        for start_j in range(0, 2**N, 2**L):
            tmp_board = [[0 for _ in range(2**L)] for _ in range(2**L)]
            for i in range(2**L):
                for j in range(2**L):
                    tmp_board[i][j] = copied_board[i + start_i][j + start_j]

            new_board = []
            for new_list in zip(*tmp_board):
                new_list = list(reversed(list(new_list)))
                new_board.append(new_list)

            for i in range(2**L):
                for j in range(2**L):
                    copied_board[i + start_i][j + start_j] = new_board[i][j]

    # 얼음 녹이기
    copied_board = melt_ice(copied_board)
    board = copied_board

# 가장큰 얼음 덩어리 찾기
visit = [[False for _ in range(2**N)] for _ in range(2**N)]
for i in range(2 ** N):
    for j in range(2 ** N):
        if not visit[i][j] and board[i][j] > 0:
            largest_ice = max(largest_ice, find_section(i, j, copied_board))

# 남은 얼음양의 합 구하기
for i in range(2**N):
    for j in range(2**N):
        if board[i][j] > 0:
            sum_of_ice += board[i][j]

print(sum_of_ice)
print(largest_ice)

