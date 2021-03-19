from collections import deque

def meet_check(start_i, start_j, end_i, end_j):
    q = deque([[start_i, start_j]])
    _visit = [[False for j in range(M)] for i in range(N)]
    _visit[start_i][start_j] = True
    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            if not _visit[next_i][next_j] and (board[next_i][next_j] == '.' or board[next_i][next_j] == 'L'):
                q.append([next_i,next_j])
                _visit[next_i][next_j] = True

    return True if _visit[end_i][end_j] else False

def melt(start_i, start_j):
    global answer
    melt_land = []
    q = deque([[start_i, start_j]])
    visit[start_i][start_j] = True
    while q:
        current_i, current_j = q.popleft()

        melt_found = False
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue

            if not melt_found and (board[next_i][next_j] == '.' or board[next_i][next_j] == 'L'):
                melt_land.append([current_i, current_j])
                melt_found = True
            
            if not visit[next_i][next_j] and board[next_i][next_j] == 'X':
                q.append([next_i, next_j])
                visit[next_i][next_j] = True

    for I, J in melt_land:
        board[I][J] = '.'

    if meet_check(start_i, start_j, end_i, end_j):
        print(answer)
        exit()

start_i, start_j, end_i, end_j = 0, 0, 0, 0
N, M = map(int, input().split())
board, bird = [], []
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == 'L':
            bird.append([i,j])
    board.append(row)

start_i, start_j = bird[0]
end_i, end_j = bird[1]
answer = 0
while True:
    answer += 1
    visit = [[False for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] == 'X':
                melt(i, j)
    
    if meet_check(start_i, start_j, end_i, end_j):
        break

print(answer)