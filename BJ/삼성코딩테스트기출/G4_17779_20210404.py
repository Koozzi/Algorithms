'''
시작 22:00
제출 23:11
종료

'''

from collections import deque
def make_section_five(x,y,d1,d2):
    section = [[0 for _ in range(N+1)] for _ in range(N+1)]

    X, Y = x, y
    section[X][Y] = 5
    while True:
        X += 1 ; Y -= 1
        section[X][Y] = 5
        if X == x+d1 and Y == y-d1: break
    
    X, Y = x, y
    while True:
        X += 1 ; Y += 1
        section[X][Y] = 5
        if X == x+d2 and Y == y+d2: break

    X, Y = x+d1, y-d1
    while True:
        X += 1 ; Y += 1
        section[X][Y] = 5
        if X == x+d1+d2 and Y == y+d2-d1: break
    
    X, Y = x+d2, y+d2
    while True:
        X += 1 ; Y -= 1
        section[X][Y] = 5
        if X == x+d2+d1 and Y == y+d2-d1: break

    for section_num, i, j in [[1,1,1], [2,1,N],[3,N,1],[4,N,N]]:
        section = BFS(section,section_num,i,j,x,y,d1,d2)

    return section

def current_condition(section_num,r,c,x,y,d1,d2):

    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    if section_num == 1:
        if 1 <= r < x+d1 and 1 <= c <= y:
            return True

    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    elif section_num == 2:
        if 1 <= r <= x+d2 and y < c <= N:
            return True

    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    elif section_num == 3:
        if x+d1 <= r <= N and 1 <= c < y-d1+d2:
            return True

    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    elif section_num == 4:
        if x+d2 < r <= N and y-d1+d2 <= c <= N:
            return True

    return False

def BFS(section,section_num,start_i,start_j,x,y,d1,d2):
    visit = [[False for _ in range(N+1)] for _ in range(N+1)]
    section[start_i][start_j] = section_num
    visit[start_i][start_j] = True
    q = deque([[start_i,start_j]])
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            
            if not 1 <= next_i <= N or not 1 <= next_j <= N:
                continue
            
            if not visit[next_i][next_j] and section[next_i][next_j] == 0:
                if current_condition(section_num,next_i,next_j,x,y,d1,d2):
                    section[next_i][next_j] = section_num
                    visit[next_i][next_j] = True
                    q.append([next_i,next_j])

    return section

answer = 2e9
N  = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

board.insert(0, [0 for _ in range(N)])
for row in board:
    row.insert(0, 0)

for x in range(1, N-1):
    for y in range(2, N):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 <= N and 1 <= y-d1 <= N and y+d2 <= N:
                    section = make_section_five(x,y,d1,d2)
                    section_cnt = [0,0,0,0,0,0]
                    for si in range(1,N+1):
                        for sj in range(1,N+1):
                            section_num = section[si][sj]
                            if section_num == 0: section_num = 5
                            section_cnt[section_num] += board[si][sj]

                    min_num = min(section_cnt[1:])
                    max_num = max(section_cnt[1:])
                    answer = min(answer, abs(min_num-max_num) )

print(answer)