move_dir = [[0,1],[1,0],[0,-1],[-1,0]]
camera_info = [[],
    [[[0,1]], [[1,0]], [[0,-1]], [[-1,0]]],
    [[[0,1],[0,-1]], [[1,0],[-1,0]], [[0,1],[0,-1]], [[1,0],[-1,0]]], 
    [[[0,1],[-1,0]], [[0,1],[1,0]], [[1,0],[0,-1]],[ [-1,0],[0,-1]]],
    [[[0,-1],[-1,0],[0,1]], [[-1,0],[0,1],[1,0]], [[0,1],[1,0],[0,-1]], [[1,0],[-1,0],[0,-1]]],
    [[[0,1],[1,0],[0,-1],[-1,0]], [[0,1],[1,0],[0,-1],[-1,0]], [[0,1],[1,0],[0,-1],[-1,0]], [[0,1],[1,0],[0,-1],[-1,0]]]
]
def watch(I,J,move,watched):
    watched[I][J] = True
    global N, M
    while True:
        I += move[0]
        J += move[1]
        
        if not 0 <= I < N or not 0 <= J < M:
            return watched
        if board[I][J] == 6:
            return watched
        
        watched[I][J] = True
        
def solve(cnt):
    global N, M, answer, camera_cnt
    if cnt == camera_cnt:
        watched = [[False for j in range(M)] for i in range(N)]
        for idx, cam in enumerate(camera):
            for move in camera_info[cam[2]][directions[idx]]:
                watched = watch(cam[0], cam[1], move, watched)
        
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0 and not watched[i][j]:
                    cnt += 1
        
        answer = min(answer, cnt)
        return
    
    for i in range(4):
        directions.append(i)
        solve(cnt+1)
        directions.pop()

N, M = map(int, input().split())

directions = []
camera = []
board = []
blind = 0
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if row[j] != 0 and row[j] != 6:
            camera.append([i,j,row[j]])
        if row[j] == 0:
            blind += 1

camera_cnt = len(camera)

if camera_cnt == 0:
    print(blind)
    exit()

answer = 64
solve(0)

if answer == 64: print(0)
else: print(answer)