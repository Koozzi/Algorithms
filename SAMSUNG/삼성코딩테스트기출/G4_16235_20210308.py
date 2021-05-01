def spring_summer():
    global N
    dead_tree = []
    for i in range(N):
        for j in range(N):
            if not tree[i][j]: continue
            tree[i][j].sort()
            dead_flag = False
            dead_start = 0
            for num, age in enumerate(tree[i][j]):
                if food[i][j] < age:
                    dead_flag = True
                    dead_start = num
                    for idx in range(dead_start, len(tree[i][j])):
                        dead_tree.append([i,j,tree[i][j][idx]])
                    break
                else:
                    food[i][j] -= age
                    tree[i][j][num] += 1

            if dead_flag:
                tree[i][j] = tree[i][j][:dead_start]
    
    for d_tree in dead_tree:
        food[d_tree[0]][d_tree[1]] += (d_tree[2] // 2)

def fall():
    global N
    for i in range(N):
        for j in range(N):
            if not tree[i][j]: continue
            for num, age in enumerate(tree[i][j]):
                if age % 5 != 0: continue
                for move in move_dir:
                    next_i, next_j = i + move[0], j + move[1]
                    if not 0 <= next_i < N or not 0 <= next_j < N:
                        continue
                    tree[next_i][next_j].append(1)

def winter():
    global N
    for i in range(N):
        for j in range(N):
            food[i][j] += board[i][j]

move_dir = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
tree = [[[] for j in range(N)] for i in range(N)]
food = [[5 for j in range(N)] for i in range(N)]
for _ in range(M):
    i, j, age = map(int ,input().split())
    tree[i-1][j-1].append(age) 

for k in range(K):
    spring_summer()
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)