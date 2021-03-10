def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
        return tree[node]

def update(node, start, end, index, diff):

    if index < start or index > end:
        return
    
    tree[node] += diff

    if start != end:
        mid = (start+end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)

def get_sum(node, start, end, left, right):

    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return get_sum(node*2, start, mid, left, right) + get_sum(node*2+1, mid+1, end, left, right)

N, M, K = map(int, input().split())
l = []; tree = [0] * 3000000
for _ in range(N):
    l.append(int(input()))

init(1, 0, N-1)

for k in range(K+M):
    a, b, c = map(int, input().split())

    if a == 1:      # b번째 수를 c로 변경하라
        b -= 1
        diff = c - l[b]
        l[b] = c
        update(1, 0, N-1, b, diff)
    elif a == 2:    # b번째 수부터 c번째 수까지의 합을 구하라
        print(get_sum(1,0,N-1,b-1,c-1))