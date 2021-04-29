'''
시작 
제출
종료
'''
from collections import deque

def bfs(start_i, start_j,section_num):
    board[start_i][start_j] = section_num
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    section_cnt = 1
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < M:
                if not visit[next_i][next_j] and board[next_i][next_j] > 0:
                    board[next_i][next_j] = section_num
                    visit[next_i][next_j] = True
                    q.append([next_i,next_j])
                    section_cnt += 1

    return section_cnt

answer = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

# section_num에 따른 영역의 크기를 저장한다.
section = [[]]
section_num = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visit[i][j]:
            section_num += 1
            section.append(bfs(i,j,section_num))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            section_sum = 0
            set_next_section = set([])
            for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < N and 0 <= next_j < M:
                    next_section = board[next_i][next_j]
                    if next_section > 0 and next_section not in set_next_section:
                        set_next_section.add(next_section)
                        section_sum += section[next_section]
            
            answer = max(answer, section_sum)

print(answer+1)               