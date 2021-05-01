def paper_put_off(I,J,S,state):
    for i in range(I, I+S):
        for j in range(J, J+S):
            board[i][j] = state

def can_attach(I,J,S):
    for i in range(I,I+S):
        for j in range(J,J+S):
            if board[i][j] == 0:
                return False
    return True

def solve(cnt, total_paper_cnt):
    global answer

    if total_paper_cnt == 0:
        answer = min(answer, cnt)
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for s in range(5, 0, -1):
                    if paper[s] > 0 and i+s <= 10 and j+s <= 10:
                        if can_attach(i,j,s):
                            paper_put_off(i,j,s,0)
                            paper[s] -= 1
                            solve(cnt+1, total_paper_cnt-s*s)
                            paper[s] += 1 
                            paper_put_off(i,j,s,1)
                return

board = [list(map(int, input().split())) for i in range(10)]
paper = [0,5,5,5,5,5]
total_paper_cnt = 0
answer = 26

for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            total_paper_cnt += 1

solve(0, total_paper_cnt)

if answer == 26: print(-1)
else: print(answer)