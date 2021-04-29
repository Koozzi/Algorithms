def make_security_section(start_i, start_j, _k):
    security_section = [[False for _ in range(N)] for _ in range(N)]
    for _i in range(N):
        for _j in range(N):
            if abs(_i - start_i) + abs(_j - start_j) < _k:
                security_section[_i][_j] = True

    _sub_home_count = 0
    for _i in range(N):
        for _j in range(N):
            if board[_i][_j] and security_section[_i][_j]:
                _sub_home_count += 1

    return _sub_home_count


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for k in range(N + 5):
        for i in range(N):
            for j in range(N):
                sub_home_count = make_security_section(i, j, k)
                if sub_home_count * M >= k**2 + (k-1)**2:
                    answer = max(answer, sub_home_count)

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