'''
시작 00:17
제출 00:19
종료 
'''

N, M = map(int, input().split())
backet = [i for i in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    backet[A], backet[B] = backet[B], backet[A]
print(*backet[1:])