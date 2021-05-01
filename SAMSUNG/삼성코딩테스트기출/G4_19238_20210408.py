'''
시작 17:00
제출
종료
'''
from collections import deque

def get_taxi_to_customer(start_i, start_j):

    if board[start_i][start_j] > 0:
        return [[start_i, start_j, 0]]

    next_customer = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])

    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] > -1:
                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d+1])
                if board[next_i][next_j] > 0:
                    next_customer.append([next_i, next_j, current_d+1])

    next_customer.sort(key=lambda x:(x[2],x[0],x[1]))

    return next_customer

def get_customer_to_destination(start_i, start_j, dest_i, dest_j):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    while q:
        current_i, current_j, current_d = q.popleft()

        if current_i == dest_i and current_j == dest_j:
            return current_d

        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] != -1:
                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d + 1])
    
    return -1

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
customer_destination = [[] for _ in range(M+1)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = -1

taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1 ; taxi_j -= 1

for num in range(1,M+1):
    A,B,C,D = map(int, input().split())
    board[A-1][B-1] = num
    customer_destination[num] = [C-1,D-1]

for _ in range(M):

    customers = get_taxi_to_customer(taxi_i, taxi_j)
    
    if not customers:
        K = -1
        break

    K -= customers[0][2]
    if K < 0:
        K = -1
        break

    cust_i, cust_j, taxi_to_customer = customers[0]
    customer_num = board[cust_i][cust_j]
    dest_i, dest_j = customer_destination[customer_num]
    board[cust_i][cust_j] = 0
    customer_to_destination = get_customer_to_destination(cust_i, cust_j, dest_i, dest_j)

    K -= customer_to_destination
    if K < 0 or customer_to_destination == -1:
        K = -1
        break
    
    taxi_i, taxi_j = dest_i, dest_j
    K += customer_to_destination * 2

print(K)