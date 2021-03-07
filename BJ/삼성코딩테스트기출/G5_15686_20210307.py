def chicken_distance(I,J):

    distance = 100
    for idx, chick in enumerate(chicken):
        if not v_chicken[idx]: continue
        distance = min(distance, abs(I-chick[0]) + abs(J-chick[1]))
    
    return distance

def city_chicken_distance():
    global N

    sum_chicken_distance = 0
    for h in home:
        sum_chicken_distance += chicken_distance(h[0], h[1])
                
    return sum_chicken_distance

def solve(cnt, start_i):
    global N, M, chicken_cnt, answer

    if cnt == M:
        answer = min(answer, city_chicken_distance())
        return
    
    for i in range(start_i + 1, chicken_cnt):
        if v_chicken[i]: continue
        v_chicken[i] = True
        solve(cnt+1, i)
        v_chicken[i] = False

N, M = map(int, input().split())
chicken = []; chicken_cnt = 0
home = []; home_cnt = 0
board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(N):
        if row[j] == 2:
            chicken.append([i,j])
            chicken_cnt += 1
        elif row[j] == 1:
            home.append([i,j])

answer = 2e9
v_chicken = [False for j in range(chicken_cnt)]
for i in range(chicken_cnt):
    v_chicken[i] = True
    solve(1, i)
    v_chicken[i] = False

print(answer)