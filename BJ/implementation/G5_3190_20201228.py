from collections import deque

move_dir = [[-1,0],[0,1],[1,0],[0,-1]]
def change_direction(d, c):
    if c == 'L': return (d - 1) % 4
    if c == 'D': return (d + 1) % 4


def solve(board, N, times):
    time = 1
    direction = 1
    current_i, current_j = 1, 1
    snake = deque([(1,1)])
    while True:
        next_i = current_i + move_dir[direction][0]
        next_j = current_j + move_dir[direction][1]

        if 1 <= next_i <= N and 1 <= next_j <= N and board[next_i][next_j] != 1:
            snake_end_i = snake[-1][0]
            snake_end_j = snake[-1][1]

            if board[next_i][next_j] == 0:
                board[snake_end_i][snake_end_j] = 0
                snake.pop()
            board[next_i][next_j] = 1
            snake.appendleft((next_i, next_j))

            if time in times.keys():
                direction = change_direction(direction, times[time])
            time += 1
            current_i, current_j = next_i, next_j

        else: 
            return time

if __name__ == "__main__":
    N = int(input())
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    board[1][1] = 1

    K = int(input())
    for _ in range(K):
        I, J = map(int, input().split())
        board[I][J] = 2

    L = int(input())
    times = {}
    for _ in range(L):
        T, C = input().split()
        times[int(T)] = C

    print(solve(board, N, times))