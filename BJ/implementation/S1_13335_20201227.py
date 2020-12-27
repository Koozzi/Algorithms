from collections import deque
from sys import stdin

N, W, L = map(int, stdin.readline().split())
truck_weight = deque(map(int, stdin.readline().split()))
bridge = deque([0 for _ in range(W)])

time, passed = 0,0 

while passed != N:
    time += 1

    # 현재 다리 상황 체크
    if bridge[0] != 0:
        L += bridge[0]
        bridge.popleft()
        bridge.append(0)
        passed += 1
    else:
        bridge.popleft()
        bridge.append(0)

    # 새로운 트럭을 다리로 
    if len(truck_weight) == 0: continue
    if truck_weight[0] <= L:
        bridge[-1] = truck_weight[0]
        L -= truck_weight[0]
        truck_weight.popleft()

print(time)