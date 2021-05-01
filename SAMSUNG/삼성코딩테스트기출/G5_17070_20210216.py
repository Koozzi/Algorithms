def solve(I,J,D):
    global N, answer
    if I==N-1 and J==N-1:
        answer += 1
        return

    if D == 'h' or D =='d':
        if J+1 < N:
            if board[I][J+1] == 0:
                solve(I,J+1,'h')
    
    if D == 'v' or D == 'd':
        if I+1 < N:
            if board[I+1][J] == 0:
                solve(I+1,J,'v')
    
    if D == 'h' or D == 'v' or D == 'd':
        if I+1 < N and J+1 < N:
            if board[I+1][J+1] == 0 and board[I][J+1] == 0 and board[I+1][J] == 0:
                solve(I+1, J+1, 'd')
            
answer = 0
N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
solve(0,1,'h')
print(answer)