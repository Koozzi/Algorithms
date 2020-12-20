from collections import deque

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

move_dir = [[0,1], [0,-1], [1,0], [-1,0]]

def BFS(start_color, start_i, start_j):
    new_board = [['A' for _ in range(8)] for _ in range(8)] 
    q = deque()
    q.append([0, 0])
    new_board[0][0] = start_color

    while(len(q) != 0):
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()
        for i in range(4):
            next_i = current_i + move_dir[i][0]
            next_j = current_j + move_dir[i][1]

            if next_i < 0 or next_j < 0 or next_i == 8 or next_j == 8:
                continue 
            
            if new_board[next_i][next_j] == 'A':
                q.append([next_i, next_j])
                if new_board[current_i][current_j] == 'W':
                    new_board[next_i][next_j] = 'B'
                else:
                    new_board[next_i][next_j] = 'W'
    
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[i+start_i][j+start_j] != new_board[i][j]:
                cnt += 1

    return cnt

answer = 2e9
for i in range(0, N - 7):
    for j in range(0, M - 7):
        answer = min(answer, min(BFS('W', i, j), BFS('B', i, j)))

print(answer)