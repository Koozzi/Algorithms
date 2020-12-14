import bisect

arr = []
ans = []

def solve(cookies, start, max_len, max_cnt):   
    global ans
    if len(ans) == max_cnt:
        return
    if len(arr) == max_len:
        ans.append(arr[:])
        return
     
    for i in range(start+1, len(cookies)):
        if arr[-1] < cookies[i]:
            arr.append(cookies[i])
            solve(cookies, i, max_len, max_cnt)
            arr.pop()

def LIS(cookies):
    if len(cookies) == 0:
        return 0
    length = [1] * len(cookies)
    count = [1] * len(cookies)
    length[0], count[0] = 1, 1
    for i in range(len(cookies)):
        for j in range(i):
            if cookies[j] < cookies[i]:
                if length[j] + 1 == length[i]:
                    count[i] += count[j]
                elif length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
    print(length)
    print(count)

    lis_len = max(length)
    lis_cnt = sum([count[i] for i in range(len(count)) if length[i] == lis_len])
    
    print(lis_len)
    print(lis_cnt)

    return [lis_len, lis_cnt]
    
            
def solution(cookies,k):
    answer = []
            
    max_len, max_cnt = LIS(cookies)
    
    for i in range(len(cookies) - max_len + 1):
        arr.append(cookies[i])
        solve(cookies, i, max_len, max_cnt)
        arr.pop()
    
    ans.sort()
    
    return ans[k-1]

print(solution([1,9,7,4,2,6,3,11,10], 1))

'''
테스트 1 〉	통과 (0.11ms, 10.3MB)
테스트 2 〉	통과 (12.45ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (44.61ms, 10.2MB)
테스트 5 〉	통과 (0.25ms, 10.3MB)
테스트 6 〉	통과 (0.22ms, 10.3MB)
테스트 7 〉	통과 (3.42ms, 10.3MB)
테스트 8 〉	통과 (1.76ms, 10.2MB)
테스트 9 〉	통과 (2.99ms, 10.2MB)
테스트 10 〉 통과 (0.05ms, 10.3MB)
테스트 11 〉 통과 (0.27ms, 10.4MB)
테스트 12 〉 통과 (0.01ms, 10.2MB)
'''