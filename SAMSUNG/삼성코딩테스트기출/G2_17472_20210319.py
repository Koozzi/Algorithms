from collections import deque

def make_section(start_i, start_j, section):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    board[start_i][start_j] = section
    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if 0 <= next_i < N and 0 <= next_j < M:
                if board[next_i][next_j] == 1 and not visit[next_i][next_j]:
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])
                    board[next_i][next_j] = section

def bridge_check(I, J, move, section):
    length = 1
    while True:
        I, J = I + move[0], J + move[1]
        if not 0 <= I < N or not 0 <= J < M:
            return None, False, None

        if board[I][J] == section:
            return None, False, None

        if board[I][J] > 0 and board[I][J] != section:
            if length < 2: return None, False, None
            else: return board[I][J], True, length

        length += 1 

def find_bridge(start_i, start_j, section):
    
    bridge = []
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    while q:
        current_i, current_j = q.popleft()
        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            if 0 <= next_i < N and 0 <= next_j < M:
                if board[next_i][next_j] == 0:
                    next_city, valid, length = bridge_check(next_i, next_j, move, section)
                    if valid: bridge.append([section, next_city, length])
                if board[next_i][next_j] == section and not visit[next_i][next_j]:         
                    visit[next_i][next_j] = True
                    q.append([next_i, next_j])

    return bridge

def check_connected(final_bridge):
    
    visit = [False for j in range(total_section)]
    sub_relation = [[] for j in range(total_section)]
    
    for I,J,L in final_bridge:
        sub_relation[I].append([J,L])
        sub_relation[J].append([I,L])

    cnt, total_length = 1, 0
    visit[1] = True
    q = deque([1])

    while q:
        current_node = q.popleft()
        for next_node, L in sub_relation[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)
                total_length += L
                cnt += 1
    
    if cnt == total_section-1: return True, total_length
    else: return False, total_length

def solve(start_idx):
    global answer
    
    valid, total_length = check_connected(final_bridge)
    if valid: answer = min(answer, total_length)

    for idx, bridge_info in enumerate(bridge[start_idx:], start=start_idx):
        if not used[idx]:
            final_bridge.append(bridge_info)
            used[idx] = True
            solve(idx+1)
            used[idx] = False
            final_bridge.pop()

answer = 2e9
N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

total_section = 1
visit = [[False for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 1:
            make_section(i,j,total_section)
            total_section += 1

bridge_list = []
visit = [[False for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] > 0:
            bridge_list += find_bridge(i,j,board[i][j])

relation = [[2e9 for j in range(total_section)] for i in range(total_section)]
for current_city, next_city, length in bridge_list:
    if length < relation[current_city][next_city]:
        relation[current_city][next_city] = length
        relation[next_city][current_city] = length

bridge = []
for i in range(total_section):
    for j in range(i):
        if not relation[i][j] == 2e9:
            bridge.append([i,j,relation[i][j]])

final_bridge = []
used = [False for _ in range(len(bridge))]
for idx, bridge_info in enumerate(bridge):
    final_bridge.append(bridge_info)
    used[idx] = True
    solve(idx+1)
    used[idx] = False
    final_bridge.pop()

if answer == 2e9: print(-1)
else: print(answer)