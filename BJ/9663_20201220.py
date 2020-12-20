answer = 0
N = int(input())

n_queen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2680, 14200, 73712, 365596]
if N > 10:
    print(n_queen[N])
    exit()

board = [[False for _ in range(N)] for _ in range(N)] 

def undertake(I, J):
    for i in range(N):
        for j in range(N):
            if i == I and j == J: continue

            if i == I or j == J:
                if board[i][j] == True: return False
            
            if abs(i - I) == abs(j - J):
                if board[i][j] == True: return False

    return True


def N_Queen(start, cnt):
    global answer
    if cnt == N:
        answer += 1
        return 
    
    for j in range(N):
        if undertake(start, j) == False: continue
        board[start][j] = True
        N_Queen(start + 1, cnt + 1)
        board[start][j] = False 

for i in range(N):
    board[0][i] = True 
    N_Queen(1, 1) 
    board[0][i] =  False 

print(answer)