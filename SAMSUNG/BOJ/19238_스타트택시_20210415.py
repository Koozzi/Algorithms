from collections import deque


def taxi_to_customer(start_i, start_j):

    if customer_board[start_i][start_j] > 0:
        return [[start_i, start_j, customer_board[start_i][start_j], 0]]

    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    customer = []
    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j] and board[next_i][next_j] == 0:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j, current_d + 1])
                    if customer_board[next_i][next_j] > 0:
                        customer_num = customer_board[next_i][next_j]
                        customer.append([next_i, next_j, customer_num, current_d + 1])

    return customer


def customer_to_destination(start_i, start_j, end_i, end_j):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    while q:
        current_i, current_j, current_d = q.popleft()

        if current_i == end_i and current_j == end_j:
            return current_d

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if not visit[next_i][next_j] and board[next_i][next_j] == 0:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j, current_d + 1])


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
customer_board = [[0 for _ in range(N)] for _ in range(N)]
customer_info = [[] for _ in range(M+1)]
taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1
taxi_j -= 1

for customer_num in range(1, M+1):
    a, b, c, d = map(int, input().split())
    customer_board[a-1][b-1] = customer_num
    customer_info[customer_num] = [a-1, b-1, c-1, d-1]


for _ in range(M):
    next_customer = taxi_to_customer(taxi_i, taxi_j)

    # 현재 택시의 위치에서 다음 손님으로 갈 수 없는 경우
    if not next_customer:
        K = -1
        break

    next_customer.sort(key=lambda x: (x[3], x[0], x[1]))
    next_i, next_j, customer_num, distance = next_customer[0]
    customer_board[next_i][next_j] = 0

    K -= distance
    if K < 0:
        K = -1
        break

    start_i, start_j, end_i, end_j = customer_info[customer_num]
    dest_distance = customer_to_destination(start_i, start_j, end_i, end_j)

    if not dest_distance:
        K = -1
        break

    K -= dest_distance
    if K < 0:
        K = -1
        break

    taxi_i, taxi_j = end_i, end_j
    K += dest_distance * 2

print(K)