def change_visit(start_i, start_j, state):
    for j in range(start_j, start_j + M):
        visit[start_i][j] = state


def get_sum_of_honey(start_i, start_j):
    _sum_of_honey = 0
    for j in range(start_j, start_j + M):
        _sum_of_honey += board[start_i][j]
    return _sum_of_honey


def check_sub(start_i, start_j):
    for j in range(start_j, start_j + M):
        if visit[start_i][j]:
            return False
    return True


def get_valid_sum_of_honey(start, cnt, max_cnt, _sum, l, state, stack):
    global first_max, second_max

    if cnt == max_cnt:
        price = 0
        if state == 'first' and _sum <= C:
            for honey in stack:
                price += honey**2
            first_max = max(first_max, price)
        elif state == 'second' and _sum <= C:
            for honey in stack:
                price += honey ** 2
            second_max = max(second_max, price)

        return

    for i in range(start, M):
        stack.append(l[i])
        get_valid_sum_of_honey(i + 1, cnt + 1, max_cnt, _sum + l[i], l, state, stack)
        stack.pop()


def solve(ai, aj, bi, bj):
    global first_max, second_max

    first_max, second_max = 0, 0

    first_honey = board[ai][aj:aj+M]
    second_honey = board[bi][bj:bj+M]
    stack = []
    for max_cnt in range(1, M + 1):
        get_valid_sum_of_honey(0, 0, max_cnt, 0, first_honey, 'first', stack)
        get_valid_sum_of_honey(0, 0, max_cnt, 0, second_honey, 'second', stack)

    return first_max + second_max


T = int(input())
for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    first_max, second_max = 0, 0
    answer = 0

    for i in range(N):
        for j in range(N - M + 1):
            change_visit(i, j, True)
            for sub_i in range(i, N):
                for sub_j in range(N - M + 1):
                    if check_sub(sub_i, sub_j):
                        answer = max(answer, solve(i, j, sub_i, sub_j))
            change_visit(i, j, False)

    print("#{} {}".format(t, answer))

"""
1
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7

3 3 10
7 2 9
6 6 6
5 5 7
"""