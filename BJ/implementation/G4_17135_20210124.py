from sys import stdin
from copy import deepcopy
from collections import deque
from itertools import combinations

def attack(archer_i, archer_j, board, N, M, D):
    attack_possible = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                distance = abs(archer_i-i) + abs(archer_j-j)
                if distance <= D:
                    attack_possible.append([i,j,distance])

    attack_possible.sort(key=lambda x : (x[2], x[1]))
    return attack_possible

def enemy_move(N, M, board):
    get_to_castle = 0

    for j in range(M):
        q = deque([])
        
        for i in range(N-1, -1, -1):
            q.append(board[i][j])

        if q[0] == 1:
            get_to_castle += 1

        q.popleft()
        q.append(0)

        for i in range(N-1, -1, -1):
            board[i][j] = q[0]
            q.popleft()

    return board, get_to_castle

def solution(N, M, D, board):
    answer = 0

    enemy_cnt = 0
    for row in board:
        for enemy in row:
            if enemy == 1: 
                enemy_cnt += 1

    l = list(range(0, M))
    archer_location = list(combinations(l, 3))
    '''
    처음에 combination이 아니라 permutation을 사용해서 시간이 엄청 많이 걸렸다.
    왜 permutation을 썼을까. 17135번 문제 pypy3 맞은 사람들 중에서 내가 속도 제일 꼴등이다. ㅎㅎ
    다행히 permutation을 썼을 때, 시간 초과는 나지 않았지만 ^^ ,,, 아무튼 담부턴 이런 실수 하지 말자 ^^
    '''
    for archers in archer_location:
        get_enemy_cnt = 0 # 궁수가 잡은 적의 수
        get_castle_cnt = 0 # 성에 도달한 적의 수

        copy_board = deepcopy(board)

        while True:
            # 궁수가 잡은 적의 수와 성에 도달한 적의 수가 총 적의 수와 같다면 break
            if get_enemy_cnt + get_castle_cnt == enemy_cnt:
                break

            # 궁수(1,2,3)의 공격
            enemy_list = []
            for archer in archers:
                archer_i = N
                archer_j = archer

                possible_attack = attack(archer_i, archer_j, board, N, M, D)

                # 해당 궁수는 공격할 수 있는 적이 없음
                if not possible_attack:
                    continue

                enemy_i, enemy_j = possible_attack[0][0], possible_attack[0][1]
                if [enemy_i, enemy_j] not in enemy_list:
                    enemy_list.append([enemy_i, enemy_j])
                    get_enemy_cnt += 1

            for attacked_enemy in enemy_list:
                I, J = attacked_enemy[0], attacked_enemy[1]
                board[I][J] = 0

            # 적의 이동
            board, c = enemy_move(N, M, board)
            get_castle_cnt += c
            
        board = deepcopy(copy_board)
        answer = max(answer, get_enemy_cnt)

    return answer

if __name__ == "__main__":
    N, M , D = map(int, stdin.readline().split())
    
    board = []
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    print(solution(N, M, D, board))