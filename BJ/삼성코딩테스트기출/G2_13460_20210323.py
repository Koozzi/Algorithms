# 11:35

from collections import deque

def move_ball(I,J,move):
    cnt = 0
    while board[I+move[0]][J+move[1]] != '#' and board[I][J] != 'O':
        I += move[0]
        J += move[1]
        cnt += 1
    return I,J,cnt

def BFS():
    visit = [[[[False for j in range(M)]for i in range(N)]for j in range(M)]for i in range(N)]
    visit[red_i][red_j][blue_i][blue_j] = True
    q = deque([[red_i, red_j, blue_i, blue_j, 0]])

    while q:
        c_red_i, c_red_j, c_blue_i, c_blue_j, depth = q.popleft()

        if depth == 10:
            break

        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            n_red_i, n_red_j, red_cnt = move_ball(c_red_i, c_red_j, move)
            n_blue_i, n_blue_j, blue_cnt = move_ball(c_blue_i, c_blue_j, move)

            if board[n_blue_i][n_blue_j] == 'O': continue
            if board[n_red_i][n_red_j] == 'O': return depth+1

            # 빨간 공과 파란 공이 같은 위치에 있을 때,
            # 더 많이 움직인, 더 멀리서 온, 더 늦게 도착한 공이 한 칸 뒤로 간다
            if n_red_i == n_blue_i and n_red_j == n_blue_j:
                if red_cnt < blue_cnt: 
                    n_blue_i -= move[0]
                    n_blue_j -= move[1]
                else:
                    n_red_i -= move[0]
                    n_red_j -= move[1]

            if not visit[n_red_i][n_red_j][n_blue_i][n_blue_j]:
                visit[n_red_i][n_red_j][n_blue_i][n_blue_j] = True
                q.append([n_red_i, n_red_j, n_blue_i, n_blue_j, depth+1])
    return -1

if __name__=="__main__":
    N, M = map(int, input().split())
    red_i, red_j, blue_i, blue_j = 0, 0, 0, 0
    board = []
    for i in range(N):
        row = input()
        board.append(row)
        for j, ball in enumerate(row):
            if ball == 'R':
                red_i, red_j = i, j
            elif ball == 'B':
                blue_i, blue_j = i, j
    
    print(BFS())