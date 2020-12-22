def check_win(board, i, j):
    global visit 

    move_dir = [[1,1],[-1,1],[0,1],[1,0]]

    for move in move_dir:

        length = 1
        next_i, next_j = i, j
        
        while True:
            if length > 5:           
                break

            next_i += move[0]
            next_j += move[1] 
        
            if next_i < 0 or next_j < 0 or next_i >= 19 or next_j >= 19:
                break

            if board[next_i][next_j] != board[i][j]:
                break

            length += 1
        
        prev_i = i - move[0]
        prev_j = j - move[1]            

        if length == 5:
            if prev_i == -1 or prev_j == -1: # 뒷 방향으로는 고려할 필요 X
                return True
            else:
                if board[prev_i][prev_j] != board[i][j]:
                    return True

    visit[i][j] = True
    return False

board = []
import sys
for _ in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for _ in range(19)] for _ in range(19)]

for i in range(19):
    for j in range(19):
        if board[i][j] and visit[i][j] == False:
            if(check_win(board,i,j)):
                print(board[i][j])
                print(i+1, j+1)
                exit()

print(0)