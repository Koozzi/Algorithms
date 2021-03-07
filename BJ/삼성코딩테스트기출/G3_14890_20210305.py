def bridge_check(l):
    global N, L
    
    tmp = 0 # 상승 경사로 시작이 가능한 곳
    for i in range(1, N):
        if abs(l[i]-l[i-1]) > 1:
            return False

        # 하강
        if l[i-1] > l[i]:
            if i + L > N:
                return False
            for j in range(i, i+L-1):
                if l[j] != l[j+1]:
                    return False
            tmp = i+L
        
        if l[i-1] < l[i]:
            if tmp + L > i:
                return False
            tmp = i

    return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
answer = 0

for row in board:
    if bridge_check(row):
        answer += 1

for j in range(N):
    col = []
    for i in range(N):
        col.append(board[i][j])
    if bridge_check(col):
        answer += 1

print(answer)