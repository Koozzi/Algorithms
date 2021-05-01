from collections import deque

def divide_section(N, L, R, start_i, start_j, section):
    visit[start_i][start_j] = section
    q = deque([[start_i, start_j]])
    cnt_section = 1
    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if visit[next_i][next_j] != -1:
                continue
                
            if L <= abs(board[current_i][current_j] - board[next_i][next_j]) <= R:
                visit[next_i][next_j] = section
                q.append([next_i, next_j])
                cnt_section += 1

    return True if cnt_section > 1 else False

def people_move(N, section):
    section_info = [[0,0] for i in range(section+1)]
    for i in range(N):
        for j in range(N):
            section_info[visit[i][j]][0] += board[i][j]
            section_info[visit[i][j]][1] += 1
    
    for i in range(N):
        for j in range(N):
            board[i][j] = section_info[visit[i][j]][0] // section_info[visit[i][j]][1]
            

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
section_info = []
visit = []
answer = 0
while True:
    visit = [[-1 for j in range(N)] for i in range(N)]
    section_info = []
    section = 0
    moved = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] != -1: continue
            section += 1
            if divide_section(N, L, R, i, j, section):
                moved = True
    
    if not moved:
        break

    people_move(N, section)
    
    answer += 1

print(answer)
