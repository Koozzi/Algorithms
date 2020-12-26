from sys import stdin, stdout
from queue import PriorityQueue

q = PriorityQueue()
N = int(input())
size = 0
for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if size == 0:
            return_str = "0\n"
            stdout.write(return_str)
        else:
            return_str = str(q.get()[1]) + "\n"
            stdout.write(return_str)
            size -= 1

    else:
        size += 1
        q.put((abs(num), num))