from sys import stdin

def check(N, L, road):
    
    tmp = 0

    for i in range(1, N):
        # 경사로의 높이가 1보다 큰 경우
        if road[i] > road[i-1] + 1 or road[i] + 1 < road[i-1]:
            return False

        # 상승
        if road[i] == road[i-1] + 1:
            if tmp + L <= i:
                tmp = i
            else:
                return False

        # 하강
        elif road[i] == road[i-1] - 1:
            if i + L - 1 >= N:
                return False
            for j in range(i+1, i+L):
                if road[j] != road[j-1]:
                    return False
            
            tmp = i + L

        elif road[i] == road[i-1]:
            pass

    return True

def solution(N, L, board):
    ans = 0 

    for row in board:
        if check(N, L, row):
            # print(row)
            ans += 1
    
    for j in range(N):
        col = []
        for i in range(N):
            col.append(board[i][j])
        if check(N, L, col):
            # print(col)
            ans += 1

    return ans

if __name__=="__main__":
    N, L = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for i in range(N)]


    # print(check(6, L, [3,3,3,3,3,3]))
    print(solution(N, L, board))