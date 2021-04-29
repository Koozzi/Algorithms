from collections import deque


def delete_same_number(si, sj):
    visit[si][sj] = True
    q = deque([[si, sj]])
    found_same_number = False
    delete_index = [[si, sj]]
    while q:
        ci, cj = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = ci + di
            nj = cj + dj

            if nj == M: nj = 0
            elif nj == -1: nj = M - 1

            if 0 <= ni < N:
                if not visit[ni][nj] and board[ni][nj] == board[ci][cj]:
                    found_same_number = True
                    visit[ni][nj] = True
                    q.append([ni, nj])
                    delete_index.append([ni, nj])

    if found_same_number:
        for i, j in delete_index:
            board[i][j] = 0
        return found_same_number
    return found_same_number


N, M, T = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]

for _ in range(T):
    X, D, K = map(int, input().split())
    if D == 0: D = 1
    elif D == 1: D = -1

    # Rotate board
    for x in range(X, N+1, X):
        for _ in range(K):
            board[x-1].rotate(D)
    # print("After rotate")
    # for i in board:
    #     print(i)

    # Check same number exist
    visit = [[False for _ in range(M)] for _ in range(N)]
    deleted = False
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] != 0:
                if delete_same_number(i, j):
                    deleted = True

    if not deleted:
        _sum, _cnt = 0, 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    _sum += board[i][j]
                    _cnt += 1
        if _cnt == 0:
            continue
        _avg = _sum / _cnt

        # print("sum and cnt", _sum, _cnt)
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    if board[i][j] > _avg:
                        board[i][j] -= 1
                    elif board[i][j] < _avg:
                        board[i][j] += 1

    # print("After delete same number")
    # for i in board:
    #     print(i)

answer = 0
for row in board:
    answer += sum(row)

print(answer)


"""
4 4 4
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
2 0 2
3 1 1

"""