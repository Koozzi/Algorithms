def check(l):

    all_same_height = True
    for idx in range(1, N):
        if l[idx] != l[idx-1]:
            all_same_height = False
            break

    if all_same_height:
        return True

    visit = [False for _ in range(N)]
    start_idx = 0
    # 왼쪽에서 오른쪽으로 탐색
    for idx in range(1, N):
        if l[idx] - l[idx-1] > 1:
            return False

        if l[idx] > l[idx-1]:
            if start_idx <= idx - M:
                start_idx = idx
                for i in range(1, M+1):
                    visit[idx-i] = True
            else:
                return False

        elif l[idx] < l[idx-1]:
            start_idx = idx

    # 오른쪽에서 왼쪽으로 탐색
    start_idx = N-1
    for idx in range(N-2, -1, -1):
        if l[idx] - l[idx+1] > 1:
            return False

        if l[idx] > l[idx+1]:
            if start_idx >= idx + M:
                start_idx = idx
                for i in range(1, M+1):
                    if visit[idx+i]:
                        return False
            else:
                return False

        elif l[idx] < l[idx+1]:
            start_idx = idx

    return True


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for row in board:
    if check(row):
        answer += 1

board = list(map(list, zip(*board)))
for row in board:
    if check(row):
        answer += 1

print(answer)