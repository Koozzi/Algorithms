'''
시작 02:16
제출 02:18
종료
'''

N, M = map(int, input().split())
basket = [0 for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int,input().split())
    for idx in range(A,B+1):
        basket[idx] = C
print(*basket[1:])