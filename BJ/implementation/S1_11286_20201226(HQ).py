from sys import stdin, stdout
import heapq

q = []
N = int(input())
for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if not q:
            return_str = "0\n"
            stdout.write(return_str)
        else:
            return_str = str(heapq.heappop(q)[1]) + "\n"
            stdout.write(return_str)

    else:
        heapq.heappush(q, (abs(num), num))