def DFS(I, J, cnt):
    if cnt == 6:
        number_string = ''.join(stack)
        if number_string not in num_list:
            num_list.add(number_string)
        return
    
    for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        next_i = I + di
        next_j = J + dj
        if 0 <= next_i < 5 and 0 <= next_j < 5:
            stack.append(board[next_i][next_j])
            DFS(next_i, next_j, cnt+1)
            stack.pop()

board = list(input().split() for _ in range(5))
num_list = set([])
stack = []

for i in range(5):
    for j in range(5):
        stack.append(board[i][j])
        DFS(i, j, 1)
        stack.pop()
    
print(len(num_list))