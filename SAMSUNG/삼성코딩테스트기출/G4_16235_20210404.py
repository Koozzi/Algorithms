'''
시작 12:42
제출 13:08
종료 13:14

r과 c는 1부터 시작한다.
가장 처음에 양분은 모든 칸에 5만큼 들어있다.

o 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
o 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
x 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
소수점 아래는 버린다.

가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수
인접한 8개의 칸에 나이가 1인 나무가 생긴다.
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
'''

from sys import stdin

def spring():
    dead_tree = []
    for i in range(N):
        for j in range(N):
            if tree_board[i][j]:
                tree_board[i][j].sort()
                for idx, tree_age in enumerate(tree_board[i][j]):
                    if tree_age <= food_board[i][j]:
                        food_board[i][j] -= tree_age
                        tree_board[i][j][idx] += 1
                    else:
                        for dead_tree_age in tree_board[i][j][idx:]:
                            dead_tree.append([i,j,dead_tree_age])
                        tree_board[i][j] = tree_board[i][j][:idx]
                        break

    return dead_tree

def summer(dead_tree):
    for i,j,age in dead_tree:
        food_board[i][j] += age // 2
                
def fall():
    for i in range(N):
        for j in range(N):
            if tree_board[i][j]:
                for idx, tree_age in enumerate(tree_board[i][j]):
                    if tree_age % 5 == 0:
                        for di, dj in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                            next_i = i + di
                            next_j = j + dj
                            if 0 <= next_i < N and 0 <= next_j < N:
                                tree_board[next_i][next_j].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            food_board[i][j] += init_board[i][j]


N, M, K = map(int, stdin.readline().split())
init_board = [list(map(int, stdin.readline().split())) for _ in range(N)]
food_board = [[5 for _ in range(N)] for _ in range(N)]
tree_board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    tree_board[A-1][B-1].append(C)

    
for _ in range(K):
    summer(spring())
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree_board[i][j])

print(answer)