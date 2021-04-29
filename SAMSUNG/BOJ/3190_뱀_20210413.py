from collections import deque

N = int(input())
M = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(M):
    I, J = map(int, input().split())
    board[I-1][J-1] = 1

snake = deque([[0, 0]])
command = deque([])
K = int(input())
for _ in range(K):
    T, D = input().split()
    command.append([int(T), D])


D, T = 0, 0
while True:

    T += 1
    current_i, current_j = snake[0]

    next_i = current_i + move[D][0]
    next_j = current_j + move[D][1]

    # 벽에 부딪히는 경우
    if not 0 <= next_i < N or not 0 <= next_j < N:
        break

    # 자기 몸에 부딪히는 경우
    if [next_i, next_j] in snake:
        break

    snake.appendleft([next_i, next_j])

    if board[next_i][next_j] == 1:
        board[next_i][next_j] = 0

    elif board[next_i][next_j] == 0:
        snake.pop()

    if command:
        t, c = command[0]
        if T == t:
            command.popleft()
            if c == 'D':
                D = (D + 1) % 4
            elif c == 'L':
                D = (D - 1) % 4

print(T)





