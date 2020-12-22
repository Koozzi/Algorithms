N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

answer = 1
length = 1
while length < N and length < M:
    for i in range(N - length):
        for j in range(M - length):
            if board[i][j] == board[i][j+length] == board[i+length][j+length]  == board[i+length][j]:
                answer = max(answer, length + 1)
    
    length += 1

print(answer ** 2)