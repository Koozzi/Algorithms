def change_direction():
    if I+J == N+1 and I != J \
        or I == J and I > init_i and J > init_j \
            or I+1 == J and I < init_i and J <= init_j:
            return (D + 1) % 4
    return D

N = int(input())
M = int(input())

board = [[0 for _ in range(N+1)] for _ in range(N+1)]
move = [[-1,0],[0,1],[1,0],[0,-1]]

I = J = init_i = init_j = (N+1)//2
board[I][J] = 1
num, D = 2, 0
answer_i, answer_j = 0, 0 

while True:
    I += move[D][0]
    J += move[D][1]

    board[I][J] = num
    if num == M:
        answer_i = I
        answer_j = J
    num += 1

    if I == 1 and J == 1:
        break

    D = change_direction()

for row in board[1:]:
    print(*row[1:])

print(answer_i, answer_j)
