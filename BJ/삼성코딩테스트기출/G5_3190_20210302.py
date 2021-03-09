from collections import deque

def change_direction(current_direction, D):
    if D == 'D': return (current_direction + 1) % 4
    elif D == 'L': return (current_direction -1) % 4

N = int(input())
board = [['.' for j in range(N)] for i in range(N)]
board[0][0] = 'S'

M = int(input())
for i in range(M):
    I,J = map(int, input().split())
    board[I-1][J-1] = 'A'

M = int(input())
direction_info = ['.' for i in range(10001)]
for i in range(M):
    T, D = input().split()
    direction_info[int(T)] = D
    
snake = deque([[0,0]])
move_direction = [[0,1],[1,0],[0,-1],[-1,0]]
current_d = 0

time = 0
while True:

    time += 1
    head_i = snake[0][0] + move_direction[current_d][0]
    head_j = snake[0][1] + move_direction[current_d][1]

    if not 0 <= head_i < N or not 0 <= head_j < N:
        break

    if board[head_i][head_j] == 'S': break
    elif board[head_i][head_j] == '.':
        tail_i, tail_j = snake.pop()
        board[tail_i][tail_j] = '.'
    snake.appendleft([head_i, head_j])
    board[head_i][head_j] = 'S'
    
    if direction_info[time] == 'D':
        current_d = change_direction(current_d, 'D')
    elif direction_info[time] == 'L':
        current_d = change_direction(current_d, 'L')

print(time)