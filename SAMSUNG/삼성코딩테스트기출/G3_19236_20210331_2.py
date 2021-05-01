from copy import deepcopy

def get_fish_info():
    fish_info = [[] for _ in range(17)]
    board = [[[0,0] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        row = list(map(int, input().split()))
        for j in range(4):
            fish_num = row[j*2]
            fish_dir = row[j*2+1]-1
            board[i][j] = [fish_num, fish_dir]
            fish_info[fish_num] = [i, j, fish_dir, True]
    
    return board, fish_info

def fish_move():
    for fish_num in range(1,17):
        if not fish_info[fish_num][3]:
            continue
        I,J,D = fish_info[fish_num][:3]
        for _ in range(8):
            next_i = I + move[D][0]
            next_j = J + move[D][1]
            if not 0 <= next_i < 4 or not 0 <= next_j < 4:
                D = (D + 1) % 8
                continue
            if board[next_i][next_j][0] == -1:
                D = (D + 1) % 8
                continue

            next_fish_num, next_fish_dir = board[next_i][next_j]
            if next_fish_num > 0:
                board[I][J] = [next_fish_num, next_fish_dir]
                fish_info[next_fish_num] = [I, J, next_fish_dir, True]
            elif next_fish_num == 0:
                board[I][J] = [0,0]
            board[next_i][next_j] = [fish_num, D]
            fish_info[fish_num] = [next_i, next_j, D, True]
            break
 
def get_shark_can_eat(I,J,D):
    shark_can_eat = []
    while True:
        I += move[D][0]
        J += move[D][1]
        if not 0 <= I < 4 or not 0 <= J < 4:
            break
        if board[I][J][0] > 0:
            shark_can_eat.append([I,J])
    return shark_can_eat

def solve(fish_sum):
    global shark_i, shark_j, shark_d, answer, board, fish_info

    fish_move()
    shark_can_eat = get_shark_can_eat(shark_i, shark_j, shark_d)
    if not shark_can_eat:
        answer = max(answer, fish_sum)
    
    for I, J in shark_can_eat:
        copied_shark_i, copied_shark_j, copied_shark_d = shark_i, shark_j, shark_d
        copied_board, copied_fish_info = deepcopy(board), deepcopy(fish_info)

        '''
        재귀 함수에 들어가기 전에 board랑 fish_info를 조금 수정했으니,
        재귀 함수 밖으로 나오면 수정한 부분만 다시 원상복귀를 시키면 된다고 생각했으나
        재귀 함수 안에 들어갔을 때, 재귀 함수에 들어가기 전에 수정한 부분에 플러스로
        다른 부분들도 바꼈을 가능성이 크기 때문에 깔끔하게 deepcopy를 써서 원상복귀한다. 
        '''

        fish_num, fish_dir = board[I][J]
        board[shark_i][shark_j] = [0,0]
        fish_info[fish_num][3] = False
        board[I][J] = [-1, fish_dir]
        shark_i, shark_j, shark_d = I, J, fish_dir

        solve(fish_sum + fish_num)

        shark_i, shark_j, shark_d = copied_shark_i, copied_shark_j, copied_shark_d
        board, fish_info = copied_board, copied_fish_info

if __name__=="__main__":
    move = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    board, fish_info = get_fish_info()

    first_fish, first_dir = board[0][0]
    shark_i, shark_j, shark_d = 0, 0, first_dir
    fish_info[first_fish][3] = False
    board[0][0] = [-1, first_dir]
    answer = 0

    solve(first_fish)

    print(answer)