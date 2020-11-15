# 2020.11.16
from collections import deque
def solution(A, K):
    if len(A) == 0:
        return A
        
    dq = deque(A)
    
    for i in range(K):
        new_item = dq.pop()
        dq.appendleft(new_item)
    
    return list(dq)