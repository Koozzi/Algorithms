T = int(input())
for t in range(1, T + 1):
    answer = 2e9
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    w_idx, b_idx, r_idx = 0, 0, 0
    for w in range(1, N):
        for b in range(1, N):
            for r in range(1, N):
                if w + b + r == N:
                    change_count = 0
                    for i in range(w):
                        for j in range(M):
                            if board[i][j] != 'W':
                                change_count += 1

                    for i in range(w, w + b):
                        for j in range(M):
                            if board[i][j] != 'B':
                                change_count += 1

                    for i in range(w + b, N):
                        for j in range(M):
                            if board[i][j] != 'R':
                                change_count += 1

                    answer = min(answer, change_count)

    print("#{} {}".format(t, answer))


"""
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
"""