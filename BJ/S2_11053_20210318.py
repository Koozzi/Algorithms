from bisect import bisect_left

N = int(input())
num_list = list(map(int, input().split()))
binary_list = [num_list[0]]
for num in num_list[1:]:
    if num > binary_list[-1]:
        binary_list.append(num)
    else:
        idx = bisect_left(binary_list, num)
        binary_list[idx] = num

print(len(binary_list))