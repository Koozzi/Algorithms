from itertools import combinations
from copy import deepcopy

def check(copied_board):
    global N, M
    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 1:
                return False
    return True

def enemy_move(copied_board):
    global N, M
    new_board = [[0 for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 1:
                if i == N-1: continue
                new_board[i+1][j] = 1

    return new_board

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for j in range(N)]
comb_archer = list(combinations([i for i in range(M)], 3))
answer = 0

for archer in comb_archer:

    enemy_sum = 0
    copied_board = deepcopy(board)
    while True:
        # 거리가 D이하인 적들을 찾는다.
        archer_enemy = [[] for j in range(M)]
        for i in range(N):
            for j in range(M):
                if copied_board[i][j] == 1:
                    for idx in archer:
                        _D = abs(N-i) + abs(idx-j)
                        if _D <= D:
                            archer_enemy[idx].append([i,j,_D])

        # 적 죽임
        killed_enemy = set([])
        for idx in archer:
            if not archer_enemy[idx]: continue
            archer_enemy[idx].sort(key=lambda x:(x[2], x[1]))
            I, J, _D = archer_enemy[idx][0]
            copied_board[I][J] = 0
            killed_enemy.add(str(I)+str(J))
        
        enemy_sum += len(killed_enemy)

        # 적이 이동함
        copied_board = enemy_move(copied_board)

        # 격자판에 적이 남아있는지 Check
        if check(copied_board):
            break

    answer = max(answer, enemy_sum)

print(answer)