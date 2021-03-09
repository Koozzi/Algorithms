def check_paper(I,J,size):
    for i in range(I,I+size):
        for j in range(J,J+size):
            if board[i][j] == 0:
                return False         
    return True

def put_paper(I,J,size,state):
    for i in range(I,I+size):
        for j in range(J,J+size):
            board[i][j] = state

def solve(cnt, left_paper_cnt):
    
    global answer
    
    if left_paper_cnt == 0:
        answer = min(answer, cnt)
        return

    if answer == 4 or answer == 0:
        print(answer)
        exit()

    if cnt == 25:
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for size in range(5,0,-1):
                    if paper_size[size] > 0 and i+size <= 10 and j+size <= 10:
                        if check_paper(i,j,size):
                            put_paper(i,j,size,0)
                            paper_size[size] -= 1
                            solve(cnt+1, left_paper_cnt-size*size)
                            paper_size[size] += 1
                            put_paper(i,j,size,1)
                return 
                # 사이즈가 1인 것부터 5인 것까지 돌렸을 때,
                # # 붙일 수 있는 색종이가 없으면 Return
                        

board = [list(map(int, input().split())) for i in range(10)]
paper_size = [0,5,5,5,5,5]
left_paper_cnt = 0
answer = 26

for i in range(10):
    for j in range(10):
        if board[i][j] == 1: 
            left_paper_cnt += 1

solve(0, left_paper_cnt)

if answer == 26: print(-1)
else: print(answer)