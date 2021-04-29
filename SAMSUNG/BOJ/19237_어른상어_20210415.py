def make_new_smell():
    for i in range(N):
        for j in range(N):
            if shark_board[i][j] > 0:
                smell_board[i][j] = [shark_board[i][j], K]


def remove_smell():
    for i in range(N):
        for j in range(N):
            if smell_board[i][j] != [0, 0]:
                smell_board[i][j][1] -= 1
                if smell_board[i][j][1] == 0:
                    smell_board[i][j] = [0, 0]


def shark_move():
    new_shark_board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if shark_board[i][j] > 0:
                shark_num = shark_board[i][j]
                shark_dir = shark_info[shark_num]

                found_empty_place = False

                for d in shark_priority[shark_num][shark_dir]:
                    I = i + move[d][0]
                    J = j + move[d][1]
                    if 0 <= I < N and 0 <= J < N:
                        if smell_board[I][J] == [0, 0]:
                            found_empty_place = True
                            if new_shark_board[I][J] == 0 \
                                    or (new_shark_board[I][J] > 0 and new_shark_board[I][J] > shark_num):
                                new_shark_board[I][J] = shark_num
                                shark_info[shark_num] = d
                            break

                if found_empty_place:
                    continue

                for d in shark_priority[shark_num][shark_dir]:
                    I = i + move[d][0]
                    J = j + move[d][1]
                    if 0 <= I < N and 0 <= J < N:
                        if smell_board[I][J][0] == shark_num:
                            new_shark_board[I][J] = shark_num
                            shark_info[shark_num] = d
                            break

    return new_shark_board


def check_shark_left():
    shark_count = 0
    for i in range(N):
        for j in range(N):
            if shark_board[i][j] > 0:
                shark_count += 1
                if shark_count > 1:
                    return False
    return True


N, M, K = map(int, input().split())
shark_board = [list(map(int, input().split())) for _ in range(N)]
smell_board = [[[0, 0] for _ in range(N)] for _ in range(N)]
move = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

shark_info = [[]]
for d in list(map(int, input().split())):
    shark_info.append(d)

shark_priority = [[]]
for _ in range(M):
    shark_priority.append([[0]]+[list(map(int, input().split())) for _ in range(4)])

for t in range(1, 1001):
    remove_smell()
    make_new_smell()
    shark_board = shark_move()
    if check_shark_left():
        print(t)
        exit()

print(-1)


