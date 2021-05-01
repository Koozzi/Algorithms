'''
시작 02:05
제출 02:33
종료
'''
from collections import deque

def rotate_board(X,D,K):
    if D == 0: D = 1
    elif D == 1: D = -1
    
    for x in range(X, N+1, X):
        for _ in range(K):
            board[x-1].rotate(D)

def erase_same_number(start_i,start_j):
    found_same_number = False
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    init_number = board[start_i][start_j]

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if next_j == M: next_j = 0
            elif next_j == -1: next_j = M-1

            if 0 <= next_i < N:
                if not visit[next_i][next_j] and board[next_i][next_j] == init_number:
                    found_same_number = True
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])
                    board[next_i][next_j] = 0

    if found_same_number:
        board[start_i][start_j] = 0
        return True
    
    return False

N, M, T = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]
visit = []

for _ in range(T):
    X, D, K = map(int, input().split())    

    rotate_board(X,D,K)

    # print("Rotated")
    # for i in board:
    #     print(i)

    # 인접하면서 수가 같은 것을 모두 찾아서 지웠음.
    found_same_number = False
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] != 0:
                if erase_same_number(i,j):
                    found_same_number = True
    
    # 인접하면서 같은 수가 없는 경우
    if not found_same_number:
        num_sum, num_cnt = 0, 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    num_sum += board[i][j]
                    num_cnt += 1
    
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    if board[i][j] > num_sum / num_cnt:
                        board[i][j] -= 1
                    elif board[i][j] < num_sum / num_cnt:
                        board[i][j] += 1
    
    # print("Erased same numbers")
    # for i in board:
    #     print(i)

answer = 0
for row in board:
    answer += sum(row)
print(answer)