'''
시작 16:35
제출 17:05
종료 17:05
'''

from sys import stdin
from copy import deepcopy
from itertools import combinations

def enemy_move(copied_board):

    for i in range(N-1,0,-1):
        for j in range(M):
            copied_board[i][j] = copied_board[i-1][j]

    for j in range(M):
        copied_board[0][j] = 0

def is_enemy_left(copied_board):

    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 1:
                return True
    return False

def find_enemy(archer, copied_board):
    
    I, J = N, archer
    possible_enemy = []

    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 1:
                if abs(I-i) + abs(J-j) <= D:
                    possible_enemy.append([abs(I-i) + abs(J-j),j,i])
    
    possible_enemy.sort()

    return possible_enemy

answer = 0
N, M, D = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

permute_archers = combinations([i for i in range(M)], 3)
for archers in permute_archers:

    copied_board = deepcopy(board)
    get_enemy_cnt = 0

    while True:

        # 현재 궁수가 잡을 수 있는 적 위치를 파악한다.
        # 최대로 잡을 수 있는 적은 3마리 뿐
        total_enemy = [] 
        for archer in archers:
            
            possible_enemy = find_enemy(archer, copied_board)
            
            if not possible_enemy:
                # 현재 적은 있으나, 거리가 닿지 않아 죽일 수 있는 적이 없을 때
                continue

            enemy_i, enemy_j = possible_enemy[0][2], possible_enemy[0][1]
            
            if [enemy_i, enemy_j] not in total_enemy:
                total_enemy.append([enemy_i, enemy_j])
        
        # 파악된 적들은 보드에서 삭제한다.
        for enemy_i, enemy_j in total_enemy:
            get_enemy_cnt += 1
            copied_board[enemy_i][enemy_j] = 0

        if not is_enemy_left(copied_board):
            break

        # 전체 적들이 아래로 한 칸씩 내려온다.
        enemy_move(copied_board)

        if not is_enemy_left(copied_board):
            break

    answer = max(answer, get_enemy_cnt)

print(answer)