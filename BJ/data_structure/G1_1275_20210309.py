from sys import stdin

def init_tree(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(node*2, start, mid) + init_tree(node*2+1, mid+1, end)
    return tree[node]

def query(node, start, end, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)

N, Q = map(int, stdin.readline().split())
l = list(map(int, stdin.readline().split()))
tree = [0] * 400000
init_tree(1,0,N-1)
for q in range(Q):
    x, y, a, b = map(int, stdin.readline().split())
    if x <= y: print(query(1,0,N-1,x-1,y-1))
    else: print(query(1,0,N-1,y-1,x-1))
    diff = b - l[a-1]
    l[a-1] = b
    update(1,0,N-1,a-1,diff)