'''
시작 14:44
제출 15:22
종료

낚시왕이 오른쪽으로 한 칸 이동한다.
낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
상어를 잡으면 격자판에서 잡은 상어가 사라진다.
상어가 이동한다.

I,J,speed,direction,size
'''

def change_direction(I,J,D):
    if I == N-1: return 1
    elif I == 0: return 0
    elif J == M-1: return 3
    elif J == 0: return 2
    else: return D

def shark_move():
    new_board = [[[0,0,0] for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j]:
                S,D,Z = board[i][j]

                if D <= 2: S %= (N-1)*2
                elif D > 2: S %= (M-1)*2

                I, J = i, j
                for _ in range(S):
                    if D <= 2:
                        if I == N-1: D = 1
                        elif I == 0: D = 2
                    if D > 2:
                        if J == M-1: D = 4
                        elif J == 0: D = 3
                    I += move[D][0]
                    J += move[D][1]
                    
                if new_board[I][J][2] < Z:
                    new_board[I][J] = [S,D,Z]

    return new_board

                
move = [[],[-1,0],[1,0],[0,1],[0,-1]]
N, M, K = map(int, input().split())
board = [[[0,0,0] for _ in range(M)] for _ in range(N)]
shark_info = [[] for _ in range(K)]
for _ in range(K):
    I,J,S,D,Z = map(int, input().split())
    shark_info.append([I,J,True])
    board[I-1][J-1] = [S,D,Z]

answer = 0
for j in range(M):

    # 상어를 잡자
    for i in range(N):
        if board[i][j] != [0,0,0]:
            answer += board[i][j][2]
            board[i][j] = []
            break
    
    # 상어야 움직이자
    board = shark_move()
    
print(answer)