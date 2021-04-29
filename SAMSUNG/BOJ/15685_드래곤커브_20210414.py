def draw_dragon_curve(dragon_curve):

    new_dragon_curve = []
    end_point_i, end_point_j = dragon_curve[-1]
    dragon_curve = list(reversed(dragon_curve))

    for I, J in dragon_curve[1:]:
        di = I - end_point_i
        dj = J - end_point_j
        new_dragon_curve.append([end_point_i+dj, end_point_j-di])

    return new_dragon_curve


N = int(input())
board = [[False for _ in range(101)] for _ in range(101)]
move = [[0, 1], [-1, 0], [0, -1], [1, 0]]

for _ in range(N):
    i, j, d, s = map(int, input().split())
    dragon_curve = [[j, i], [j+move[d][0], i+move[d][1]]]
    for __ in range(1, s+1):
        dragon_curve += draw_dragon_curve(dragon_curve)

    for I, J in dragon_curve:
        board[I][J] = True

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            answer += 1

print(answer)