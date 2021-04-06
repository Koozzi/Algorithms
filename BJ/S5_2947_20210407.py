'''
시작 00:12
제출 00:16
종료
'''

tree = list(map(int, input().split()))
while tree != [1,2,3,4,5]:
    for i in range(4):
        if tree[i] > tree[i+1]:
            tree[i], tree[i+1] = tree[i+1], tree[i]
            print(*tree)