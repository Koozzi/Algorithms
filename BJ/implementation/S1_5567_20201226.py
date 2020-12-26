from collections import deque
import sys

def BFS(relation, N, cnt):
    visit = [False for _ in range(N+1)]
    visit[1] = True
    q = deque([(1, 0)])
    while len(q) > 0:
        current_node = q[0][0]
        current_dept = q[0][1]
        q.popleft()

        if current_dept == 3:
            break

        for next_node in relation[current_node]:
            if visit[next_node] == False:
                q.append((next_node, current_dept + 1))
                visit[next_node] = True
                if current_dept + 1 < 3:
                    cnt += 1

    return cnt

N = int(input())
list_cnt = int(input())

relation = [[] for _ in range(N+1)]

for _ in range(list_cnt):
    A, B = map(int, sys.stdin.readline().strip().split())
    relation[A].append(B)
    relation[B].append(A)

print(BFS(relation, N, 0))