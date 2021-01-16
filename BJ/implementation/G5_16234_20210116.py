from collections import deque

def people_move(start_i, start_j, N, L, R, board,visit):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]

    visit[start_i][start_j] = True # BFS 노드 방문 체크
    region = [[start_i, start_j]] # 방문한 지역
    region_sum = board[start_i][start_j] # 지역을 방문할 때마다 값을 더해줌
    q = deque([[start_i, start_j]]) # BFS Queue
    moved = False # 새로운 노으(지역)에 방문한 적이 있는지

    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()
        for i in range(4):
            next_i = current_i + move_dir[i][0]
            next_j = current_j + move_dir[i][1]

            # board밖으로 나갈 경우 무시
            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= N:
                continue

            # 방문한 적이 있으면 무시
            if visit[next_i][next_j]:
                continue
            
            # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하...
            if L <= abs(board[current_i][current_j] - board[next_i][next_j]) <= R:
                q.append([next_i, next_j])
                visit[next_i][next_j] = True
                region.append([next_i, next_j])
                region_sum += board[next_i][next_j]
                moved = True
    
    # 인구 이동이 없었으면 그대로 Return
    if not moved:
        return visit, board, False

    # 인구 이동이 있었다면 board을 수정해서 Return
    people_avg = region_sum // len(region)
    for idx in region:
        I, J = idx[0], idx[1]
        board[I][J] = people_avg

    return visit, board, True

def solution(N, L, R, board):
    move_cnt = 0

    while True:
        visit = [[False for i in range(N)] for i in range(N)]
        update = 0

        for i in range(N):
            for j in range(N):
                if visit[i][j]: continue
                visit, board, moved = people_move(i, j, N, L, R, board, visit)
                if moved: update += 1
        
        if update > 0: move_cnt += 1
        else: break

    return move_cnt

if __name__=="__main__":
    N, L, R = map(int, input().split())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    print(solution(N, L, R, board))