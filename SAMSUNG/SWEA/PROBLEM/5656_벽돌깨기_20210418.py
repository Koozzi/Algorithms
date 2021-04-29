from collections import deque
from copy import deepcopy


def find_start_i(j, current_board):
    for i in range(N):
        if current_board[i][j] > 0:
            return i

    return -1


def get_next_location(i, j, current_board):
    next_location = []
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    spread_number = current_board[i][j]
    for di, dj in move:
        I, J = i, j
        for _ in range(spread_number - 1):
            I += di
            J += dj
            next_location.append([I, J])

    return next_location


def board_go_down(current_board):
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(M):
        new_list = []
        for i in range(N - 1, -1, -1):
            if current_board[i][j] > 0:
                new_list.append(current_board[i][j])
        for i in range(len(new_list)):
            new_board[N - 1 - i][j] = new_list[i]

    return new_board


def break_block(start_i, start_j, current_board):
    break_block_list = [[start_i, start_j]]
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    while q:
        current_i, current_j = q.popleft()
        for next_i, next_j in get_next_location(current_i, current_j, current_board):
            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and current_board[next_i][next_j] > 0:
                    break_block_list.append([next_i, next_j])
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])

    for i, j in break_block_list:
        current_board[i][j] = 0

    return board_go_down(current_board)


def get_answer(current_board):
    ans = 0
    for i in range(N):
        for j in range(M):
            if current_board[i][j]:
                ans += 1
    return ans


def get_selected_j(cnt):
    global answer

    if cnt == K:
        copied_board = deepcopy(board)
        for j in stack:
            i = find_start_i(j, copied_board)
            if i != -1:
                copied_board = break_block(i, j, copied_board)
        answer = min(answer, get_answer(copied_board))
        return

    for j in range(M):
        stack.append(j)
        get_selected_j(cnt + 1)
        stack.pop()


T = int(input())
for t in range(1, T + 1):
    K, M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 2e9
    stack = []
    get_selected_j(0)

    print("#{} {}".format(t, answer))
