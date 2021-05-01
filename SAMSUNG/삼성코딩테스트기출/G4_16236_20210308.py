from collections import deque

def can_eat_fish(N, shark_i, shark_j, shark_s):
    visit = [[False for j in range(N)] for i in range(N)]
    visit[shark_i][shark_j] = True
    q = deque([[shark_i, shark_j, 0]])
    bfs_fishes = []
    while q:
        current_i, current_j, current_d = q.popleft()
        
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i, next_j = current_i + move[0], current_j + move[1]
            
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if visit[next_i][next_j]:
                continue
            if board[next_i][next_j] > shark_s:
                continue
            
            visit[next_i][next_j] = True
            q.append([next_i, next_j, current_d+1])

            if 0 < board[next_i][next_j] < shark_s:
                bfs_fishes.append([next_i,next_j,current_d+1])

    return bfs_fishes

N = int(input())
board = []
shark_i, shark_j, shark_s = 0, 0, 2
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(N):
        if row[j] == 9:
            shark_i, shark_j = i, j

eat_cnt = 0
answer = 0
while True:
    fishes = can_eat_fish(N, shark_i, shark_j, shark_s)
    fishes.sort(key=lambda x:(x[2], x[0], x[1]))
    if fishes:
        next_i, next_j, dist = fishes[0][0], fishes[0][1], fishes[0][2]
        board[shark_i][shark_j] = 0
        shark_i, shark_j = next_i, next_j
        board[next_i][next_j] = 9
        answer += dist
        eat_cnt += 1
        if eat_cnt == shark_s:
            shark_s += 1
            eat_cnt = 0
    else: break

print(answer)