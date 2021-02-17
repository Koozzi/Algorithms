from collections import deque
from sys import stdin

T = int(input())
N, M, answer = 0, 0, 0
board = []
key_set = set([])
move_dir = [[0,1],[0,-1],[1,0],[-1,0]]

def BFS(start_i, start_j):
    global N, M, answer

    check = 0
    visit = [[False for j in range(M+2)] for i in range(N+2)]
    q = deque([[start_i, start_j]])
    visit[start_i][start_j] = True

    while q:
        ci, cj = q[0][0], q[0][1]
        q.popleft()

        for move in move_dir:
            ni, nj = ci + move[0], cj + move[1]

            # 밖으로 나가는 경우
            if ni < 0 or nj < 0 or ni > N+1 or nj > M+1:
                continue
            
            # 벽을 만나는 경우
            if board[ni][nj] == '*':
                continue

            # 이미 방문한 곳
            if visit[ni][nj]:
                continue
            
            # 문을 만나는 경우
            if 'A' <= board[ni][nj] <= 'Z':
                need_key = chr(ord(board[ni][nj]) + 32)
                if need_key in key_set:
                    board[ni][nj] = '.'
                    q.append([ni,nj])
                    visit[ni][nj] = True

            # 키를 만나는 경우    
            elif 'a' <= board[ni][nj] <= 'z':
                check += 1
                key_set.add(board[ni][nj])
                board[ni][nj] = '.'
                return ni, nj

            # 문서를 만나는 경우
            elif board[ni][nj] == '$':
                board[ni][nj] = '.'
                q.append([ni,nj])
                visit[ni][nj] = True
                answer += 1

            elif board[ni][nj] == '.':
                q.append([ni,nj])
                visit[ni][nj] = True
    
    return -1, -1


for t in range(T):
    answer = 0
    key_set = set([])
    board = [['.' for j in range(110)] for i in range(110)]
    N, M = map(int, input().split())
    for i in range(1,N+1):
        board[i][1:M+1] = list(input())
    
    key = input()
    if key == '0': key_set = set([])
    else: key_set = set(list(key)) 

    start_i, start_j = 0, 0
    while True:
        start_i, start_j = BFS(start_i, start_j)

        if start_i == -1 and start_j == -1:
            print(answer)
            break