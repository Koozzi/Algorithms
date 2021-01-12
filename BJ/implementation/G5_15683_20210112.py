from itertools import product

class CCTV:
    def __init__(self, num, i, j):
        self.num = num # CCTV 번호
        self.i = i # CCTV 행
        self.j = j # CCTV 열

    def __str__(self):
        return '({},({},{}))'.format(self.num, self.i, self.j)

def watch_one_direction(direction, i, j, board, check):
    N = len(board)
    M = len(board[0])
    cnt = 0
    direction %= 4
    if direction == 0:
        while True:
            j += 1
            if i < 0 or j < 0 or i >= N or j >= M: break
            if board[i][j] == 6: break
            if board[i][j] == 0 and not check[i][j]:
                cnt += 1
                check[i][j] = True
        
    elif direction == 1:
        while True:
            i += 1
            if i < 0 or j < 0 or i >= N or j >= M: break
            if board[i][j] == 6: break
            if board[i][j] == 0 and not check[i][j]:
                cnt += 1
                check[i][j] = True

    elif direction == 2:
        while True:
            j -= 1
            if i < 0 or j < 0 or i >= N or j >= M: break
            if board[i][j] == 6: break
            if board[i][j] == 0 and not check[i][j]:
                cnt += 1
                check[i][j] = True

    else:
        while True:
            i -= 1
            if i < 0 or j < 0 or i >= N or j >= M: break
            if board[i][j] == 6: break
            if board[i][j] == 0 and not check[i][j]:
                cnt += 1
                check[i][j] = True
    
    return cnt, check


def watch(cctv, board, check):
    cctv_num = cctv[0].num
    current_i = cctv[0].i
    current_j = cctv[0].j
    current_d = cctv[1]

    watch_cnt = 0

    if cctv_num == 1:
        add_cnt, check = watch_one_direction(current_d, current_i, current_j, board, check)
        watch_cnt += add_cnt
    elif cctv_num == 2:
        add_cnt, check = watch_one_direction(current_d, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 2, current_i, current_j, board, check)
        watch_cnt += add_cnt
    elif cctv_num == 3:
        add_cnt, check = watch_one_direction(current_d, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 1, current_i, current_j, board, check)
        watch_cnt += add_cnt
    elif cctv_num == 4:
        add_cnt, check = watch_one_direction(current_d, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 1, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 3, current_i, current_j, board, check)
        watch_cnt += add_cnt
    else:
        add_cnt, check = watch_one_direction(current_d, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 1, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 2, current_i, current_j, board, check)
        watch_cnt += add_cnt
        add_cnt, check = watch_one_direction(current_d + 3, current_i, current_j, board, check)
        watch_cnt += add_cnt

    return watch_cnt, check

def main(N, M, board):

    wall_cnt = 0
    cctv_cnt = 0
    cctv_list = []
     
    for i in range(N):
        for j in range(M):
            if 1 <= board[i][j] <= 5:
                cctv_list.append(CCTV(board[i][j], i, j))
                cctv_cnt += 1

            if board[i][j] == 6:
                wall_cnt += 1

    watch_max = 0
    direciions = list(product([0,1,2,3], repeat=cctv_cnt))

    for direction_list in direciions:
        check = [[False for i in range(M)] for i in range(N)]
        cctv_info = list(zip(cctv_list, direction_list))
        watch_cnt = 0
        for cctv in cctv_info:
            add_cnt, check = watch(cctv, board, check)
            watch_cnt += add_cnt
        watch_max = max(watch_max, watch_cnt)

    return N*M - cctv_cnt - wall_cnt - watch_max
        

if __name__=="__main__":
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    print(main(N, M, board))