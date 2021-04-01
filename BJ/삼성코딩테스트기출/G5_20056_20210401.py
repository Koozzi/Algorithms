'''
16:40
17:50

오타 시발 오타 제발 오타 옽아ㅣㅁ눙라ㅓ문ㅇ라ㅣㅜㅁㄴ이;ㅏㅇ른아ㅓ루미ㅏ르ㅟㅁㄴㄷㅅ;밣
'''

def all_even_or_odd(fireball):
    for idx in range(1, len(fireball)):
        if fireball[idx][2]%2 != fireball[idx-1][2]%2:
            return False
    return True

def fireball_combine(new_board):
    for i in range(N):
        for j in range(N):
            if len(new_board[i][j]) > 1:
                total_cnt = len(new_board[i][j])
                new_m, new_s = 0, 0

                for M, S, D in new_board[i][j]:
                    new_m += M
                    new_s += S

                new_m //= 5
                new_s //= total_cnt

                if new_m == 0:
                    new_board[i][j] = []
                    continue

                d_list = []
                if all_even_or_odd(new_board[i][j]):
                    d_list = [0, 2, 4, 6]
                else:
                    d_list = [1, 3, 5, 7]
                
                new_board[i][j] = []
                for new_d in d_list:
                    new_board[i][j].append([new_m, new_s, new_d])

    return new_board

def fireball_move():
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for M, S, D in board[i][j]:
                next_i = (i + S * move[D][0]) % N
                next_j = (j + S * move[D][1]) % N
                new_board[next_i][next_j].append([M, S, D])

    return fireball_combine(new_board)            
                    
move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(1,M+1):
    I, J, M, S, D = map(int, input().split())
    board[I-1][J-1].append([M, S, D])

for _ in range(K):
    board = fireball_move()

answer = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for fireball in board[i][j]:
                answer += fireball[0]

print(answer)