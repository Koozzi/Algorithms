"""
00:05
"""
from itertools import combinations


def test(current_board):
    for j in range(M):
        same_count = 1
        valid = False
        for i in range(1, N):
            if current_board[i][j] == current_board[i - 1][j]:
                same_count += 1
                if same_count == K:
                    valid = True
                    break
            else:
                same_count = 1
                if i + K > N:
                    return False
        if not valid:
            return False

    return True


def solve(_cnt, max_cnt):
    global answer, answer_found

    if answer_found:
        return

    if _cnt == max_cnt:

        dic = {}
        for selected_index, _type in zip(i_index, stack):
            dic[selected_index] = board[selected_index]
            board[selected_index] = [_type for _ in range(M)]

        if test(board):
            answer = _cnt
            answer_found = True

        for index, row in dic.items():
            board[index] = row

        return

    for i in range(2):
        stack.append(i)
        solve(_cnt + 1, max_cnt)
        stack.pop()


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer_found = False
    answer = 0

    if K == 1:
        print("#{} {}".format(t, answer))
        continue

    if test(board):
        print("#{} {}".format(t, answer))
        continue

    for cnt in range(1, K+1):
        if answer_found: break
        for i_index in combinations(range(N), cnt):
            if answer_found: break
            stack = []
            solve(0, cnt)

    print("#{} {}".format(t, answer))