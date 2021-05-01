# 13:48
# 14:31
#

def check(l):

    # 경사로를 놓기 전에 모두 높이가 같은지 Check
    all_same = True
    for i in range(1, N):
        if l[i-1] != l[i]:
            all_same = False
            break

    if all_same:
        return True

    bridge = [False for _ in range(N)]

    # 왼쪽에서 오른쪽으로 탐색
    start_bridge_idx = 0
    for i in range(1, N):
        # 높이 차이가 2이상이면 경사로를 놓을 수 없음
        if l[i] - l[i-1] > 1:
            return False

        if l[i] > l[i-1]:
            # 경사로를 놓을 수 있는 여유가 있음
            if start_bridge_idx <= i - L:
                for bridge_idx in range(i-1, i-1-L, -1):
                    bridge[bridge_idx] = True
                start_bridge_idx = i

            # 경사로를 놓을 수 없는 경우
            else:
                return False

        elif l[i] < l[i-1]:
            start_bridge_idx = i
    
    # 오른쪽에서 왼쪽으로 탐색
    start_bridge_idx = N-1
    for i in range(N-2, -1, -1):
        # 높이 차이가 2이상이면 경사로를 놓을 수 없음
        if l[i] - l[i+1] > 1:
            return False

        if l[i] > l[i+1]:
            if i + L <= start_bridge_idx:
                # 이미 자리에 반대쪽 경사로가 있는 경우를 Check한다.
                for bridge_idx in range(i+1, i+1+L):
                    if bridge[bridge_idx]:
                        return False
                start_bridge_idx = i
            else:
                return False
                
        elif l[i] < l[i+1]:
            start_bridge_idx = i
   
    return True

if __name__=="__main__":
    N, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for l in board:
        if check(l):
            answer += 1

    for j in range(N):
        l = []
        for i in range(N):
            l.append(board[i][j])
        if check(l):
            answer += 1
    
    print(answer)
