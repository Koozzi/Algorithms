'''
시작 21:00
제출 21:17
종료 21:25

N개의 구역을 2개의 선거구로 나눈다.
각 구역은 2개의 선거구 중 하나에 꼭 속해야 한다
선거구에 포함된 구역은 서로 연결이 되어있다.

두 선거구에 포함된 인구의 차이를 최소화하자.
'''

from collections import deque

def check_connected(s, state):

    if not s:
        return False

    visit = [False for _ in range(N+1)]
    visit[s[0]] = True
    q = deque([s[0]])
    
    while q:
        current = q.popleft()    
        for _next in section_relation[current]:
            
            if not visit[_next] and section[_next] == state:
                visit[_next] = True
                q.append(_next)

    for num in s:
        if not visit[num]:
            return False

    return True

def divide(start_idx):
    global answer

    section_one_cnt, section_two_cnt = 0, 0
    section_one, section_two = [], [] # 구역 번호
    for section_num in range(1, N+1):
        if section[section_num]:
            section_one.append(section_num)
            section_one_cnt += poeple[section_num-1]
        else:
            section_two.append(section_num)
            section_two_cnt += poeple[section_num-1]
    
    if check_connected(section_one, True) and check_connected(section_two, False):
        answer = min(answer, abs(section_one_cnt - section_two_cnt))

    for section_num in range(start_idx, N+1):
        section[section_num] = True
        divide(section_num+1)
        section[section_num] = False

N = int(input())
poeple = list(map(int, input().split()))
section_relation = [[] for _ in range(N+1)]
section = [False for _ in range(N+1)]
for section_num in range(1, N+1):
    section_info = list(map(int, input().split()))
    section_relation[section_num] = section_info[1:]

answer = 2e9
divide(1)
if answer == 2e9: print(-1)
else: print(answer)