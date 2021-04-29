from collections import deque


N = int(input())
M = int(input())
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(M):
    i, j = map(int, input().split())
    board[i][j] = 1

command = deque([])
K = int(input())
for _ in range(K):
    time, direction = input().split()
    command.append([int(time), direction])

answer = 0
i, j, d = 1, 1, 0
snake = deque([[i, j]])
while True:
    answer += 1

    i += move[d][0]
    j += move[d][1]

    if not 1 <= i <= N or not 1 <= j <= N:
        break

    if [i, j] in snake:
        break

    snake.appendleft([i, j])

    if board[i][j] == 0:
        snake.pop()
    elif board[i][j] == 1:
        board[i][j] = 0

    if command:
        if answer == command[0][0]:
            t, c = command.popleft()
            if c == 'D':
                d = (d + 1) % 4
            elif c == 'L':
                d = (d - 1) % 4

print(answer)
