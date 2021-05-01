'''
시작 14:00
제출 14:20
종료
'''       
def get_new_direction(fireballs):
    
    directions_all_same = True
    for i in range(1, len(fireballs)):
        if fireballs[i-1][2] % 2 != fireballs[i][2] % 2:
            directions_all_same = False
            break
    
    if directions_all_same: return [0,2,4,6]
    else: return [1,3,5,7]

def combine_fireball(new_board):

    for i in range(N):
        for j in range(N):
            if len(new_board[i][j]) > 1:
                len_of_fireball = len(new_board[i][j])
                new_m, new_s = 0, 0
                
                for M,S,D in new_board[i][j]:
                    new_m += M
                    new_s += S
                
                new_m //= 5
                new_s //= len_of_fireball

                d_list = get_new_direction(new_board[i][j])

                new_board[i][j] = []

                if new_m > 0:
                    for new_d in d_list:
                        new_board[i][j].append([new_m,new_s,new_d])

    return new_board

def fireball_move():
    new_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not board[i][j]: continue
            for M,S,D in board[i][j]:
                next_i = (i + S * move[D][0]) % N
                next_j = (j + S * move[D][1]) % N

                new_board[next_i][next_j].append([M,S,D])

    return combine_fireball(new_board)

move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
new_board = []

for _ in range(M):
    I,J,M,S,D = map(int, input().split())
    board[I-1][J-1].append([M,S,D])

for _ in range(K):
    board = fireball_move()

answer = 0
for i in range(N):
    for j in range(N):
        if not board[i][j]: continue
        for M,S,D in board[i][j]:
            answer += M

print(answer)