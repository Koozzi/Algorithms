N, M = map(int, input().split())
I, J, D = map(int, input().split())

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
board = [list(map(int, input().split())) for _ in range(N)]
clean = [[False for _ in range(M)] for _ in range(N)]
clean_count = 0

while True:

    # 현재 위치를 청소한다.
    if not clean[I][J]:
        clean[I][J] = True
        clean_count += 1

    found_not_cleaned_spot = False
    for _ in range(4):
        D = (D - 1) % 4
        next_i = I + move[D][0]
        next_j = J + move[D][1]

        if not clean[next_i][next_j] and board[next_i][next_j] == 0:
            found_not_cleaned_spot = True
            I, J = next_i, next_j
            break

    if found_not_cleaned_spot:
        continue

    # 바라보는 방향을 유지한 채로 한 칸 후진
    I -= move[D][0]
    J -= move[D][1]

    # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
    if board[I][J] == 1:
        break

print(clean_count)