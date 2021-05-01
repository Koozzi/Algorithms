'''
시작 15:15
제출 16:05
종료
'''

from collections import deque

def go_to_customer(taxi_i, taxi_j):

    if cust_board[taxi_i][taxi_j] > 0:
        return taxi_i, taxi_j, 0

    customers = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[taxi_i][taxi_j] = True
    q = deque([[taxi_i, taxi_j, 0]])
    
    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and init_board[next_i][next_j] == 0:
                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d + 1])

                if cust_board[next_i][next_j] > 0:
                    customers.append([next_i, next_j, current_d + 1])

    if not customers:
        return 0,0,-1

    customers.sort(key=lambda x:(x[2], x[0], x[1]))
    return customers[0]

def go_to_destination(cust_i, cust_j, dest_i, dest_j):

    # print("현재 택시는 ", current_customer_num, "을 태우고 ", current_destination_num,"로 향할 예정")

    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[cust_i][cust_j] = True
    q = deque([[cust_i, cust_j, 0]])

    while q:
        current_i, current_j, current_d = q.popleft()

        if current_i == dest_i and current_j == dest_j:
            return current_d

        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and init_board[next_i][next_j] == 0:
                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d + 1])

    return -1

N, M, K = map(int, input().split())
init_board = [list(map(int, input().split())) for _ in range(N)]
cust_board = [[0 for _ in range(N)] for _ in range(N)]

customer_info = [[]]

taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1 ; taxi_j -= 1

for num in range(1,M+1):
    A,B,C,D = map(int, input().split())
    cust_board[A-1][B-1] = num
    customer_info.append([num, A-1, B-1, C-1, D-1])

for _ in range(M):

    # print("#######################################")
    # print("택시 출발합니다.")
    # print("현재 위치 : ", taxi_i, taxi_j)
    # print("남은 연료 : ", K)
    # print("#######################################")

    cust_i, cust_j, taxi_to_customer = go_to_customer(taxi_i, taxi_j)
    
    K -= taxi_to_customer
    if taxi_to_customer == -1 or K < 0:
        K = -1
        break

    # print("#######################################")
    # print("정상적으로 손님을 태웠습니다.")
    # print("현재 위치 : ", cust_i,cust_j)
    # print("남은 연료 : ", K)
    # print("#######################################")

    current_customer_num = cust_board[cust_i][cust_j]
    dest_i, dest_j = customer_info[current_customer_num][3:]
    cust_board[cust_i][cust_j] = 0
    customer_to_dest = go_to_destination(cust_i, cust_j, dest_i, dest_j)

    K -= customer_to_dest
    if customer_to_dest == -1 or K < 0:
        K = -1
        break

    taxi_i, taxi_j = dest_i, dest_j
    K += (customer_to_dest * 2)

    # print("#######################################")
    # print("정상적으로 손님을 목적지까지 데려다 줬습니다.")
    # print("이동 거리 : ", customer_to_dest)
    # print("현재 위치 : ", dest_i,dest_j)
    # print("남은 연료 : ", K)
    # print("#######################################")

print(K)


'''
6 4 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
1 6 5 4
ans: 20

'''