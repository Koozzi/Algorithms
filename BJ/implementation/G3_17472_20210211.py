from collections import deque
from itertools import combinations

def check_bridge(board, current_i, current_j, direction):
    N, M = len(board), len(board[0])
    new_bridge = []

    while True:
        next_i = current_i + direction[0]
        next_j = current_j + direction[1]

        if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
            return [], 0, 0

        if board[next_i][next_j] == 0:
            new_bridge.append([next_i,next_j])

        else:
            return new_bridge, next_i, next_j

        current_i = next_i
        current_j = next_j

def BFS(board, start_i, start_j, visit, section, new_bridge, bridge_info):
    N, M = len(board), len(board[0])
    move_dir = [[0,1],[1,0],[-1,0],[0,-1]]
    q = deque( [ [start_i, start_j] ] )
    visit[start_i][start_j] = True
    board[start_i][start_j] = section
    
    while q:
        current_i, current_j = q[0][0], q[0][1]
        q.popleft()
        
        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                continue

            if board[next_i][next_j] == 0:
                bridge, end_i, end_j = check_bridge(board, current_i, current_j, move)
                bridge_reversed = list(reversed(bridge))

                if len(bridge) < 2: continue
                if bridge in new_bridge: continue
                if bridge_reversed in new_bridge: continue
                new_bridge.append(bridge)
                bridge_info.append([current_i, current_j, end_i, end_j, len(bridge)])
                continue
            
            if visit[next_i][next_j]:
                continue

            q.append([next_i, next_j])
            visit[next_i][next_j] = True
            board[next_i][next_j] = section

    return visit, new_bridge, board, bridge_info

def relation_check(start, relation, section):
    _visit = [False for i in range(7)]

    q = deque([start])
    _visit[start] = True
    cnt = 1

    while q:
        c = q[0]
        q.popleft()

        for next in relation[c]:
            if _visit[next]: continue
            q.append(next)
            _visit[next] = True
            cnt += 1
    
    if cnt == section: return True
    else: return False

def solution(N, M, board):

    ans = int(2e9)
    visit = [[False for j in range(M)] for i in range(N)]
    bridge = []
    bridge_info = []
    section = 0

    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] != 0:
                section += 1
                visit, bridge, board, bridge_info = BFS(board, i, j, visit, section, bridge, bridge_info)

    for cnt in range(1, len(bridge_info)+1):
        comb_bridge = list(combinations(bridge_info, cnt))
        for new_bridge in comb_bridge:
            land_relation = []
            for b in new_bridge:
                section1 = board[b[0]][b[1]]
                section2 = board[b[2]][b[3]]
                length = b[4]
                land_relation.append([section1, section2, length])

            relation = [[] for i in range(7)]

            length_sum = 0
            for r in land_relation:
                relation[r[0]].append(r[1])
                relation[r[1]].append(r[0])
                length_sum += r[2]
            
            if relation_check(land_relation[0][0], relation, section):
                ans = min(ans, length_sum)

    if ans == int(2e9): return -1
    return ans

if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]

    print(solution(N, M, board))