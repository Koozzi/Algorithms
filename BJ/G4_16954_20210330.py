# 13:10
# 13:40
#

from collections import deque

def go_down(board):
    board = list(map(list, zip(*board)))
    for idx, row in enumerate(board):
        board[idx] = ['.'] + row[:7]
    board = list(map(list, zip(*board)))
    return board

def BFS(board):
    new_board = [['.' for _ in range(8)] for _ in range(8)]
    visit = [[False for _ in range(8)] for _ in range(8)]
    visit[7][0] = True
    q = deque([[7,0,0]])
    new_board[7][0] = 'L'
    check_depth = 0

    while q:
        
        current_i, current_j, current_d = q.popleft()
        if current_i == 0 and current_j == 7:
            return 1

        if current_d != check_depth:
            check_depth = current_d
            board = go_down(board)
            for i in range(8):
                for j in range(8):
                    if board[i][j] == '#' and new_board[i][j] == 'L':
                        new_board[i][j] = '.'

        if new_board[current_i][current_j] == '.':
            continue

        q.append([current_i,current_j,current_d+1])
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < 8 or not 0 <= next_j < 8:
                continue

            if not visit[next_i][next_j] \
                and new_board[next_i][next_j] == '.' \
                    and board[next_i][next_j] != '#':
                visit[next_i][next_j] == True
                new_board[next_i][next_j] = 'L'
                q.append([next_i,next_j,current_d+1])

    return 0

if __name__=="__main__":
    board = [list(input()) for _ in range(8)]
    print(BFS(board))