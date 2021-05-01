'''
14:40

'''

from collections import deque

# [I,J] 현재 택시 위치에서 가장 가까운 손님을 찾아내는 메소드
def find_nearest(A,B):
    customer = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[A][B] = True
    q = deque([[A,B,0]])

    if board[A][B] > 0:
        customer.append([A,B,0])

    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] != -1:
                if board[next_i][next_j] > 0:
                    customer.append([next_i, next_j, current_d+1])
                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d+1])
    
    customer.sort(key=lambda x:(x[2], x[0], x[1]))

    return customer

# [A,B] 에서 [C,D] 까지 거리를 구하는 메소드
def get_distance(A,B,C,D):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[A][B] = True
    q = deque([[A,B,0]])

    while q:
        current_i, current_j, current_d = q.popleft()

        if current_i == C and current_j == D:
            return current_d

        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] != -1:
                visit[next_i][next_j] = True
                q.append([next_i, next_j, current_d+1])

    return -1

if __name__=="__main__":
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    customer_info = [[]]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board[i][j] = -1

    I, J = map(int, input().split())
    I -= 1 ; J -= 1

    for num in range(M):
        A, B, C, D = map(int, input().split())
        board[A-1][B-1] = num + 1
        customer_info.append([A-1,B-1,C-1,D-1])
    
    while True:
        
        customer = find_nearest(I,J)
        if len(customer) != M:
            K = -1
            break

        next_i, next_j, source_to_customer = customer[0]
        K -= source_to_customer
        if K <= 0:
            K = -1
            break
        
        customer_num = board[next_i][next_j]
        board[next_i][next_j] = 0
        I, J = next_i, next_j
        dest_i, dest_j = customer_info[customer_num][2:]

        customer_to_destination = get_distance(I,J,dest_i,dest_j)
        K -= customer_to_destination
        if customer_to_destination == -1 or K < 0:
            K = -1
            break

        I, J = dest_i, dest_j

        K += customer_to_destination * 2
        M -= 1
        if M == 0:
            break
        
    print(K)