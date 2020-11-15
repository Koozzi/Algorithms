from queue import PriorityQueue
import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for value in scoville:
        heapq.heappush(heap, value)

    while True:
        if heap[0] >= K:
            break

        if len(heap) == 1:
            answer = -1
            break

        answer += 1
        A = heapq.heappop(heap)
        B = heapq.heappop(heap)
        heapq.heappush(heap, A + B * 2)

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
# 2