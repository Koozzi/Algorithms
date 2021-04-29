from collections import deque


def find_same_number(start_i, start_j, visit):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    will_be_erased = [[start_i, start_j]]
    init_number = board[start_i][start_j]
    found = False
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if next_j == -1: next_j = M-1
            elif next_j == M: next_j = 0

            if 0 <= next_i < N:
                if not visit[next_i][next_j]:
                    if board[next_i][next_j] == init_number:
                        visit[next_i][next_j] = True
                        q.append([next_i, next_j])
                        will_be_erased.append([next_i, next_j])
                        found = True

    if found:
        for i, j in will_be_erased:
            board[i][j] = 0

    return visit, found


def found_same_number_and_erased():

    visit = [[False for _ in range(M)] for _ in range(N)]
    found_same_number = False
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] != 0:
                visit, found = find_same_number(i, j, visit)
                if found:
                    found_same_number = True

    return found_same_number


N, M, K = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]

for _ in range(K):
    X, D, C = map(int, input().split())

    if D == 0: D = 1
    elif D == 1: D = -1

    for x in range(X, N+1, X):
        for _ in range(C):
            board[x-1].rotate(D)

    if found_same_number_and_erased():
        continue

    elif not found_same_number_and_erased():
        _sum, _cnt = 0, 0

        for i in range(N):
            for j in range(M):
                if board[i][j] > 0:
                    _sum += board[i][j]
                    _cnt += 1

        if _cnt == 0:
            continue

        _avg = _sum / _cnt

        for i in range(N):
            for j in range(M):
                if board[i][j] > 0:
                    if board[i][j] > _avg:
                        board[i][j] -= 1
                    elif board[i][j] < _avg:
                        board[i][j] += 1

answer = 0
for i in range(N):
    for j in range(M):
        answer += board[i][j]
print(answer)
