'''
시작 14:48
제출 15:06
종료
'''

def spring():
    dead_tree = []
    for i in range(N):
        for j in range(N):
            tree_board[i][j].sort()
            for idx, tree_age in enumerate(tree_board[i][j]):
                if food_board[i][j] >= tree_age:
                    food_board[i][j]  -= tree_age
                    tree_board[i][j][idx] += 1
                else:
                    for age in tree_board[i][j][idx:]:
                        dead_tree.append([i,j,age])
                    tree_board[i][j] = tree_board[i][j][:idx]
                    break

    return dead_tree

def summer(dead_tree):
    for I,J,A in dead_tree:
        food_board[I][J] += A//2

def fall():
    for i in range(N):
        for j in range(N):
            for age in tree_board[i][j]:
                if age % 5 == 0:
                    for di, dj in move:
                        next_i = i + di
                        next_j = j + dj
                        if 0 <= next_i < N and 0 <= next_j < N:
                            tree_board[next_i][next_j].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            food_board[i][j] += new_food_board[i][j]

move = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
N, M, K = map(int, input().split())
new_food_board = [list(map(int, input().split())) for _ in range(N)]
food_board = [[ 5 for _ in range(N)] for _ in range(N)]
tree_board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    I,J,A = map(int, input().split())
    tree_board[I-1][J-1].append(A)

for _ in range(K):
    summer(spring())
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree_board[i][j])

print(answer)