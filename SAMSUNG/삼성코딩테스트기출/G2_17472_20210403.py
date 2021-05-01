'''
시작 21:25
제출 22:13
종료 22:37

다리는 바다에만 놓을 수 있음
다리의 길이는 무조건 2이상
방향은 가로 혹은 세로임

구역을 구한다.
우선 놓을 수 있는 다리를 모두 구한다. > [A,B,2] > 다리의 길이 최소값을 유지한다.
그리고 DFS를 돌려서 다리를 조합한다.
총 다리 길이의 최소값을 구한다.

구현 능력이 딸려서 늦음
'''

from collections import deque

# 첫 구간을 설정하는 함수
def make_section(start_i, start_j, section_num):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    board[start_i][start_j] = section_num
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue

            if board[next_i][next_j] == 1 and not visit[next_i][next_j]:
                visit[next_i][next_j] = True
                q.append([next_i, next_j])
                board[next_i][next_j] = section_num

# 시작점에서 방향을 바꾸지 않고 새로운 영역이 발견될 때까지 앞으로 나아간다.
def make_bridge(I,J,di,dj,current_section):

    bridge_length = 1
    while True:

        I += di
        J += dj
        if not 0 <= I < N or not 0 <= J < M:
            return
             
        if board[I][J] == current_section:
            return

        if board[I][J] > 0 and board[I][J] != current_section:
            break

        bridge_length += 1
    
    if bridge_length >= 2:
        start = current_section
        end = board[I][J]
        
        section_bridge[start][end] = min(section_bridge[start][end], bridge_length)
        section_bridge[end][start] = min(section_bridge[end][start], bridge_length)

# 놓을 수 있는 다리 전체를 구한다.
def find_total_bridge(start_i, start_j, section_num):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            
            if board[next_i][next_j] == 0:
                make_bridge(next_i, next_j, di, dj, section_num)

            if board[next_i][next_j] == section_num and not visit[next_i][next_j]:
                visit[next_i][next_j] = True
                q.append([next_i, next_j])

# 현재 tmp에 담겨있는 다리로 전체를 연결할 수 있는가?
def all_connected():
    
    section_relation = [[] for _ in range(section_num)]
    visit = [False for _ in range(section_num)]

    for A, B, C in tmp:
        section_relation[A].append(B)
        section_relation[B].append(A)

    visit_cnt = 1
    visit[1] = True
    q = deque([1])
    while q:
        c = q.popleft()
        for n in section_relation[c]:
            if not visit[n]:
                visit_cnt += 1
                visit[n] = True
                q.append(n)

    if visit_cnt == section_num-1: return True
    else: return False

# tmp에 다리 정보를 추가하고, 최종적으로 전체가 연결되어 있는지 확인하는 함수
def put_bridge(start_idx,len_sum):
    global answer

    if len_sum != 0 and all_connected():
        answer = min(answer, len_sum)

    for i in range(start_idx, len(total_bridge)):
        tmp.append(total_bridge[i])
        put_bridge(i+1, len_sum+total_bridge[i][2])
        tmp.pop()

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

# 처음에 영역을 설정한다.
section_num = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visit[i][j]:
            make_section(i,j,section_num)
            section_num += 1

# 놓을 수 있는 다리 전체를 구하고, 
# 그 정보를 토대로 영역별로 이을 수 있는 최종 다리 하나씩만 남겨둠
section_bridge = [[2e9 for _ in range(section_num)] for _ in range(section_num)]
visit = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and not visit[i][j]:
            find_total_bridge(i,j,board[i][j])

# 그리고 정말로 최종 다리 목록들.
total_bridge = []
for i in range(1, section_num):
    for j in range(i):
        if section_bridge[i][j] != 2e9:
            total_bridge.append([i,j,section_bridge[i][j]])

# 놓을 수 있는 다리를 조합해서 
# 그 다리로 전체 영역을 연결할 수 있는지 확인한다.
# 그리고 answer를 갱신한다.
tmp = []
answer = 2e9
put_bridge(0,0)
if answer == 2e9: print(-1)
else: print(answer)