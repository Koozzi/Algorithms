'''
시작 22:40
제출 22:58
종료
'''
N, M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
water = [[0 for _ in range(M)] for _ in range(N)]
wall = list(map(int, input().split()))

for j in range(M):
    for i in range(wall[j]):
        board[i][j] = 1

for i in range(N):
    left_found = False
    for j in range(M):
        if board[i][j] == 1:
            left_found = True
        
        if left_found:
            if board[i][j] == 0:
                water[i][j] = 1

answer = 0
for i in range(N):
    right_found = False
    for j in range(M-1, -1, -1):
        if board[i][j] == 1:
            right_found = True
        
        if right_found:
            if water[i][j] == 1:
                answer += 1

print(answer)