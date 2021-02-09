from collections import deque

def ball_move(board, I, J, move):
    cnt = 0
    while board[I][J] != 'O' and board[I+move[0]][J+move[1]] != '#':
        I += move[0]
        J += move[1]
        cnt += 1
    return cnt, I, J

def BFS(N, M, board, start_red_i, start_red_j, start_blue_i, start_blue_j):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit = [[[[False] * M for i in range(N)] for i in range(M)] for i in range(N)]
    visit[start_red_i][start_red_j][start_blue_i][start_blue_j] = True
    q = deque([[start_red_i, start_red_j, start_blue_i, start_blue_j, 0]])

    while q:
        curr_red_i, curr_red_j = q[0][0], q[0][1]
        curr_blue_i, curr_blue_j = q[0][2], q[0][3]
        curr_d = q[0][4]
        q.popleft()
        
        if curr_d == 10: break

        for move in move_dir:
            red_move_cnt, next_red_i, next_red_j = ball_move(board, curr_red_i, curr_red_j, move)
            blue_move_cnt, next_blue_i, next_blue_j = ball_move(board, curr_blue_i, curr_blue_j, move)

            if board[next_blue_i][next_blue_j] == 'O': continue
            if board[next_red_i][next_red_j] == 'O':
                return 1

            if next_red_i == next_blue_i and next_red_j == next_blue_j:
                if red_move_cnt > blue_move_cnt:
                    next_red_i -= move[0]
                    next_red_j -= move[1]
                else:
                    next_blue_i -= move[0]
                    next_blue_j -= move[1]
            
            if not visit[next_red_i][next_red_j][next_blue_i][next_blue_j]:
                visit[next_red_i][next_red_j][next_blue_i][next_blue_j] = True
                q.append([next_red_i, next_red_j, next_blue_i, next_blue_j, curr_d+1])
    return 0


def solution(N, M, board):
    red_i, red_j, blue_i, blue_j= 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red_i, red_j = i, j
            elif board[i][j] == 'B':
                blue_i, blue_j = i, j
    
    return BFS(N, M, board, red_i, red_j, blue_i, blue_j)

if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(input()) for i in range(N)]

    print(solution(N, M, board))