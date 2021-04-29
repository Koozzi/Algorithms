"""
시작 23:43
종료 01:12
"""
from collections import deque
from copy import deepcopy


def get_i(j, current_board):
    for i in range(N):
        if current_board[i][j] > 0:
            return i
    return -1


def wall_down(current_board):

    for j in range(M):
        q = deque([])

        for i in range(N-1, -1, -1):
            if current_board[i][j] > 0:
                q.append(current_board[i][j])

        for i in range(N-1, -1, -1):
            current_board[i][j] = 0

        for i in range(N-1, -1, -1):
            if q:
                current_board[i][j] = q.popleft()
            else:
                break

    return current_board


def get_next_location(i, j, current_board):
    next_location = []
    spread_number = current_board[i][j]
    for di, dj in move:
        next_i, next_j = i, j
        for _ in range(spread_number-1):
            next_i += di
            next_j += dj
            if 0 <= next_i < N and 0 <= next_j < M:
                if current_board[next_i][next_j] > 0:
                    next_location.append([next_i, next_j])

    return next_location


def break_wall(start_i, start_j, copied_board):
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    wall_list = [[start_i, start_j]]
    while q:
        current_i, current_j = q.popleft()
        for next_i, next_j in get_next_location(current_i, current_j, copied_board):
            if not visit[next_i][next_j]:
                visit[next_i][next_j] = True
                q.append([next_i, next_j])
                wall_list.append([next_i, next_j])

    return wall_list


def get_ball_location(cnt):
    global answer
    if cnt == K:
        copied_board = deepcopy(board)

        for j in stack:
            i = get_i(j, copied_board)
            if i == -1:
                return
            break_wall_list = break_wall(i, j, copied_board)
            for break_i, break_j in break_wall_list:
                copied_board[break_i][break_j] = 0
            copied_board = wall_down(copied_board)

        ball_left = 0
        for i in range(N):
            for j in range(M):
                if copied_board[i][j] > 0:
                    ball_left += 1

        answer = min(answer, ball_left)
        return

    for j in range(M):
        stack.append(j)
        get_ball_location(cnt + 1)
        stack.pop()


T = int(input())

for t in range(1, T+1):

    K, M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    answer = 2e9

    stack = []
    get_ball_location(0)

    if answer == 2e9:
        answer = 0

    print("#{} {}".format(t, answer))











    # copied_board = deepcopy(board)
    # break_wall_list = break_wall(1, 2)
    # for break_i, break_j in break_wall_list:
    #     copied_board[break_i][break_j] = 0
    # wall_down()
    #
    # break_wall_list = break_wall(2, 2)
    # for break_i, break_j in break_wall_list:
    #     copied_board[break_i][break_j] = 0
    # wall_down()
    #
    # break_wall_list = break_wall(8, 6)
    # for break_i, break_j in break_wall_list:
    #     copied_board[break_i][break_j] = 0
    # wall_down()
    #
    # for i in copied_board:
    #     print(i)