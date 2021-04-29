from itertools import combinations


def test():
    for j in range(M):
        same_count = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]:
                same_count += 1
                if same_count == K:
                    break
            elif board[i-1][j] != board[i][j]:
                same_count = 1
        if same_count < K:
            return False
    return True


def decide_type(cnt, max_cnt):
    global answer, answer_found

    if answer_found:
        return

    if cnt == max_cnt:

        copied_row_dictionary = {}
        for _type, i in zip(stack, i_list):
            copied_row_dictionary[i] = board[i]
            board[i] = [_type for _ in range(M)]

        if test():
            answer = cnt
            answer_found = True

        for i, row in copied_row_dictionary.items():
            board[i] = row

        return

    for _type in range(2):
        stack.append(_type)
        decide_type(cnt + 1, max_cnt)
        stack.pop()


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    if test() or K == 1:
        print("#{} {}".format(t, 0))
        continue

    answer = 0
    answer_found = False
    for n in range(1, K + 1):
        if answer_found: break
        for i_list in combinations(range(N), n):
            if answer_found: break
            stack = []
            decide_type(0, n)

    print("#{} {}".format(t, answer))


"""
1            
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
"""
