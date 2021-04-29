def remove_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j] != [0, 0]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = [0, 0]

    # print("After remove smell (smell)")
    # for s in smell:
    #     print(s)


def make_new_smell():
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                smell[i][j] = [board[i][j], K]

    # print("After make new smell (smell)")
    # for b in smell:
    #     print(b)


def shark_move():

    new_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                continue

            shark_num, shark_dir = board[i][j], direction[board[i][j]]
            found_next_location = False
            for d in priority[shark_num][shark_dir]:
                next_i = i + move[d][0]
                next_j = j + move[d][1]
                if 0 <= next_i < N and 0 <= next_j < N:
                    if smell[next_i][next_j] == [0, 0]:
                        found_next_location = True
                        if new_board[next_i][next_j] == 0 or new_board[next_i][next_j] > shark_num:
                            new_board[next_i][next_j] = shark_num
                            direction[shark_num] = d
                        break

            if found_next_location:
                continue

            for d in priority[shark_num][shark_dir]:
                next_i = i + move[d][0]
                next_j = j + move[d][1]
                if 0 <= next_i < N and 0 <= next_j < N:
                    if smell[next_i][next_j][0] == shark_num:
                        new_board[next_i][next_j] = shark_num
                        direction[shark_num] = d
                        break

    # print("After shark move (board)")
    # for i in new_board:
    #     print(i)

    return new_board


def check_only_one_shark_left():
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                count += 1
                if count == 2:
                    return False

    return True


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
direction = [0] + list(map(int, input().split()))
move = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
priority = [[]]
for _ in range(1, M + 1):
    sub_priority = [0] + [list(map(int, input().split())) for _ in range(4)]
    priority.append(sub_priority)

answer = -1
for t in range(1, 1001):
    remove_smell()
    make_new_smell()
    board = shark_move()

    if check_only_one_shark_left():
        answer = t
        break

print(answer)