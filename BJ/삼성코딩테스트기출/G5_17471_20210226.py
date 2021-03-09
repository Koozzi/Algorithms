from itertools import combinations
from collections import deque

def BFS(length, check):
    global N

    cnt = 0
    q = deque([])
    visit = [False for i in range(N+1)]
    
    for num in range(1,N+1):
        if section[num] == check:
            visit[num] = True
            q.append(num)
            cnt += 1
            break

    while q:
        current_num = q.popleft()
        for next_num in relation[current_num]:
            if not visit[next_num] and section[next_num] == check:
                visit[next_num] = True
                q.append(next_num)
                cnt += 1

    if cnt == length: return True
    else: return False

N = int(input())
answer = 2e9
people_cnt = list(map(int ,input().split()))
section = [False for i in range(N+1)]
relation = [[] for i in range(N+1)]

for i in range(1,N+1):
    rel = list(map(int, input().split()))
    relation[i] = rel[1:]

for M in range(1,N//2+2):
    total_comb_list = list(combinations(range(1,N+1), M))
    
    for comb_list in total_comb_list:
        for num in comb_list:
            section[num] = True
        
        if BFS(len(comb_list), True) and BFS(N-len(comb_list), False):
        
            a_section_sum, b_section_sum = 0, 0
            for num in range(1,N+1):
                if section[num]: a_section_sum += people_cnt[num-1]
                else: b_section_sum += people_cnt[num-1]
            answer = min(answer, abs(a_section_sum-b_section_sum))

        for num in comb_list:
            section[num] = False

if answer == 2e9: print(-1)
else: print(answer)

