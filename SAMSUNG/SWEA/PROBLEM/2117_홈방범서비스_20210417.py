"""
22:50
"""


def make_safe_area(i, j, k):
    for _i in range(N):
        for _j in range(N):
            if abs(_i - i) + abs(_j - j) < k:
                safe[_i][_j] = True


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for k in range(N+2):
        for i in range(N):
            for j in range(N):
                safe = [[False for _ in range(N)] for _ in range(N)]
                make_safe_area(i, j, k)

                current_home_count = 0
                for sub_i in range(N):
                    for sub_j in range(N):
                        if safe[sub_i][sub_j] and board[sub_i][sub_j]:
                            current_home_count += 1

                if k * k + (k - 1) * (k - 1) <= current_home_count * M:
                    answer = max(answer, current_home_count)

    print("#{} {}".format(t, answer))

"""
1
8 3
0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0
1 0 0 0 0 0 0 0
"""