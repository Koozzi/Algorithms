from collections import deque


def get_taxi_to_cust(start_i, start_j):

    if cust_board[start_i][start_j] == 1:
        cust_board[start_i][start_j] = 0
        return start_i, start_j, 0

    possible = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if board[next_i][next_j] == 0 and not visit[next_i][next_j]:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j, current_d + 1])
                    if cust_board[next_i][next_j] == 1:
                        possible.append([next_i, next_j, current_d + 1])

    if not possible:
        return 0, 0, -1

    possible.sort(key=lambda x: (x[2], x[0], x[1]))
    i, j, d = possible[0]
    cust_board[i][j] = 0
    return i, j, d


def get_cust_to_dest(start_i, start_j):
    dest_i, dest_j = customer_destination[(start_i, start_j)]
    # print("Start from", start_i, start_j)
    # print("And destination is ", dest_i, dest_j)
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    while q:
        current_i, current_j, current_d = q.popleft()

        if current_i == dest_i and current_j == dest_j:
            return current_i, current_j, current_d

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j] and board[next_i][next_j] == 0:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j, current_d + 1])

    return 0, 0, -1


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cust_board = [[0 for _ in range(N)] for _ in range(N)]
taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1 ; taxi_j -= 1

customer_destination = {}
for _ in range(M):
    I, J, _I, _J = map(int, input().split())
    customer_destination[(I-1, J-1)] = (_I-1, _J-1)
    cust_board[I-1][J-1] = 1

for _ in range(M):

    cust_i, cust_j, cust_d = get_taxi_to_cust(taxi_i, taxi_j)

    # print("Found nearest customer")
    # print(cust_i, cust_j, cust_d)

    K -= cust_d
    if cust_d == -1 or K < 0:
        # print("not enough k or impossible to reach customer")
        K = -1
        break

    dest_i, dest_j, dest_d = get_cust_to_dest(cust_i, cust_j)

    # print("Found customer's destination")
    # print(dest_i, dest_j, dest_d)

    K -= dest_d
    if dest_d == -1 or K < 0:
        # print("not enough k or impossible to reach destination")
        K = -1
        break

    taxi_i, taxi_j = dest_i, dest_j
    K += dest_d * 2

print(K)