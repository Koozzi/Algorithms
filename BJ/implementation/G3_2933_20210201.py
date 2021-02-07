from collections import deque
from sys import stdin

def throw_stick(N, M, board, height, direction):
    if direction == -1:
        for j in range(M):
            if board[N-height][j] == 'x':
                board[N-height][j] = '.'
                break
    else:
        for j in range(M-1, -1, -1):
            if board[N-height][j] == 'x':
                board[N-height][j] = '.'
                break

    return board

def BFS(N, M, start_i, start_j, board, visit):
    
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])

    while q:
        current_i, current_j = q[0][0], q[0][1]
        
        q.popleft()
        for move in move_dir:
            next_i = current_i + move[0]
            next_j = current_j + move[1]

            if next_i < 0 or next_j < 0 or next_i > N or next_j >= M:
                continue

            if visit[next_i][next_j]:
                continue

            if board[next_i][next_j] == '.':
                continue

            visit[next_i][next_j] = True
            q.append([next_i, next_j])

    return visit
                
def fall(N, board, fall_list):

    fall_height = 0
    for k in range(1, N):
        flag = False
        for fall in fall_list:
            if fall[0]+k+1 > N: continue
            if fall[0]+k == N-1 or (board[fall[0]+k+1][fall[1]] == 'x' and [fall[0]+k+1, fall[1]] not in fall_list):
                fall_height = k
                flag = True
                break
        if flag: break

    for fall in fall_list:
        board[fall[0]][fall[1]] = '.'
    for fall in fall_list:
        board[fall[0]+fall_height][fall[1]] = 'x'

    return board

def solution(N, M, board, heights):
    direction = 1
    for height in heights:
        direction *= -1
        board = throw_stick(N, M, board, height, direction)
        
        visit = [[False for j in range(M)] for i in range(N+1)]
        visit = BFS(N, M, N, 0, board, visit)
        fall_list = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'x' and not visit[i][j]:
                    fall_list.append([i,j])

        if fall_list:
            board = fall(N, board, fall_list)

    board.pop()
    for i in board:
        print("".join(i))

if __name__=="__main__":
    N, M = map(int, stdin.readline().split())
    board = [list(stdin.readline()[:-1]) for i in range(N)]
    board.append(['x' for j in range(M)])
    K = int(stdin.readline())
    heights = list(map(int, stdin.readline().split()))

    solution(N, M, board, heights)