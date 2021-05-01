def go():
    global N, M

    for j in range(M):
        I, J = 0, j

        while True:
            if I == N:
                break
            if not ladder[I][J]:
                I += 1
            else:
                I, J = ladder[I][J]
                I += 1
        if J != j: return False

    return True

def solve(cnt, ladder_cnt, start_i):
    global N, M, answer

    if ladder_cnt == cnt:
        if go():
            print(ladder_cnt)
            exit()
        return

    for i in range(N):
        for j in range(M-1):
            if i < start_i: continue
            if not ladder[i][j] and not ladder[i][j+1]:
                ladder[i][j] = [i,j+1]
                ladder[i][j+1] = [i,j]
                solve(cnt+1, ladder_cnt, i)
                ladder[i][j+1] = []
                ladder[i][j] = []

M, H, N = map(int, input().split())
ladder = [[[] for j in range(M)] for i in range(N)]
for _ in range(H):
    A, B = map(int, input().split())
    A -= 1; B -= 1
    ladder[A][B] = [A,B+1]
    ladder[A][B+1] = [A,B]

if go():
    print(0)
    exit()

for ladder_cnt in range(1, 4):
    solve(0, ladder_cnt, 0)

print(-1)