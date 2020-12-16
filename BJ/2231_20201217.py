import sys
A = int(sys.stdin.readline())

for i in range(1, A):
    num_list = list(map(int, str(i)))
    if sum(num_list) + i == A:
        print(i)
        exit()

print(0)