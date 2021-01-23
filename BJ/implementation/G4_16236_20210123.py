from collections import deque

def get_distance(N, board, shark_i, shark_j, shark_s):
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit = [[False for j in range(N)] for i in range(N)]
    depth = [[0 for j in range(N)] for i in range(N)]
    q = deque([[shark_i, shark_j]])
    visit[shark_i][shark_j] = True
    distance_info = []

    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()

        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= N:
                continue

            if board[next_i][next_j] > shark_s:
                continue

            if visit[next_i][next_j]:
                continue

            q.append([next_i, next_j])
            visit[next_i][next_j] = True
            depth[next_i][next_j] = depth[current_i][current_j] + 1

            if  0 < board[next_i][next_j] < shark_s:
                distance_info.append([next_i, next_j, depth[next_i][next_j]])

    return distance_info

def get_shark_location(N, board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                return i, j, 2

def solution(N, board):
    time = 0
    shark_tmp = 0
    
    shark_i, shark_j, shark_s = get_shark_location(N, board)

    while True:
        fish_can_eat = get_distance(N, board, shark_i, shark_j, shark_s)
        fish_can_eat.sort(key=lambda x : (x[2], x[0], x[1]))

        if fish_can_eat:
            board[shark_i][shark_j] = 0
            shark_i = fish_can_eat[0][0]
            shark_j = fish_can_eat[0][1]
            board[shark_i][shark_j] = 9
            time += fish_can_eat[0][2]
            shark_tmp += 1

            if shark_tmp == shark_s:
                shark_s += 1
                shark_tmp = 0

        else: break

    return time

if __name__ == "__main__":
    N = int(input())

    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    print(solution(N, board))