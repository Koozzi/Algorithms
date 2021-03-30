# 21:40
# 22:46
#

def summer(dead_tree):
    for I,J,A in dead_tree:
        food[I][J] += A // 2

def spring():
    dead_tree = []
    for i in range(N):
        for j in range(N):
            tree_board[i][j].sort()
            for idx, tree_age in enumerate(tree_board[i][j]):
                if tree_age <= food[i][j]:
                    food[i][j] -= tree_age
                    tree_board[i][j][idx] += 1
                else:
                    for dead_tree_age in tree_board[i][j][idx:]:
                        dead_tree.append([i,j,dead_tree_age])
                    tree_board[i][j] = tree_board[i][j][:idx]
                    break

    return dead_tree

def fall():
    for i in range(N):
        for j in range(N):
            for tree_age in tree_board[i][j]:
                if tree_age % 5 == 0:
                    for move in move_dir:
                        next_i = i + move[0]
                        next_j = j + move[1]

                        if not 0 <= next_i < N or not 0 <= next_j < N:
                            continue
                        
                        tree_board[next_i][next_j].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            food[i][j] += add_food[i][j]

if __name__=="__main__":

    answer = 0
    N, M, K = map(int, input().split())
    add_food = [list(map(int, input().split())) for _ in range(N)]
    tree_board = [[[] for _ in range(N)] for _ in range(N)]
    food = [[5 for _ in range(N)] for _ in range(N)]
    move_dir = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    for _ in range(M):
        I, J, A = map(int, input().split())   
        tree_board[I-1][J-1].append(A)

    for _ in range(K):
        summer(spring())
        fall()
        winter()

    for i in range(N):
        for j in range(N):
            answer += len(tree_board[i][j])

    print(answer)