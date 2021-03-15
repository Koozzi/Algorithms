def solution(a):
    answer = 2

    a_len = len(a)
    if a_len < 3:
        return a_len
        
    min_list_from_start = [0] * a_len
    min_list_from_end = [0] * a_len

    min_num = 1000000001
    for i in range(a_len):
        min_num = min(min_num, a[i])
        min_list_from_start[i] = min_num

    min_num = 1000000001
    for i in range(a_len-1, -1, -1):
        min_num = min(min_num, a[i])
        min_list_from_end[i] = min_num
    
    for i in range(1, a_len-1):
        min_left = min_list_from_start[i-1]
        min_right = min_list_from_end[i+1]

        if min_left < a[i] and min_right < a[i]:
            continue
        else:
            answer += 1

    return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))