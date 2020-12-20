def solution(n, times):
    answer = 0
    left, right = 0, min(times) * n

    while left <= right:
        mid = (left + right) // 2
        
        people = 0
        for time in times:
            people += mid // time
            if n <= people:
                break

        if n <= people:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer

print(solution(6, [7,10])) # 28