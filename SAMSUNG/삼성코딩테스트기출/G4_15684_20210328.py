
def go():
    for j in range(N):
        I, J = 0, j
        while True:
            if ladder[I][J] == 'R':
                I += 1
                J += 1
            elif ladder[I][J] == 'L':
                I += 1
                J -= 1
            elif ladder[I][J] == '.':
                I += 1
            if I == H:
                break
        if J != j:
            return False
    return True

def put_ladder(start_idx, cnt, c):

    if cnt == c:
        if go():
            print(cnt)
            exit()
        return

    for i in range(start_idx, H):
        for j in range(N-1):
            if ladder[i][j] == '.' and ladder[i][j+1] == '.':
                ladder[i][j] = 'R'
                ladder[i][j+1] = 'L'
                put_ladder(i, cnt+1, c)
                ladder[i][j] = '.'
                ladder[i][j+1] = '.'

if __name__=="__main__":
    N, M, H = map(int, input().split())
    ladder = [['.' for _ in range(N)] for _ in range(H)]
    for _ in range(M):
        A, B = map(int, input().split())
        ladder[A-1][B-1] = 'R'
        ladder[A-1][B] = 'L'

    for c in range(0,4):
        put_ladder(0,0,c)
    
    print(-1)