from sys import stdin

def go_down(ladder_info, H, N):

    for j in range(1, N):
        current_i = 0
        current_j = j

        while current_i < H:
            current_i += 1
            if ladder_info[current_i][current_j] == 'R':
                current_j += 1
            elif ladder_info[current_i][current_j] == 'L':
                current_j -= 1

        if current_j != j: return False

    return True


def make_new_ladder(start_i, start_j, N, H, num, cnt, ladder_info):

    if cnt == num:
        if go_down(ladder_info, H, N):
            print(num)
            exit()
        return 
        
    for i in range(start_i, H+1):
        for j in range(1, N):
            if i == start_i and 2 < j <= start_j + 1: continue
            if ladder_info[i][j] != 'X' or ladder_info[i][j+1] != 'X': continue
            ladder_info[i][j], ladder_info[i][j+1] = 'R', 'L'
            make_new_ladder(i, j, N, H, num, cnt + 1, ladder_info)
            ladder_info[i][j], ladder_info[i][j+1] = 'X', 'X'


def solution(N, H, ladder_info):

    for i in range(1, 4):
        make_new_ladder(1, 1, N, H, i, 0, ladder_info)

    return -1


if __name__=="__main__":

    N, M, H = map(int, stdin.readline().split())
    ladder_info = [['X' for i in range(N+1)] for i in range(H+1)]

    for i in range(M):
        a, b = map(int, stdin.readline().split())
        ladder_info[a][b], ladder_info[a][b+1] = 'R', 'L'

    if go_down(ladder_info, H, N): print(0)
    else: print(solution(N, H, ladder_info))