from itertools import combinations
from copy import deepcopy

def kill_enemy(archers):

    archer_can_kill = [ [] for i in range(M) ]
    kill = set([])

    for archer in archers:
        for i in range(N):
            for j in range(M):
                if copied_board[i][j] == 1:
                    if abs(N-i) + abs(archer-j) <= K:
                        archer_can_kill[archer].append([i,j,abs(N-i) + abs(archer-j)])
    
    for archer in archers:
        if archer_can_kill[archer]:
            archer_can_kill[archer].sort(key=lambda x:(x[2], x[1]))
            enemy_i, enemy_j, enemy_d = archer_can_kill[archer][0]
            copied_board[enemy_i][enemy_j] = 0
            kill.add(str(enemy_i)+str(enemy_j))

    return len(kill)

def enemy_move(copied_board):

    new_board = [[0 for j in range(M)] for i in range(N)]

    for i in range(N-1):
        for j in range(M):
            if copied_board[i][j] == 1:
                new_board[i+1][j] = copied_board[i][j]
    
    return new_board

def enemy_check(copied_board):
    
    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 1:
                return False

    return True

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
archer_comb = list(combinations([i for i in range(M)], 3))
answer = 0

for archers in archer_comb:
    kill_cnt = 0
    copied_board = deepcopy(board)
    while not enemy_check(copied_board):
        kill_cnt += kill_enemy(archers)
        copied_board = enemy_move(copied_board)
    answer = max(answer, kill_cnt)

print(answer)