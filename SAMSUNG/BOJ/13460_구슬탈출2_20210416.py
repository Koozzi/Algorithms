"""
격자 NxM
가장 바깥 행과 열은 모두 막혀져 있음
구멍은 한 개
파란 구슬은 구멍에 들어가면 안 됨
"""
from collections import deque


def init_red_blue_ball():
    global init_red_i,  init_red_j, init_blue_i, init_blue_j
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                init_red_i, init_red_j = i, j
            elif board[i][j] == 'B':
                init_blue_i, init_blue_j = i, j


def next_location(next_i, next_j, di, dj):

    move_count = 0
    while board[next_i + di][next_j + dj] != '#' and board[next_i][next_j] != 'O':
        next_i += di
        next_j += dj
        move_count += 1
    return next_i, next_j, move_count


def move_ball():
    visit = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visit[init_red_i][init_red_j][init_blue_i][init_blue_j] = True
    q = deque([[init_red_i, init_red_j, init_blue_i, init_blue_j, 0]])

    while q:
        cred_i, cred_j, cblue_i, cblue_j, d = q.popleft()

        if d == 10:
            return -1

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nred_i, nred_j, red_count = next_location(cred_i, cred_j, di, dj)
            nblue_i, nblue_j, blue_count = next_location(cblue_i, cblue_j, di, dj)

            if board[nblue_i][nblue_j] == 'O':
                continue

            if board[nred_i][nred_j] == 'O':
                return d + 1

            if nred_i == nblue_i and nred_j == nblue_j:
                if red_count < blue_count:
                    nblue_i -= di
                    nblue_j -= dj
                elif red_count > blue_count:
                    nred_i -= di
                    nred_j -= dj

            if not visit[nred_i][nred_j][nblue_i][nblue_j]:
                visit[nred_i][nred_j][nblue_i][nblue_j] = True
                q.append([nred_i, nred_j, nblue_i, nblue_j, d+1])

    return -1


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
init_red_i, init_red_j = 0, 0
init_blue_i, init_blue_j = 0, 0
init_red_blue_ball()
print(move_ball())


