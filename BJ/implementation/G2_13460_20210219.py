from collections import deque

def move_ball(I, J, move):
    cnt = 0
    while board[I][J] != 'O' and board[I+move[0]][J+move[1]] != '#':
        I += move[0]
        J += move[1]
        cnt += 1
    return I, J, cnt

def BFS():
    global N, M, ri, rj, bi, bj

    move_dir = [[-1,0],[1,0],[0,1],[0,-1]]
    visit = [[[[False for j in range(M)] for i in range(N)] for j in range(M)] for i in range(N)]
    visit[ri][rj][bi][bj] = True
    
    q = deque([[ri,rj,bi,bj,0]])

    while q:
        cri, crj = q[0][0], q[0][1]
        cbi, cbj = q[0][2], q[0][3]
        cd = q[0][4]
        q.popleft()
        
        if cd == 10: break

        for move in move_dir:
            nri, nrj, r_cnt = move_ball(cri, crj, move)
            nbi, nbj, b_cnt = move_ball(cbi, cbj, move)
            if board[nbi][nbj] == 'O': continue
            if board[nri][nrj] == 'O': return cd+1

            if nri == nbi and nrj == nbj:
                if r_cnt > b_cnt:
                    nri -= move[0]
                    nrj -= move[1]
                else:
                    nbi -= move[0]
                    nbj -= move[1]

            if not visit[nri][nrj][nbi][nbj]:
                visit[nri][nrj][nbi][nbj] = True
                q.append([nri,nrj,nbi,nbj,cd+1])
    
    return -1

N, M = map(int, input().split())
ri, rj, bi, bj = 0, 0, 0, 0
board = []
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == 'R': ri, rj = i, j
        elif row[j] == 'B': bi, bj = i, j

    board.append(row)

print(BFS())