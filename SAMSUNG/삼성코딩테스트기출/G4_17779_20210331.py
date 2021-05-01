# 11:20
# 12:20
#

from collections import deque

def fill_the_section(section,section_num,start_i,start_j,I,J,D1,D2):
    
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    section[start_i][start_j] = section_num
    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if visit[next_i][next_j] or section[next_i][next_j] == 5:
                continue
            
            if section_num == 1:
                if not (0 <= next_i < I+D1 and 0 <= next_j <= J):
                    continue
            elif section_num == 2:
                if not (0 <= next_i <= I+D2 and J < next_j < N):
                    continue
            elif section_num == 3:
                if not (I+D1 <= next_i < N and 0 <= next_j < J-D1+D2):
                    continue
            elif section_num == 4:
                if not (I+D2 < next_i < N and J-D1+D2 <= next_j < N):
                    continue

            visit[next_i][next_j] = True
            q.append([next_i, next_j])
            section[next_i][next_j] = section_num

    return section

def get_people(section):
    people_count = [0 for _ in range(6)]
    for i in range(N):
        for j in range(N):
            idx = section[i][j]
            people_count[idx] += board[i][j]
    
    return max(people_count) - min(people_count[1:])

def make_section(I,J,D1,D2):
    global answer, total_sum

    init_i, init_j = I, J
    section = [[0 for _ in range(N)] for _ in range(N)]
    move = [[1,1],[1,-1],[-1,-1],[-1,1]]
    current_direction = 0
    section[I][J] = 5

    while True:
        I += move[current_direction][0]
        J += move[current_direction][1]
        section[I][J] = 5
        
        if I == init_i and J == init_j:
            break

        if (I == init_i+D2 and J == init_j+D2) \
            or (I == init_i+D1+D2 and J == init_j-D1+D2) \
                or (I == init_i+D1 and J == init_j-D1):
                current_direction += 1

    start_idx = [[],[0,0],[0,N-1],[N-1,0],[N-1,N-1]]
    for section_num in range(1,5):
        si, sj = start_idx[section_num]
        section = fill_the_section(section,section_num,si,sj,I,J,D1,D2)

    for i in range(N):
        for j in range(N):
            if section[i][j] == 0:
                section[i][j] = 5

    answer = min(answer, get_people(section))

if __name__=="__main__":
    answer = 2e9
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    total_sum = 0
    for i in range(N):
        for j in range(N):
            total_sum += board[i][j]

    for i in range(N-2):
        for j in range(1,N-1):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if j+d2 < N and i+d1+d2 < N and j-d1 >= 0:
                        make_section(i,j,d1,d2)

    print(answer)