from itertools import combinations
from copy import deepcopy


def go():
    for j in range(1,M+1):
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

            if I == N+1:
                break

        if J != j:
            return False

    return True


def put_ladder(start_idx, cnt, max_count):

    if cnt == max_count:
        if go():
            print(cnt)
            exit()
        return

    for i in range(start_idx, N+1):
        for j in range(M):
            if ladder[i][j] == '.' and ladder[i][j+1] == '.':
                ladder[i][j] = 'R'
                ladder[i][j+1] = 'L'
                put_ladder(i, cnt+1, max_count)
                ladder[i][j] = '.'
                ladder[i][j+1] = '.'


M, H, N = map(int, input().split())
ladder = [['.' for _ in range(M+1)] for _ in range(N+1)]
for _ in range(H):
    I, J = map(int, input().split())
    ladder[I][J] = 'R'
    ladder[I][J+1] = 'L'

if go():
    print(0)
    exit()

for max_count in range(1, 4):
    put_ladder(1, 0, max_count)

print(-1)