def is_possible(l):
    visit = [False for _ in range(N)]

    start_idx = 0
    for i in range(1, N):
        prev_height = l[i-1]
        curr_height = l[i]

        if abs(prev_height - curr_height) > 1:
            return False

        if prev_height > curr_height:
            start_idx = i
            continue

        if prev_height < curr_height:
            if start_idx <= i - M:
                start_idx = i
                for sub_i in range(i-M, i):
                    visit[sub_i] = True
            else:
                return False

    start_idx = N-1
    for i in range(N-2, -1, -1):
        prev_height = l[i+1]
        curr_height = l[i]

        if prev_height > curr_height:
            start_idx = i
            continue

        if prev_height < curr_height:
            if start_idx >= i + M:
                start_idx = i
                for sub_i in range(i+1, i+M+1):
                    if visit[sub_i]:
                        return False
            else:
                return False

    return True


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for row in board:
        if is_possible(row):
            answer += 1

    board = list(map(list, zip(*board)))
    for row in board:
        if is_possible(row):
            answer += 1

    print("#{} {}".format(t, answer))
    # print(is_possible([1, 2, 3, 4, 5, 6]))
    # print(is_possible([2, 2, 2, 2, 2, 2]))
    # print(is_possible([1, 1, 2, 2, 1, 1]))
    # print(is_possible([2, 2, 1, 1, 2, 2]))
    # print(is_possible([1, 4, 4, 4, 4, 4]))
    # print(is_possible([1, 1, 2, 2, 3, 3]))
    # print(is_possible([3, 3, 2, 2, 1, 1]))


"""
1
6 2
3 3 3 2 1 1
3 3 3 2 2 1
3 3 3 3 3 2
2 2 3 2 2 2
2 2 3 2 2 2
2 2 2 2 2 2
"""