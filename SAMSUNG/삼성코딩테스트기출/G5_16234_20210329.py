# 14:25
#
# 오타 오타 오타 오타

from collections import deque

def get_union(start_i, start_j, visit, union_idx,union_board):
    
    union_cnt, union_sum = 1, board[start_i][start_j]
    q = deque([[start_i, start_j]])   
    visit[start_i][start_j] = True 
    union_board[start_i][start_j] = union_idx
    
    while q:
        current_i, current_j = q.popleft()
        current_num = board[current_i][current_j]

        for move in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + move[0]
            next_j = current_j + move[1]
            
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue

            next_num = board[next_i][next_j]
            if not visit[next_i][next_j]:
                if L <= abs(current_num - next_num) <= R:
                    
                    q.append([next_i,next_j])
                    visit[next_i][next_j] = True
                    union_board[next_i][next_j] = union_idx
                    union_sum += board[next_i][next_j]
                    union_cnt += 1

    return visit,union_cnt,union_sum,union_board

def solution():
    move_cnt = 0

    while True:
        moved = False
        union_board = [[-1 for _ in range(N)] for _ in range(N)]
        visit = [[False for _ in range(N)] for _ in range(N)]
        union_info, union_idx = [], 0 
        for i in range(N):
            for j in range(N):
                if visit[i][j]: continue

                visit,union_cnt,union_sum,union_board = get_union(i,j,visit,union_idx,union_board)
            
                if union_cnt > 1:
                    moved = True

                union_info.append(union_sum // union_cnt)
                union_idx += 1

        if moved:
            move_cnt += 1
            for i in range(N):
                for j in range(N):
                    if union_board[i][j] == -1: continue
                    union_idx = union_board[i][j]
                    board[i][j] = union_info[union_idx]

        else:
            break

    return move_cnt

if __name__=="__main__":
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution())