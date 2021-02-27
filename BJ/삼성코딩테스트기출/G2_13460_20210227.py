from collections import deque

def move_ball(I,J,move):
    cnt = 0
    while board[I][J] != 'O' and board[I+move[0]][J+move[1]] != '#':
        I += move[0]
        J += move[1]
        cnt += 1
    return I,J,cnt

def BFS(ri, rj, bi, bj):
    global N, M
    visit = [[[[False for j in range(M)] for i in range(N)] for j in range(M)] for i in range(N)]
    visit[ri][rj][bi][bj] = True
    q = deque([[ri,rj,bi,bj,0]])

    while q:
        cri, crj, cbi, cbj, depth = q.popleft()
        if depth == 10: break
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            nri, nrj, r_cnt = move_ball(cri, crj, move)
            nbi, nbj, b_cnt = move_ball(cbi, cbj, move)

            if board[nbi][nbj] == 'O': continue
            if board[nri][nrj] == 'O': return depth+1
                
            if nri == nbi and nrj == nbj:
                if r_cnt < b_cnt: nbi, nbj = nbi - move[0], nbj - move[1]
                else: nri, nrj = nri - move[0], nrj - move[1]
            
            if not visit[nri][nrj][nbi][nbj]:
                visit[nri][nrj][nbi][nbj] = True
                q.append([nri,nrj,nbi,nbj,depth+1])
                
    return -1

N, M = map(int, input().split())
ri, rj, bi, bj = 0, 0, 0, 0
board = []
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            ri, rj = i, j
        if board[i][j] == 'B':
            bi, bj = i, j

print(BFS(ri, rj, bi, bj))