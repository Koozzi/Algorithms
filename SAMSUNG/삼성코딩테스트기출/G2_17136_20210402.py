'''
시작 20:00
제출 20:26
종료
'''

def can_put_paper(I,J,S):
    for i in range(I,I+S):
        for j in range(J,J+S):
            if board[i][j] == 0:
                return False
    return True

def paper_put_or_off(I,J,S,state):
    for i in range(I,I+S):
        for j in range(J,J+S):
            board[i][j] = state

def solve(cnt, total_paper_cnt):
    global answer

    if total_paper_cnt == 0:
        answer = min(answer, cnt)
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for size in range(5,0,-1):
                    if paper_cnt[size] > 0 and i+size <= 10 and j+size <= 10:
                        if can_put_paper(i,j,size):
                            paper_put_or_off(i,j,size,0)
                            paper_cnt[size] -= 1
                            solve(cnt+1, total_paper_cnt-size*size)
                            paper_cnt[size] += 1
                            paper_put_or_off(i,j,size,1)
                return

board = [list(map(int, input().split())) for _ in range(10)]
paper_cnt = [0, 5, 5, 5, 5, 5]
total_paper_cnt = 0
answer = 26

for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            total_paper_cnt += 1

solve(0, total_paper_cnt)

if answer == 26: print(-1)
else: print(answer)