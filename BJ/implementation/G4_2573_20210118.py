from sys import stdin
from collections import deque

def melt(N, M, board):
    move_dir = [[1,0],[-1,0],[0,1],[0,-1]]
    new_board = [[0 for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                for move in move_dir:
                    next_i = i + move[0]
                    next_j = j + move[1]

                    if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                        continue

                    if board[next_i][next_j] == 0:
                        new_board[i][j] += 1

    for i in range(N):
        for j in range(M):
            if board[i][j] > new_board[i][j]:
                board[i][j] -= new_board[i][j]
            else:
                board[i][j] = 0

    return board

def check(N, M, board, visit, start_i, start_j):
    move_dir = [[1,0],[-1,0],[0,1],[0,-1]]
    q = deque([[start_i, start_j]])
    visit[start_i][start_j] = True

    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()

        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                continue

            if board[next_i][next_j] > 0 and not visit[next_i][next_j]:
                q.append([next_i, next_j])
                visit[next_i][next_j] = True

    return visit

def solution(N, M, board):
    year = 0

    while True:
        year += 1
        board = melt(N, M, board)
        
        land_cnt = 0
        visit = [[False for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] > 0 and not visit[i][j]:
                    land_cnt += 1
                    visit = check(N, M, board, visit, i, j)
                    
        if land_cnt == 0:
            return 0

        if land_cnt > 1:
            break

    return year 

if __name__=="__main__":
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    print(solution(N, M, board)) 