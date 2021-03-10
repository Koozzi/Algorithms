from collections import deque

def range_check(N, x, y, d1, d2):
    if 0 <= x < x+d1+d2 < N:
        if 0 <= y-d1 < y < y+d2 < N:
            return True
    return False

def get_section_five(section, N, i, j, d1, d2):
    for d in range(d1+1):
        section[i+d][j-d] = 5
    for d in range(d2+1):
        section[i+d][j+d] = 5
    for d in range(d2+1):
        section[i+d1+d][j-d1+d] = 5
    for d in range(d1+1):
        section[i+d2+d][j+d2-d] = 5
    return section
    
def BFS(init_i, init_j, start_i, start_j, end_i, end_j, section_num):
    global N
    people_sum = board[init_i][init_j]
    visit = [[False for j in range(N)] for i in range(N)] 
    visit[init_i][init_j] = True
    q = deque([[init_i, init_j]])
    section[init_i][init_j] = section_num
    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            if not start_i <= next_i < end_i or not start_j <= next_j < end_j:
                continue
            if visit[next_i][next_j]:
                continue
            if section[next_i][next_j] == 0:
                visit[next_i][next_j] = True
                q.append([next_i, next_j])
                section[next_i][next_j] = section_num
                people_sum += board[next_i][next_j]
    return people_sum

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
answer = 2e9
for i in range(N):
    for j in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if range_check(N, i, j, d1, d2):
                
                    section = [[0 for _ in range(N)] for _ in range(N)]
                    section = get_section_five(section, N, i, j, d1, d2)
                    section_people = [0,0,0,0,0,0]
                    section_people[1] = BFS(0,0, 0,0, i+d1,j+1, 1)
                    section_people[2] = BFS(0,N-1, 0,j+1, i+d2+1,N, 2)
                    section_people[3] = BFS(N-1,0, i+d1,0, N,j+d2-d1, 3)
                    section_people[4] = BFS(N-1,N-1, i+d2+1,j+d2-d1, N,N, 4)

                    for sec_i in range(N):
                        for sec_j in range(N):
                            if section[sec_i][sec_j] == 0 or section[sec_i][sec_j] == 5:
                                section_people[5] += board[sec_i][sec_j]
                    
                    max_poeple = max(section_people[1:])
                    min_people = min(section_people[1:])
                    answer = min(answer, max_poeple - min_people)

print(answer)                    