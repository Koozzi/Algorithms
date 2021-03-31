# 14:40
# 15:50
#

from collections import deque

def rotate(x, d, k):
    for _ in range(k):
        if d == 0: board[x-1].rotate(1)
        elif d == 1: board[x-1].rotate(-1)

def find_same_number(start_i, start_j):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    init_number = board[start_i][start_j]
    found_same_number = False

    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            
            if next_j == M: next_j = 0
            elif next_j == -1: next_j = M-1

            if not 0 <= next_i < N:
                continue

            if not visit[next_i][next_j] and board[next_i][next_j] == init_number:
                found_same_number = True
                visit[next_i][next_j] = True
                q.append([next_i, next_j])
                board[next_i][next_j] = 0
                board[start_i][start_j] = 0

    return found_same_number

def get_cnt_sum():
    c, s, tmp = 0, 0, []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                c += 1
                s += board[i][j]
                tmp.append([i,j])
    return s, c, tmp

if __name__=="__main__":
    N, M, T = map(int, input().split())
    board = [deque(list(map(int, input().split()))) for _ in range(N)]

    for _ in range(T):
        X, D, K = map(int, input().split())
        for x in range(X, N+1, X):
            rotate(x, D, K)
        
        found_same_number = False
        visit = [[False for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if not visit[i][j] and board[i][j] != 0:
                    if find_same_number(i,j):
                        found_same_number = True 

        if not found_same_number:
            _sum, _cnt, tmp = get_cnt_sum()
            if _cnt == 0: break
            _avg = _sum / _cnt
            
            for I, J in tmp:
                if board[I][J] > _avg: board[I][J] -= 1
                elif board[I][J] < _avg: board[I][J] += 1
        
    answer, c, t = get_cnt_sum()
    
    print(answer)