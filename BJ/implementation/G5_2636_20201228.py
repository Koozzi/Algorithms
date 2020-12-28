from collections import deque
from copy import deepcopy
from sys import stdin

def melt(N, M, board):
    new_board = deepcopy(board)
    move_dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[0][0] = True
    q = deque([(0,0)])

    while len(q) != 0:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()

        for i in range(4):
            next_i = current_i + move_dir[i][0]
            next_j = current_j + move_dir[i][1]

            if next_i < 0 or next_j < 0 or next_i == N or next_j == M:
                continue

            if visit[next_i][next_j] == True:
                continue

            if new_board[next_i][next_j] == 0:
                q.append((next_i, next_j))
                visit[next_i][next_j] = True

            if new_board[next_i][next_j] == 1:
                visit[next_i][next_j] = True
                new_board[next_i][next_j] = 0
                
    return new_board

def is_cheeze_left(board):
    cheeze_cnt = 0
    for row in board:
        for item in row:
            if item == 1: cheeze_cnt += 1
    
    return cheeze_cnt

board = []
N, M = map(int, stdin.readline().split())
for _ in range(N):
    board_row = list(map(int, stdin.readline().split()))
    board.append(board_row)

# 주어진 board에 이미 치즈가 없는 경우
if is_cheeze_left(board) == 0:
    print(0)
    print(0)
    exit()

time = 0
prev_cheeze = 0
'''
1. 시간을 +1 해줌
2. 현재 남은 치즈의 값을 구해줌 -> prev_cheeze에 저장
3. BFS를 사용해서 바깥공기와 맞닿는 부분을 지워줌
4. 다시 현재 남은 치즈의 값을 구해줌
5. 바깥공기와 맞닿는 부분을 지워주고 현재 남은 치즈가 0이면
6. 걸린 시간과 prev_cheeze를 출력
'''
while True:
    time += 1
    prev_cheeze = is_cheeze_left(board)
    board = melt(N, M, board)
    present_cheeze = is_cheeze_left(board)
    if present_cheeze == 0:
        print(time)
        print(prev_cheeze)
        break