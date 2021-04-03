'''
시작 23:21
제출 
종료 23:51

A => B
B => C
C => B
A에서 시작했을 때, 그 안에서 Cycle이 생겨 메모리가 터진 것.
'''
from collections import deque

def bfs(start):
    global cnt

    possible = []
    q = deque([start])
    while q:
        c = q.popleft()
        if c in relation:
            for n in relation[c]:
                if n not in possible and n != start:
                    q.append(n)
                    possible.append(n)
                    cnt += 1

    for n in possible:
        answer.append(start+n)

N = int(input())
relation = {}
cnt, answer = 0, []
for _ in range(N):
    l = input()

    if l[0] not in relation:
        relation[l[0]] = []

    if l[0] != l[5]:
        if l[5] not in relation[l[0]]:
            relation[l[0]].append(l[5])

for start in relation.keys():
    bfs(start)

answer.sort()
print(cnt)
for a in answer:
    print(a[0],'=>',a[1])