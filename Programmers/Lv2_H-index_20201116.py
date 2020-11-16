import bisect
def solution(citations):
    answer = 0

    citations.sort()

    # i는 H-index임
    for i in range(citations[-1] + 1):
        # idx는 citations리스트 안에서 i보다 크거나 같은 수들 중 가장 작은 수의 index
        idx = bisect.bisect_left(citations, i)

        if idx+1 <= i and len(citations)-idx >= i:
            if i > answer: answer = i

    return answer

print(solution([3, 0, 6, 1, 5]))