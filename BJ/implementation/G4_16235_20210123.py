from sys import stdin

def spring_summer(N, tree_info, board):
    dead_tree = []
    for i in range(N):
        for j in range(N):
            if tree_info[i][j]:
                tree_info[i][j].sort()
                for k in range(len(tree_info[i][j])):
                    if tree_info[i][j][k] <= board[i][j]:
                        board[i][j] -= tree_info[i][j][k]
                        tree_info[i][j][k] += 1
                    else:
                        dead_tree.append([i,j,tree_info[i][j][k]])
                        tree_info[i][j][k] = 0 
            
                for k in range(len(tree_info[i][j]) - 1, -1, -1):
                    if tree_info[i][j][k] == 0:
                        tree_info[i][j].pop()
                    else: break 

    for tree in dead_tree:
        board[tree[0]][tree[1]] += tree[2] // 2

    return board

def fall(N, tree_info):
    move_dir = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
    for i in range(N):
        for j in range(N):
            for tree_age in tree_info[i][j]:
                if tree_age % 5 == 0:
                    for move in move_dir:
                        next_i = i + move[0]
                        next_j = j + move[1]

                        if 0 <= next_i < N and 0 <= next_j < N:
                            tree_info[next_i][next_j].append(1)

    return tree_info

def winter(N, tree_food, board):
    # board에 새로운 양분을 추가한다.
    for i in range(N):
        for j in range(N):
            board[i][j] += tree_food[i][j]

    return board

def solution(N, M, K, tree_food, tree_info, board):

    year = 0 
    while year != K:
        year += 1
        board = spring_summer(N, tree_info, board)
        tree_info = fall(N, tree_info)
        board = winter(N, tree_food, board) 

    tree_cnt = 0
    for i in range(N):
        for j in range(N):
            tree_cnt += len(tree_info[i][j])

    return tree_cnt 

if __name__ == "__main__":
    N, M, K = map(int, stdin.readline().split())
    
    tree_food = []
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        tree_food.append(row)

    tree_info = [[[] for i in range(N)] for i in range(N)]
    for i in range(M):
        I, J, age = map(int, stdin.readline().split())
        tree_info[I-1][J-1].append(age)

    board = [[5 for i in range(N)] for i in range(N)]
 
    print(solution(N, M, K, tree_food, tree_info, board))