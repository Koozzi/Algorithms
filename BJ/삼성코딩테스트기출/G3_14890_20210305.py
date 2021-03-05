def check(l):
    global N, L
    
    tmp = 0
    for i in range(1, N):
        if abs(l[i] - l[i-1]) > 1:
            return False
        
        # 상승
        if l[i] > l[i-1] :
            if tmp + L > i:
                return False
            tmp =  i
            
        # 하강    
        elif l[i-1] > l[i]:
            if i + L > N: 
                return False
            for j in range(i, i + L - 1):
                if l[j] != l[j+1]: 
                    return False
            tmp = i + L

    return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
answer = 0

for row in board:
    if check(row):
        answer += 1

for j in range(N):
    row = []
    for i in range(N):
        row.append(board[i][j])
    if check(row):
        answer += 1

print(answer)