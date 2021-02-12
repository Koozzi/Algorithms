from sys import stdin 
from collections import deque

def rotate(N, board, r):
    rotate_num = r[0] # rotate_num의 배수의 원판을 돌릴 것.
    rotate_dir = r[1] # 0은 시계 방향, 1은 반시계 방향
    rotate_cnt = r[2] # 돌리는 횟수

    for idx in range(rotate_num, N+1, rotate_num):
        idx -= 1
        if rotate_dir == 0:
            for _ in range(rotate_cnt):
                board[idx].insert(0, board[idx][-1])
                board[idx].pop()
        elif rotate_dir == 1:
            for _ in range(rotate_cnt):
                board[idx].append(board[idx][0])
                board[idx].pop(0)
    
    return board

def sub_bfs(current_i, current_j, next_i, next_j, board, q, tmp, visit):
    if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
        return q, tmp, visit
                        
    if visit[next_i][next_j]:
        return q, tmp, visit

    if board[next_i][next_j] == board[current_i][current_j]:
        q.append([next_i, next_j])
        tmp.append([next_i, next_j])
        visit[next_i][next_j] = True
    
    return True, q, tmp, visit

def erase_near_num(N, M, board):
    erased = False
    visit = [[False for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == -1: continue
            if visit[i][j]: continue
            
            tmp = [[i,j]]
            q = deque([[i,j]])
            visit[i][j] = True
            
            while q:
                current_i = q[0][0]
                current_j = q[0][1]
                q.popleft()
                
                if current_j == M-1:
                    for move in [ [-1,0],[1,0],[0,-1],[0,-M+1] ]:
                        next_i = current_i + move[0]
                        next_j = current_j + move[1]

                        q, tmp, visit = sub_bfs(current_i, current_j, next_i, next_j, board, q, tmp, visit)

                elif current_j == 0:
                    for move in [[1,0],[-1,0],[0,1],[0,M-1]]:
                        next_i = current_i + move[0]
                        next_j = current_j + move[1]

                        q, tmp, visit = sub_bfs(current_i, current_j, next_i, next_j, board, q, tmp, visit)

                else:
                    for move in [[0,1],[0,-1],[1,0],[-1,0]]:
                        next_i = current_i + move[0]
                        next_j = current_j + move[1]

                        q, tmp, visit = sub_bfs(current_i, current_j, next_i, next_j, board, q, tmp, visit)
                
            if len(tmp) > 1:
                erased = True
                for I,J in tmp:
                    board[I][J] = -1
 
    return erased, board

def sum_cnt(board):
    _sum, _cnt = 0, 0
    for row in board:
        for item in row:
            if item != -1:
                _sum += item
                _cnt += 1
    
    return _sum, _cnt

def solution(N,M,T,board,rotate_info):

    for r in rotate_info:
        board = rotate(N,board,r)
        erased, board = erase_near_num(N,M,board)

        if not erased: # 인접하면서 같은 숫자는 존재하지 않음
            
            _sum, _cnt = sum_cnt(board)
            
            if _cnt == 0:
                return 0

            avg = _sum / _cnt

            for i in range(N):
                for j in range(M):
                    if board[i][j] == -1: continue
                    if board[i][j] < avg: board[i][j] += 1
                    elif board[i][j] > avg: board[i][j] -= 1

    _sum, _cnt = sum_cnt(board)

    return _sum

if __name__=="__main__":
    N, M, T = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for n in range(N)]
    rotate_info = [list(map(int, stdin.readline().split())) for t in range(T)]

    print(solution(N,M,T,board,rotate_info))