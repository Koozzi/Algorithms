# 00:38
# 01:00
# EOFError
from collections import deque

move = [[0,1],[0,-1],[1,0],[-1,0]]
move_horse = [[-2,-1],[-1,-2],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

def BFS():
    # visit[I][J][K] : K번 점프해서 I, J까지 가는데 걸린 시간
    visit = [[[2e9 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 0
    q = deque([[0,0,0]])

    while q:
        current_i, current_j, current_k = q.popleft()

        if current_i == N-1 and current_j == M-1:
            return min(visit[current_i][current_j])

        for di, dj in move:
            next_i = current_i + di
            next_j = current_j + dj

            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            if board[next_i][next_j] == 1:
                continue
            if visit[current_i][current_j][current_k] + 1 < visit[next_i][next_j][current_k]:
                visit[next_i][next_j][current_k] = visit[current_i][current_j][current_k] + 1
                q.append([next_i, next_j, current_k])

        if  current_k >= K: continue

        for di, dj in move_horse:
            next_i = current_i + di
            next_j = current_j + dj
            if not 0 <= next_i < N or not 0 <= next_j < M:
                continue
            if board[next_i][next_j] == 1:
                continue
            if visit[current_i][current_j][current_k] + 1 < visit[next_i][next_j][current_k+1]:
                visit[next_i][next_j][current_k+1] = visit[current_i][current_j][current_k] + 1
                q.append([next_i, next_j, current_k+1])

    return -1

if __name__ =="__main__":
    K = int(input())
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(BFS())