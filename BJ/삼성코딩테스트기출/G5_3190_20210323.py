# 14:27
# 14:59

from collections import deque

def change_direction():
    global snake_direction
    if snake_move_info[0][1] == 'D':
        snake_direction = (snake_direction + 1) % 4
    elif snake_move_info[0][1] == 'L':
        snake_direction -= 1
        if snake_direction == -1:
            snake_direction = 3
    snake_move_info.popleft()

def solve():
    global snake_direction

    t = 0
    while True:
        t += 1

        head_i, head_j = snake[0]

        # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        next_i = head_i + move_dir[snake_direction][0]
        next_j = head_j + move_dir[snake_direction][1]

        # 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
        if not 0 <= next_i < N or not 0 <= next_j < N:
            break

        if board[next_i][next_j] == 9:
            break

        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if board[next_i][next_j] == 1:
            board[next_i][next_j] = 9
            snake.appendleft([next_i,next_j])

        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        elif board[next_i][next_j] == 0:
            snake.appendleft([next_i,next_j])
            tail_i, tail_j = snake.pop()
            board[next_i][next_j] = 9
            board[tail_i][tail_j] = 0

        if snake_move_info:
            if t == snake_move_info[0][0]:
                change_direction()

    return t

if __name__=="__main__":
    N = int(input())
    K = int(input())
    board = [[0 for j in range(N)] for i in range(N)]
    move_dir = [[0,1],[1,0],[0,-1],[-1,0]]
    for _ in range(K):
        I, J = map(int, input().split())
        board[I-1][J-1] = 1
    
    snake_move_info = deque([])
    L = int(input())
    for _ in range(L):
        T, D = input().split()
        snake_move_info.append([int(T), D])
    
    snake_direction = 0
    snake = deque([[0,0]])
    board[0][0] = 9

    print(solve())