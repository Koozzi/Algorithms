from collections import deque

def solution(N, M, pop_num):
    move_count = 0
    num_list = deque([i for i in range(1, N+1)])

    for target_num in pop_num:
        target_num_index = num_list.index(target_num)
        rotate_right = target_num_index
        rotate_left = len(num_list) - target_num_index

        if rotate_right >= rotate_left:
            move_count += rotate_left
            for i in range(rotate_right):
                num_list.append(num_list[0])
                num_list.popleft()
        else:
            move_count += rotate_right
            for i in range(rotate_left):
                num_list.appendleft(num_list[-1])
                num_list.pop()
        
        num_list.popleft()

    return move_count

if __name__ == "__main__":
    N, M = map(int, input().split())
    pop_num = list(map(int, input().split()))

    print(solution(N, M, pop_num))