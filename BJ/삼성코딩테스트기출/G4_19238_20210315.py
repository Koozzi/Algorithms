'''
1. 현재 택시 위치에서 가장 가까운 손님을 찾아서 리스트에 저장한다. (BFS_01)
    1-1. 손님의 수가 2명 이상일 때는 우선순위에 따라 정렬한다.
    1-2. 가장 가까운 손님 위치까지의 거리와 현재 연료 Check
    1-3. 택시 위치 갱신
    1-4. board에서 손님 번호 삭제 (n->0)
2. 손님 출발지에서 손님 목적지까지 이동한다. customer_info[n] => [[현재 위치],[현재 위치]]
    2-1. 손님의 목적지까지 거리와 현재 연료 Check
    2-2. 택시 위치 갱신
3. 택시 연료 충전
'''

from collections import deque

def get_distance(start_i, start_j, end_i, end_j):
    global N
    visit = [[False for j in range(N+1)] for i in range(N+1)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j,0]])
    while q:
        current_i, current_j, current_d = q.popleft()
        for move in [[0,1],[0,-1],[-1,0],[1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            if not 0 < next_i <= N or not 0 < next_j <= N:
                continue
            if visit[next_i][next_j] or board[next_i][next_j] == -1:
                continue
            visit[next_i][next_j] = True
            q.append([next_i, next_j, current_d+1])
            if next_i == end_i and next_j == end_j:
                return current_d+1
    return -1

def get_nearest_customer(start_i, start_j):
    global N
    visit = [[False for j in range(N+1)] for i in range(N+1)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j,0]])
    customer = [] # [..., [X, Y], ... ] X : 고객 번호, Y : 현재 위치에서 고객 위치까지의 거리
    if board[start_i][start_j] != 0:
        customer.append([start_i, start_j,board[start_i][start_j], 0])
    while q:
        current_i, current_j, current_d = q.popleft()
        for move in [[0,1],[0,-1],[-1,0],[1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            if not 0 < next_i <= N or not 0 < next_j <= N:
                continue
            if visit[next_i][next_j] or board[next_i][next_j] == -1:
                continue
            visit[next_i][next_j] = True
            q.append([next_i, next_j, current_d+1])
            if board[next_i][next_j] != 0:
                customer_num = board[next_i][next_j]
                customer_dis = current_d + 1
                customer.append([next_i, next_j, customer_num, customer_dis])

    customer = sorted(customer, key=lambda x:(x[3], x[0], x[1]))
    return customer

N, M, K = map(int, input().split())
board = [[],]
for _ in range(N):
    row = [0]
    row_input = list(map(int, input().split()))
    for j in range(N):
        if row_input[j] == 1: row_input[j] = -1
    row += row_input
    board.append(row)

taxi_i, taxi_j = map(int, input().split())

customer_info = [[]]
for num in range(1,M+1):
    customer = list(map(int, input().split()))
    board[customer[0]][customer[1]] = num
    customer_info.append(customer)

while True:
    
    customer = get_nearest_customer(taxi_i, taxi_j)
    if len(customer) != M:
        K = -1
        break

    next_customer = customer[0]
    K -= next_customer[3]
    if K < 0:
        K = -1
        break

    taxi_i = next_customer[0]
    taxi_j = next_customer[1]
    board[taxi_i][taxi_j] = 0
    next_customer_num = next_customer[2]

    end_i = customer_info[next_customer_num][2]
    end_j = customer_info[next_customer_num][3]

    distance = get_distance(taxi_i,taxi_j, end_i, end_j)
    K -= distance
    if distance == -1 or K < 0:
        K = -1
        break

    taxi_i = end_i
    taxi_j = end_j

    K += distance * 2
    M -= 1
    if M == 0:
        break


print(K)