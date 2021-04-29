def on_wall(i, j):
    if i == N-1 or i == 0 or j == 0 or j == N-1:
        return True
    return False


def change_direction(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3


def miseng_move():

    new_board = [[[0, 0] for _ in range(N)] for _ in range(N)]
    tmp_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j][0] > 0:
                cnt, d = board[i][j]
                next_i = i + move[d][0]
                next_j = j + move[d][1]

                # 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고,
                # 이동방향이 반대로 바뀐다.
                if on_wall(next_i, next_j):
                    d = change_direction(d)
                    cnt //= 2

                tmp_board[next_i][next_j].append([cnt, d])

    for i in range(N):
        for j in range(N):
            if len(tmp_board[i][j]) == 1:
                new_board[i][j] = tmp_board[i][j][0]

            elif len(tmp_board[i][j]) > 1:
                sum_of_cnt = 0
                max_cnt, max_dir = 0, 0
                for cnt, final_d in tmp_board[i][j]:
                    sum_of_cnt += cnt
                    if cnt > max_cnt:
                        max_cnt = cnt
                        max_dir = final_d

                new_board[i][j] = [sum_of_cnt, max_dir]

    return new_board


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[[0, 0] for _ in range(N)] for _ in range(N)]
    move = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

    for _ in range(K):
        i, j, cnt, d = map(int, input().split())
        board[i][j] = [cnt, d]

    for _ in range(M):
        board = miseng_move()

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += board[i][j][0]

    print("#{} {}".format(t, answer))