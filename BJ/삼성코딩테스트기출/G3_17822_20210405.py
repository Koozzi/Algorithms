'''
시작 14:42
제출
종료
'''
from collections import deque

def get_cnt_sum():
    c, s, tmp = 0, 0, []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                c += 1
                s += board[i][j]
                tmp.append([i,j])
    return s, c, tmp

def find_same_number(start_i, start_j):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    init_num = board[start_i][start_j]
    found_same_number = False

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            
            if next_j == -1: next_j = M-1
            elif next_j == M: next_j = 0
            
            if not 0 <= next_i < N:
                continue
            
            if not visit[next_i][next_j] and board[next_i][next_j] == init_num:
                found_same_number = True
                visit[next_i][next_j] = True
                q.append([next_i, next_j])
                board[next_i][next_j] = 0
                board[start_i][start_j] = 0
    
    return found_same_number

N, M, T = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]

for _ in range(T):
    X, D, K = map(int, input().split())

    # 돌린다
    if D == 0: D = 1
    elif D == 1: D = -1
    for x in range(X, N+1, X):
        for _ in range(K):
            board[x-1].rotate(D)

    # 인접한 수가 있는지 찾는다.
    found_same_num = False
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] != 0:
                if find_same_number(i,j):
                    found_same_num = True

    if not found_same_num:
        num_sum, num_cnt, num_tmp = get_cnt_sum()
        if num_cnt == 0: break
        num_avg = num_sum / num_cnt

        for I, J in num_tmp:
            if board[I][J] > num_avg: board[I][J] -= 1
            elif board[I][J] < num_avg: board[I][J] += 1

print(get_cnt_sum()[0])


'''
4 4 2
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
'''