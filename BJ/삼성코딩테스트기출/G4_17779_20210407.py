'''
시작 17:55
제출 18:44
종료
'''
from collections import deque

def make_section_five(x,y,d1,d2):
    section = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for d in range(d1+1):
        section[x+d][y-d] = 5
        section[x+d2+d][y+d2-d] = 5

    for d in range(d2+1):
        section[x+d][y+d] = 5
        section[x+d1+d][y-d1+d] = 5
    
    return section

def section_num_condition(r,c,section_num,x,y,d1,d2):
    # 1 ≤ r < x+d1, 1 ≤ c ≤ y
    if section_num == 1:
        if 1 <= r < x+d1 and 1 <= c <= y:
            return True 

    # 1 ≤ r ≤ x+d2, y < c ≤ N  
    elif section_num == 2:
        if 1 <= r <= x+d2 and y < c <= N:
            return True
    
    # x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    elif section_num == 3:
        if x+d1 <= r <= N and 1 <= c < y-d1+d2:
            return True

    # x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    elif section_num == 4:
        if x+d2 < r <= N and y-d1+d2 <= c <= N:
            return True
    
    return False

def make_section_other(section,section_num,x,y,d1,d2):
    start_i, start_j = start_location[section_num]
    visit = [[False for _ in range(N+1)] for _ in range(N+1)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    section[start_i][start_j] = section_num
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 1 <= next_i <= N and 1 <= next_j <= N:
                if not visit[next_i][next_j] and section[next_i][next_j] == 0:
                    if section_num_condition(next_i,next_j,section_num,x,y,d1,d2):
                        visit[next_i][next_j] = True
                        q.append([next_i,next_j])
                        section[next_i][next_j] = section_num

    return section

answer = 2e9
N = int(input())
start_location = [[],[1,1],[1,N],[N,1],[N,N]]
board = [list(map(int,input().split())) for _ in range(N)]
board.insert(0, [0 for _ in range(N)])
for row in board:
    row.insert(0,0)

for x in range(1,N-1):
    for y in range(2,N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if x+d1+d2<=N and 1<=y-d1 and y+d2<=N:
                    section = make_section_five(x,y,d1,d2)
                    for section_num in range(1,5):
                        section = make_section_other(section,section_num,x,y,d1,d2)

                    section_cnt = [0,0,0,0,0,0]
                    for i in range(1,N+1):
                        for j in range(1,N+1):
                            section_num = section[i][j]
                            if section_num == 0: section_num = 5
                            section_cnt[section_num] += board[i][j]

                    min_num = min(section_cnt[1:])
                    max_num = max(section_cnt[1:])
                    answer = min(answer, abs(min_num-max_num) )

print(answer)               