from sys import stdin
from collections import deque

def make_boundary(N, boundary):
    X, Y, D1, D2 = boundary[0], boundary[1], boundary[2], boundary[3]
    boundary_board = [[0 for i in range(N+1)] for i in range(N+1)]

    boundary_board[X][Y] = 5
    boundary_board[X+D2][Y+D2] = 5
    boundary_board[X+D1][Y-D1] = 5

    for d1 in range(1, D1+1):
        for d2 in range(1, D2+1):
            boundary_board[X+d1][Y-d1] = 5
            boundary_board[X+d2][Y+d2] = 5
            boundary_board[X+D2+d1][Y+D2-d1] = 5
            boundary_board[X+D1+d2][Y-D1+d2] = 5

    for i in range(X+1, X+D1+D2):
        flag = False
        for j in range(1, N+1):
            if boundary_board[i][j] == 5 and not flag:
                flag = True
                continue

            if boundary_board[i][j] == 5 and flag:
                break

            if flag:
                boundary_board[i][j] = 5
                
    for i in range(1, N+1):
        for j in range(1, N+1):
            if boundary_board[i][j] == 5: continue

            if 1 <= i < X+D1 and 1 <= j <= Y: boundary_board[i][j] = 1
            elif 1 <= i <= X+D2 and Y < j <= N: boundary_board[i][j] = 2
            elif X+D1 <= i <= N and 1 <= j < Y-D1+D2: boundary_board[i][j] = 3
            elif X+D2 < i <= N and Y-D1+D2 <= j <= N: boundary_board[i][j] = 4
            else: boundary_board[i][j] = 5

    return boundary_board

def get_boundary_value(start_i, start_j, board, boundary_board, visit, boundary):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    q = deque([[start_i, start_j]])
    visit[start_i][start_j] = True
    location_num = boundary_board[start_i][start_j]
    location_sum = board[start_i][start_j]

    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()

        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            # 밖으로 나가면 무시 (Out of Index)
            if next_i <= 0 or next_j <= 0 or next_i > N or next_j > N:
                continue

            # 해당 선거구가 아닐 경우 무시
            if boundary_board[next_i][next_j] != location_num:
                continue

            # 방문한적이 있으면 무시
            if visit[next_i][next_j]:
                continue

            q.append([next_i, next_j])
            visit[next_i][next_j] = True
            location_sum += board[next_i][next_j]

    return location_sum, visit

def solution(N, board):
    min_gap = 2e9

    # 가능한 경계 기준점과 경계선의 길이의 조합을 구하고 리스트에 넣어준다. [[x,y,d1,d2], [x,y,d1,d2], ...]
    possible_value = []
    for i in range(1, N-1):
        for j in range(2, N):
            X, Y = i, j
            for D1_D2 in range(2, N-X+1):
                for D1 in range(1, D1_D2):
                    D2 = D1_D2 - D1
                    if 1 <= Y-D1 < Y and Y < Y+D2 <= N:
                        possible_value.append([X,Y,D1,D2])

    for boundary in possible_value:
        min_value, max_value = 2e9, 0
        boundary_board = make_boundary(N, boundary) # 경계 기준점과 경계선의 길이를 통해서 선거구을 나눔

        visit = [[False for i in range(N+1)] for i in range(N+1)]
        # BFS를 통해서 각 선거구의 값을 구한다.
        l = []
        for i in range(1,N+1):
            for j in range(1,N+1):
                if not visit[i][j]:
                    boundary_value, visit = get_boundary_value(i, j, board, boundary_board, visit, boundary) 
                    # 나오는 결과마다 최소값, 최대값을 갱신한다.
                    min_value = min(min_value, boundary_value)
                    max_value = max(max_value, boundary_value)
                    
        
        # 현재 나누어진 선거구 기준으로 최대값와 최소값의 차이에 대해서 갱신한다.
        min_gap = min(min_gap, max_value - min_value)

    return min_gap

if __name__=="__main__":
    N = int(stdin.readline())
    
    board = [[0 for i in range(N+1)]]
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        row.insert(0,0)
        board.append(row)

    print(solution(N, board))