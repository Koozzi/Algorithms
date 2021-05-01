gear = [list(input()) for i in range(4)]
K = int(input())
for k in range(K):
    num, direction = map(int, input().split())
    num -= 1

    gear_rotate = [0,0,0,0]
    gear_rotate[num] = direction
    for i in range(num-1, -1, -1):
        if gear[i][2] == gear[i+1][6]: break    
        gear_rotate[i] = -gear_rotate[i+1]
    
    for i in range(num+1, 4):
        if gear[i][6] == gear[i-1][2]: break
        gear_rotate[i] = -gear_rotate[i-1]

    for num in range(4):
        if gear_rotate[num] == 1:
            gear[num] = gear[num][7:] + gear[num][:7]
        elif gear_rotate[num] == -1:
            gear[num] = gear[num][1:] + gear[num][:1]
    
score = 0
for num in range(4):
    if gear[num][0] == '1':
        score += 2 ** num

print(score)