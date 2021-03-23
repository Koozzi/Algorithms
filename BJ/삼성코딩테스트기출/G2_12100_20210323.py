# 12:30
from copy import deepcopy

def integrate_number(l):
    idx = 0
    new_list = []
    while True:
        if idx > N-1:                   # while 문아서 idx를 더해주는데,
            break                       # idx가 범위 밖을 나간 경우 고려 ㄴㄴ 함
        if idx == N-1:
            new_list.append(l[idx])
            break
        if l[idx] == l[idx+1]:
            new_list.append(l[idx]*2)
            idx += 2
        else:
            new_list.append(l[idx])
            idx += 1

    new_list_len = len(new_list)
    for _ in range(N-new_list_len):
        new_list.append(0)

    return new_list

def move_number(l):
    new_list = []
    for num in l:
        if num != 0:
            new_list.append(num)
    for num in l:
        if num == 0:
            new_list.append(num)
    return integrate_number(new_list)

def total_move(move_dir, copied_board):
    for move in move_dir:
        if move == 0:    # 오른쪽으로 붙여
            for i in range(N):
                new_list = list(reversed(copied_board[i]))
                new_list = move_number(new_list)
                copied_board[i] = list(reversed(new_list))

        elif move == 1:  # 왼쪽으로 붙여
            for i in range(N):
                copied_board[i] = move_number(copied_board[i])

        elif move == 2:  # 위쪽으로 붙여
            for j in range(N):
                new_list = []
                for i in range(N):
                    new_list.append(copied_board[i][j])
                new_list = move_number(new_list)
                for i in range(N):
                    copied_board[i][j] = new_list[i]

        elif move == 3:  # 아래쪽으로 붙여
            for j in range(N):
                new_list = []
                for i in range(N):
                    new_list.append(copied_board[i][j])
                new_list = list(reversed(new_list))
                new_list = move_number(new_list)
                new_list = list(reversed(new_list))
                for i in range(N):
                    copied_board[i][j] = new_list[i]    

    return copied_board    

def direction_dfs(cnt,move_dir):
    global answer

    if cnt == 5:
        copied_board = deepcopy(board)
        copied_board = total_move(move_dir, copied_board)

        max_num = 0
        for row in copied_board:
            max_num = max(max_num, max(row))
        answer = max(answer, max_num)

        return

    for i in range(4):
        move_dir.append(i)
        direction_dfs(cnt+1,move_dir)
        move_dir.pop()

def solution():

    move_dir = []
    for i in range(4):
        move_dir.append(i)
        direction_dfs(1,move_dir)
        move_dir.pop()

    return answer

if __name__=="__main__":

    answer = 0
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    print(solution())