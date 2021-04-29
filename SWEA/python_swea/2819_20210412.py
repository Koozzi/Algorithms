"""
15:20
"""

def solve(current_i, current_j, cnt):
    if cnt == 7:
        new_string = ''.join(stack)
        if new_string not in s:
            s.add(new_string)
        return

    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_i = current_i + di
        next_j = current_j + dj
        if 0 <= next_i < 4 and 0 <= next_j < 4:
            stack.append(board[next_i][next_j])
            solve(next_i, next_j, cnt + 1)
            stack.pop()


T = int(input())
for t in range(1, T+1):
    s = set([])
    stack, board = [], []

    for _ in range(4):
        row = list(input().split())
        board.append(row)

    for i in range(4):
        for j in range(4):
            stack.append(board[i][j])
            solve(i, j, 1)
            stack.pop()

    print('#{0} {1}'.format(t, len(s)))