from bisect import bisect_left

N = int(input())
num_list = list(map(int, input().split()))
num_list_reverse = list(reversed(num_list))
answer = 0

for i, max_num in enumerate(num_list):

    binary_num = [num_list[0]]
    binary_num_reverse = [num_list[-1]]

    for num in num_list[:i+1]:
        if num > binary_num[-1]:
            binary_num.append(num)
        else:
            idx = bisect_left(binary_num, num)
            binary_num[idx] = num
    
    for num in num_list_reverse[:N-i]:
        if num > binary_num_reverse[-1]:
            binary_num_reverse.append(num)
        else:
            idx = bisect_left(binary_num_reverse, num)
            binary_num_reverse[idx] = num
    
    answer = max(answer, len(binary_num) + len(binary_num_reverse) - 1)

print(answer)