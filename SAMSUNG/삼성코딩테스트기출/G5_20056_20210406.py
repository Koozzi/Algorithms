'''
시작 18:20 
제출 19:00
종료 17:15
'''

def get_next_direction(l):
    for idx in range(1,len(l)):
        if l[idx-1][2] % 2 != l[idx][2] % 2:
            return [1,3,5,7]
    return [0,2,4,6]

def combine_fireball(new_board):
    for i in range(N):
        for j in range(N):
            if len(new_board[i][j]) > 1:
                
                sum_m, sum_s = 0, 0
                for M,S,D in new_board[i][j]:
                    sum_m += M
                    sum_s += S

                next_m = sum_m // 5
                next_s = sum_s // len(new_board[i][j])
                total_d = get_next_direction(new_board[i][j])

                new_board[i][j] = []
                
                if next_m == 0:
                    continue

                for d in total_d:
                    new_board[i][j].append([next_m, next_s, d])

    return new_board    

def fireball_move():
    new_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for M,S,D in board[i][j]:
                next_i = (i + S * move[D][0]) % N
                next_j = (j + S * move[D][1]) % N
                new_board[next_i][next_j].append([M,S,D])

    return combine_fireball(new_board)

move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    I,J,M,S,D = map(int, input().split())
    board[I-1][J-1].append([M,S,D])

for _ in range(K):
    board = fireball_move()

answer = 0
for i in range(N):
    for j in range(N):
        for fireball in board[i][j]:
            answer += fireball[0]

print(answer)