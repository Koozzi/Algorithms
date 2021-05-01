from collections import deque

def get_section(start_i, start_j, section_num):

    q = deque([[start_i, start_j]])
    visit[start_i][start_j] = True
    board[start_i][start_j] = section_num

    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            
            if board[next_i][next_j] == 0:
                start_bridge[section_num].append([next_i,next_j,move])

            if not visit[next_i][next_j] and board[next_i][next_j] == 1:
                q.append([next_i, next_j])
                visit[next_i][next_j] = True
                board[next_i][next_j] = section_num

def make_relation(num, bridges):

    for I, J, move in bridges:
        bridge_length = 0

        while True:
            bridge_length += 1
            I += move[0]
            J += move[1]
            if not 0 <= I < N or not 0 <= J < M:
                break

            if board[I][J] == num:
                break

            if board[I][J] > 0 and board[I][J] != num and bridge_length < 2:
                break

            if board[I][J] > 0 and board[I][J] != num and bridge_length > 1:
                relation_distance[num][board[I][J]] = min(relation_distance[num][board[I][J]], bridge_length)
                relation_distance[board[I][J]][num] = relation_distance[num][board[I][J]]
                break

def is_connected(relation):

    for idx in range(1, section_num+1):
        if not relation[idx]: return False

    visit = [ False for i in range(section_num+1) ]
    visit[1] = True
    q = deque([1])
    cnt = 1

    while q:
        c = q.popleft()
        for _next in relation[c]:
            if not visit[_next]:
                visit[_next] = True
                q.append(_next)
                cnt += 1
    
    if cnt == section_num: return True
    return False

def solve(start_idx):
    global answer

    distance_sum = 0
    relation = [[] for i in range(section_num+1)]

    for A, B in real_relation:
        distance_sum += relation_distance[A][B]
        relation[A].append(B)
        relation[B].append(A)

    # 만약에 모두 연결이 되어 있다.
    if is_connected(relation):
        answer = min(answer, distance_sum)

    for idx, island in enumerate(island_relation[start_idx:], start=start_idx):
        if used[idx]: continue
        used[idx] = True
        real_relation.append(island)
        solve(start_idx+1)
        real_relation.pop()
        used[idx] = False

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
visit = [[False for j in range(M)] for i in range(N)]
relation_distance = [[1000 for j in range(7)] for i in range(7)]
start_bridge = [ [] for i in range(7) ]
answer, section_num = 1000000, 0

for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 1:
            section_num += 1
            get_section(i,j,section_num)
    
for num, bridge in enumerate(start_bridge):
    if num == 0: continue
    if num > section_num: continue
    make_relation(num, bridge)

island_relation = []

for i in range(section_num+1):
    for j in range(i+1, section_num+1):
        if relation_distance[i][j] == 1000: continue
        island_relation.append([i,j])

real_relation = []
used = [False for j in range(len(island_relation))]

for idx, island in enumerate(island_relation):
    used[idx] = True
    real_relation.append(island)
    solve(idx+1)
    real_relation.pop()
    used[idx] = False

if answer == 1000000: print(-1)
else: print(answer)