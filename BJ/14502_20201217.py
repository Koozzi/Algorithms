from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
board = [list(input().split()) for i in range(N)]
move_dir = [[0,1],[0,-1],[1,0],[-1,0]]

# 초기 바이러스 위치와 벽을 세울 수 있는 곳들을 찾아서 저장
virus_location = []
not_virus_location = []

for i in range(N):
    for j in range(M):
        if board[i][j] == '0': not_virus_location.append([i,j])
        if board[i][j] == '2': virus_location.append([i,j])

# 벽을 만들고 BFS로 바이러스를 퍼트리자 
def make_wall_spread(new_wall, new_board):
    
    new_board = deepcopy(new_board)

    # 새로운 벽 세우기
    for wall in new_wall:
        new_board[wall[0]][wall[1]] = '1'

    # 바이러스 퍼트리기
    visit = [[False for i in range(M)] for i in range(N)]
    q = deque()

    for virus in virus_location:
        q.append([virus[0], virus[1]])
        visit[virus[0]][virus[1]] = True

    while(len(q) != 0):
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()
        for i in range(4):
            next_i = current_i + move_dir[i][0]
            next_j = current_j + move_dir[i][1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M : continue

            if new_board[next_i][next_j] == '0' and visit[next_i][next_j] == False:
                q.append([next_i, next_j])
                visit[next_i][next_j] = True
                new_board[next_i][next_j] = '2'
    
    # 안전 영역 구하기
    safe_area = 0
    for row in new_board:
        for item in row:
            if item == '0':
                safe_area += 1
    
    return safe_area

# 조합을 사용해서 벽을 세울 수 있는 곳들을 정해주기
make_wall = list(combinations(not_virus_location, 3))

answer = 0
for wall in make_wall:
    answer = max(answer, make_wall_spread(wall, board))

print(answer)