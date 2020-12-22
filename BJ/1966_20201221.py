from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    num_list = deque(list(map(int, input().split())))
    idx_list = deque([])
    for i in range(N): 
        idx_list.append(i)

    answer = 1

    while len(num_list) != 0:
        if num_list[0] == max(num_list):
            num_list.popleft()

            if idx_list[0] == M:
                break

            idx_list.popleft()
            answer += 1
        
        else:
            num_list.append(num_list[0])
            num_list.popleft()

            idx_list.append(idx_list[0])
            idx_list.popleft()

    print(answer)
