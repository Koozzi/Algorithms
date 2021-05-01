from collections import deque

def BFS(group_bfs):
    global N

    cnt = 1
    visit = [False for i in range(N)]
    q = deque([group_bfs[0]])
    visit[group_bfs[0]] = True

    while q:
        current_node = q.popleft()
        for next_node in relation[current_node]:
            if visit[next_node]: continue
            if next_node not in group_bfs: continue
            q.append(next_node)
            visit[next_node] = True
            cnt += 1
    
    if cnt == len(group_bfs): return True
    else: return False

def get_people_sub():
    global N
    sum_one, sum_two = 0, 0
    for i in range(N):
        if group[i]: sum_one += people[i]
        else: sum_two += people[i]
    return abs(sum_one - sum_two)

def solve(start_i):
    global N, answer

    group_one, group_two = [], []
    for i in range(N):
        if group[i]: group_one.append(i)
        else: group_two.append(i)

    if group_one and group_two:
        if BFS(group_one) and BFS(group_two):
            people_sub = get_people_sub()
            answer = min(answer, people_sub)

    for i in range(start_i+1, N):
        if group[i]: continue
        group[i] = True
        solve(i)
        group[i] = False

N = int(input())
people = list(map(int, input().split()))
relation = [[] for i in range(N)]
group = [False for i in range(N)]
answer = 1000

for i in range(N):
    other_people = list(map(int, input().split()))[1:]
    for p in other_people:
        relation[i].append(p-1)
        relation[p-1].append(i)

for i in range(N):
    group[i] = True
    solve(i)
    group[i] = False

if answer == 1000: print(-1)
else: print(answer)