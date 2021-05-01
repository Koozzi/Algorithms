# 14:00
# 14:18
# 치킨 집을 최대로 남기는 것이 무조건 치킨 거리를 최소화할 수 있기 때문에
# 기존 치킨 집의 수에서 M개를 고르는 Combination 방법을 쓰면 더 빠를 듯.
# 다시 말해, 치킨집이 1개, 2개, ... M-1개 일 때는 고려할 필요 ㄴㄴ해

def get_chicken_distance(remain_chicken):
    chicken_distance = 0
    for i in range(N):
        for j in range(N):
            distance = 2e9
            if board[i][j] == 1:
                for chicken_i, chicken_j in remain_chicken:
                    distance = min(distance, abs(i-chicken_i) + abs(j-chicken_j))
                chicken_distance += distance
    
    return chicken_distance

def solve(start_idx, cnt, c):
    global answer

    if cnt == c:
        answer = min(answer, get_chicken_distance(remain_chicken))
        return

    for i in range(start_idx, len(chicken)):
        remain_chicken.append(chicken[i])
        solve(i+1, cnt+1, c)
        remain_chicken.pop()

if __name__=="__main__":
    answer = 2e9
    N, M = map(int, input().split())
    board, chicken, remain_chicken = [], [], []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(N):
            if row[j] == 2:
                chicken.append([i,j])
    
    for c in range(1, M+1):
        solve(0, 0, c)

    print(answer)