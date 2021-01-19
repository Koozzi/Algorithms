from sys import stdin
from collections import deque

def melt(N, M, board):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit = [[False for j in range(M)] for i in range(N)]
    new_board = [[0 for j in range(M)] for i in range(N)]
    q = deque([[0,0]])
    visit[0][0] = True
    while q:
        current_i = q[0][0]
        currnet_j = q[0][1]
        q.popleft()

        for move in move_dir:
            next_i = current_i + move[0]
            next_j = currnet_j + move[1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                continue

            if board[next_i][next_j] == 1:
                new_board[next_i][next_j] += 1

            if board[next_i][next_j] == 0 and not visit[next_i][next_j]:
                q.append([next_i, next_j])
                visit[next_i][next_j] = True

    for i in range(N):
        for j in range(M):
            if new_board[i][j] > 1:
                board[i][j] = 0

    return board

def check(board):

    for row in board:
        for cheeze in row:
            if cheeze > 0:
                return True

    return False

def solution(N, M, board):
    time = 0

    if not check(board):
        return time

    while True:
        time += 1
        board = melt(N, M, board)

        if check(board): continue
        else: break

    return time

if __name__=="__main__":
    N, M = map(int, stdin.readline().split())
    
    board = []
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    print(solution(N, M, board))