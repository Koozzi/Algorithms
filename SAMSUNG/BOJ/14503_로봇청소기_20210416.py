N, M = map(int, input().split())
i, j, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
clean = [[False for _ in range(M)] for _ in range(N)]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0

while True:

    # 현재 위치를 청소한다
    if not clean[i][j]:
        clean[i][j] = True
        answer += 1

    # 현재 위치에서, 현재 방향을 기준으로 왼쪽 방향을 탐색한다.
    tmp_d = d
    found_not_cleaned_spot = False
    for _ in range(4):
        tmp_d = (tmp_d - 1) % 4
        tmp_i = i + move[tmp_d][0]
        tmp_j = j + move[tmp_d][1]

        if not clean[tmp_i][tmp_j] and board[tmp_i][tmp_j] == 0:
            found_not_cleaned_spot = True
            i, j, d = tmp_i, tmp_j, tmp_d
            break

    if found_not_cleaned_spot:
        continue

    # 청소할 수 있는 공간을 찾지 못함
    # 뒤로 빠꾸할 수 있나?
    back_i = i - move[d][0]
    back_j = j - move[d][1]

    if board[back_i][back_j] == 0:
        i, j = back_i, back_j
    else:
        break

print(answer)