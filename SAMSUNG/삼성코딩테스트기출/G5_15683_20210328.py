# 16:00
# 16:38
# Recursion Error 조심할 것

from copy import deepcopy

cctv_watch = [
    [],
    [[[0,1]],[[0,-1]],[[-1,0]],[[1,0]]],
    [[[0,1],[0,-1]],[[1,0],[-1,0]],[[0,1],[0,-1]],[[1,0],[-1,0]]],
    [[[-1,0],[0,1]],[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]]],
    [[[0,-1],[1,0],[-1,0]], [[0,1],[1,0],[-1,0]], [[0,1],[0,-1],[-1,0]], [[0,1],[0,-1],[1,0]]],
    [[[0,1],[0,-1],[1,0],[-1,0]],[[0,1],[0,-1],[1,0],[-1,0]],[[0,1],[0,-1],[1,0],[-1,0]],[[0,1],[0,-1],[1,0],[-1,0]]],
]

def watch(total_direction_info):
    copied_board = deepcopy(board)
    
    for cctv_idx, current_direction in enumerate(total_direction_info):
        cctv_i, cctv_j, cctv_num = cctv_info[cctv_idx]
        for move in cctv_watch[cctv_num][current_direction]:
            next_i, next_j = cctv_i, cctv_j
            while True:
                next_i += move[0]
                next_j += move[1]
                if not 0 <= next_i < N or not 0 <= next_j < M:
                    break
                if copied_board[next_i][next_j] == 6:
                    break
                if 0 < copied_board[next_i][next_j] < 6:
                    continue
                if copied_board[next_i][next_j] == 0:
                    copied_board[next_i][next_j] = -1
    
    not_safe_area = 0
    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 0:
                not_safe_area += 1
            
    return not_safe_area

def solve(cnt):
    global answer
    if cnt == len(cctv_info):
        answer = min(answer, watch(total_direction_info))
        return

    for direction in range(4):
        total_direction_info.append(direction)
        solve(cnt+1)
        total_direction_info.pop()

if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = N * M
    
    total_direction_info = []
    cctv_info = []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and board[i][j] != 6:
                cctv_info.append([i,j,board[i][j]])

    solve(0)
    
    print(answer)