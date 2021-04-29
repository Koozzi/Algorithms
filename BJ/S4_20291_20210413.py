from sys import stdin

extender_dic = {}
N = int(stdin.readline())

for _ in range(N):
    filename, extender = input().split('.')
    
    if extender in extender_dic:
        extender_dic[extender] += 1
    elif extender not in extender_dic:
        extender_dic[extender] = 1

for key, value in sorted(extender_dic.items()):
    print(key, value)