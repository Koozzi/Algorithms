from collections import deque

def BFS(city):
    if not city: return False
    visit = [False for j in range(N+1)]
    visit[city[0]] = True
    q = deque([city[0]])
    visit_cnt = 1

    while q:
        current_node = q.popleft()
        for next_node in relation[current_node]:
            if section[next_node] == section[city[0]]:
                if not visit[next_node]:
                    visit[next_node]= True    
                    q.append(next_node)
                    visit_cnt += 1
    
    return True if visit_cnt == len(city) else False

def solve(start_idx):
    global answer

    section_one, section_two = [], []
    section_one_sum, section_two_sum = 0, 0
    for idx, s in enumerate(section[1:], start=1):
        if s:
            section_one.append(idx)
            section_one_sum += people[idx-1]
        else:
            section_two.append(idx)
            section_two_sum += people[idx-1]
    
    if BFS(section_one) and BFS(section_two):
        answer = min(answer, abs(section_one_sum-section_two_sum) )

    for i in range(start_idx, N+1):
        if not section[i]:
            section[i] = True
            solve(i+1)
            section[i] = False

answer = 2e9
N = int(input())
people = list(map(int, input().split()))
relation = [[] for _ in range(N+1)]
for i in range(1, N+1):
    row = list(map(int, input().split()))
    if row[0] == 0: continue
    for num in row[1:]:
        relation[i].append(num)

section = [False for i in range(N+1)]
for i in range(1, N+1):
    section[i] = True
    solve(i+1)
    section[i] = False

if answer == 2e9: print(-1)
else: print(answer)