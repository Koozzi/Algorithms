go = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 24],
    [7, 7],
    [8, 8],
    [9, 9],
    [10, 10],
    [11, 31],
    [12, 12],
    [13, 13],
    [14, 14],
    [15, 15],
    [16, 29],
    [17, 17],
    [18, 18],
    [19, 19],
    [20, 20],
    [32, 32],
    [20, 20],
    [21, 21],
    [22, 22],
    [25, 25],
    [26, 26],
    [23, 23],
    [23, 23],
    [27, 27],
    [28, 28],
    [23, 23],
    [30, 30],
]
score_list = [-1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,35,30,25,13,16,19,26,27,28,24,22,0]


def get_next_index(current_index, dice):
    _dice = dice
    _idx = current_index
    while _dice:
        if _idx == 32: break
        _idx = go[_idx][int(_dice == dice)]
        _dice -= 1
    return _idx


def solve(cnt):
    global answer

    if cnt == 10:
        horse_location = [0 for _ in range(4)]
        location = [False for _ in range(33)]
        score = 0

        for h, c in zip(stack, command):
            current_location = horse_location[h]

            # 해당 말이 끝자리에 도착해있으면 Continue
            if current_location == 32:
                return

            next_location = get_next_index(current_location, c)

            # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다.
            # 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
            if next_location != 32 and location[next_location]:
                return

            location[current_location] = False          # 현재자리는 빈자리로 만들어주고
            location[next_location] = True              # 다음자리에 자리를 차지한다.
            horse_location[h] = next_location           # 말의 현재 위치를 '다음자리'로 바꿔준다.
            score += score_list[next_location]          # '다음자리'에 해당하는 점수를 더해준다.

        answer = max(answer, score)
        return

    for i in range(4):
        stack.append(i)
        solve(cnt + 1)
        stack.pop()


answer = 0
command = list(map(int, input().split()))
stack = []
solve(0)
print(answer)