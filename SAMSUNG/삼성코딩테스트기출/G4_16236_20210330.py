# 14:20
# 14:50
# 초반에 설계를 할 때 살짝 꼬였음. 다음부터는 절대 이런 일이 없어야 할 것.

from collections import deque

def shark_find_fish(shark_i, shark_j, shark_s):
    visit = [[False for _ in range(N)] for i in range(N)]
    visit[shark_i][shark_j] = True
    q = deque([[shark_i, shark_j, 0]])
    fish_candidate = []
    while q:
        current_i, current_j, current_d = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if not 0 <= next_i < N or not 0 <= next_j < N:
                continue
            if board[next_i][next_j] > shark_s:
                continue
            if visit[next_i][next_j]:
                continue
            if 0 < board[next_i][next_j] < shark_s:
                fish_candidate.append([current_d+1, next_i, next_j])
            visit[next_i][next_j] = True
            q.append([next_i, next_j, current_d+1])
        
    fish_candidate.sort()
    return fish_candidate
    
def shark_move(next_i, next_j, next_d):
    global shark_i, shark_j, answer

    answer += next_d
    board[shark_i][shark_j] = 0
    board[next_i][next_j] = 9
    shark_i, shark_j = next_i, next_j

if __name__=="__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    shark_i, shark_j, shark_s = 0, 0, 2
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                shark_i, shark_j = i, j
    
    answer = 0
    shark_size_exp = 0
    while True:
        fish_candidate = shark_find_fish(shark_i, shark_j, shark_s)
        if not fish_candidate:
            break

        shark_size_exp += 1
        if shark_size_exp == shark_s:
            shark_s += 1
            shark_size_exp = 0

        next_d, next_i, next_j = fish_candidate[0]
        shark_move(next_i, next_j, next_d)
    
    print(answer)