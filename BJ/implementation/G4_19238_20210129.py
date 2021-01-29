from sys import stdin
from collections import deque

def get_distance(N, board, start_i, start_j, dest_i, dest_j):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit = [[False for i in range(N)] for i in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j, 0]])
    
    if start_i == dest_i and start_j == dest_j:
        return 0

    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        current_d = q[0][2]
        q.popleft()

        if current_i == dest_i and current_j == dest_j:
            return current_d        

        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= N:
                continue

            if board[next_i][next_j] == 1:
                continue

            if visit[next_i][next_j]:
                continue

            visit[next_i][next_j] = True
            q.append([next_i, next_j, current_d+1])

    return -1

def get_distance_all(N, board, start_i, start_j, customer_info):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit = [[False for i in range(N)] for i in range(N)]
    depth = [[0 for i in range(N)] for i in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])

    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()

        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= N:
                continue

            if board[next_i][next_j] == 1:
                continue

            if visit[next_i][next_j]:
                continue

            visit[next_i][next_j] = True
            q.append([next_i, next_j])
            depth[next_i][next_j] = depth[current_i][current_j] + 1

    for customer in customer_info:
        customer[4] = depth[customer[0]][customer[1]]
        if customer[4] == 0:
            if start_i != customer[0] or start_j != customer[1]:
                customer[4] = -1
    
    customer_info.sort(key=lambda x:(-x[4], -x[0], -x[1]))

    return customer_info

def solution(N, M, K, board, current_i, current_j, customer_info):

    for i in range(M):
        customer_info = get_distance_all(N, board, current_i, current_j, customer_info)

        customer_i, customer_j = customer_info[-1][0], customer_info[-1][1]
        dest_i, dest_j = customer_info[-1][2], customer_info[-1][3]
        distance_taxi_to_customer = customer_info[-1][4]

        if distance_taxi_to_customer == -1:
            return -1
        
        # 가장 가까운 손님의 위치로 이동
        current_i, current_j = customer_i, customer_j
        K -= distance_taxi_to_customer
        if K <= 0: return -1

        # 손님의 목표지점까지 이동
        distance_customer_to_destination = get_distance(N, board, current_i, current_j, dest_i, dest_j)
        current_i, current_j = dest_i, dest_j
        if distance_customer_to_destination == -1:
            return -1

        K -= distance_customer_to_destination
        if K < 0: return -1
        if K == 0 and i < N-1: return -1

        K += (distance_customer_to_destination) * 2
        customer_info.pop(-1)
        
    return K

if __name__=="__main__":
    N, M, K = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for i in range(N)]
    start_i, start_j = map(int, stdin.readline().split())
    customer_info = [list(map(int, stdin.readline().split())) for i in range(M)]

    for customer in customer_info:
        for i in range(4):
            customer[i] -= 1
        customer.append(0)

    print(solution(N, M, K, board, start_i-1, start_j-1, customer_info))