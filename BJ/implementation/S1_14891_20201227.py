gear = []
for _ in range(4):
    new_gear = list(input())
    gear.append(new_gear)

rotate_cnt = int(input())
for _ in range(rotate_cnt):
    rotate_info = [0,0,0,0]
    gear_num, direction = map(int, input().split())
    gear_num -= 1
    rotate_info[gear_num] = direction

    # 현재 기어 앞쪽으로 확인
    for i in range(gear_num-1, -1, -1):
        if gear[i][2] == gear[i+1][6]: break
        rotate_info[i] = -rotate_info[i+1]

    # 현재 기어 뒤쪽으로 확인
    for i in range(gear_num+1, 4):
        if gear[i][6] == gear[i-1][2]: break
        rotate_info[i] = -rotate_info[i-1]

    # 돌리자
    for idx, rotate in enumerate(rotate_info):
        if rotate == 0: continue
        if rotate == 1:
            gear[idx].insert(0, gear[idx][-1])
            gear[idx].pop()
        elif rotate == -1:
            gear[idx].append(gear[idx][0])
            gear[idx].pop(0)

ans = 0
if gear[0][0] == '1': ans += 1
if gear[1][0] == '1': ans += 2
if gear[2][0] == '1': ans += 4
if gear[3][0] == '1': ans += 8
print(ans)