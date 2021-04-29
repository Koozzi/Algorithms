def spring():
    dead_tree = []

    for i in range(N):
        for j in range(N):
            tree_board[i][j].sort()
            for k in range(len(tree_board[i][j])):
                if food_board[i][j] >= tree_board[i][j][k]:
                    food_board[i][j] -= tree_board[i][j][k]
                    tree_board[i][j][k] += 1
                else:
                    for _k in range(k, len(tree_board[i][j])):
                        dead_tree.append([i, j, tree_board[i][j][_k]])
                    tree_board[i][j] = tree_board[i][j][:k]
                    break

    return dead_tree


def summer(dead_tree):
    for i, j, age in dead_tree:
        food_board[i][j] += age // 2


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


N, M, K = map(int, input().split())
new_food_board = [list(map(int, input().split())) for _ in range(N)]
food_board = [[5 for _ in range(N)] for _ in range(N)]
tree_board = [[[] for _ in range(N)] for _ in range(N)]
move = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

for _ in range(M):
    i, j, age = map(int, input().split())
    tree_board[i-1][j-1].append(age)

for _ in range(K):
    summer(spring())
    fall()
    winter()


answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree_board[i][j])

print(answer)
