def make_one_month(start, cnt, max_cnt):
    global answer

    if cnt == max_cnt:
        for s in one_month_stack:
            state[s] = '1month'

        price = len(one_month_stack) * month + len(three_month_stack) * month3

        for i in range(1, 13):
            if plan[i] and state[i] == 'empty':
                price += day * plan[i]

        for s in one_month_stack:
            state[s] = 'empty'

        answer = min(answer, price)

        return

    for i in range(start, 13):
        if state[i] == 'empty':
            one_month_stack.append(i)
            make_one_month(i + 1, cnt + 1, max_cnt)
            one_month_stack.pop()
    pass


def make_three_month(start, cnt, max_cnt):
    global state, one_month_stack, three_month_stack

    if cnt == max_cnt:
        one_month_stack = []
        state = ['empty' for _ in range(13)]
        for s in three_month_stack:
            for i in range(3):
                if s + i <= 12:
                    state[s+i] = '3month'
        for mc in range(12 - max_cnt * 3 + 1):
            make_one_month(0, 0, mc)

        return

    for start_month in range(start, 13):
        three_month_stack.append(start_month)
        make_three_month(start_month + 3, cnt + 1, max_cnt)
        three_month_stack.pop()


T = int(input())
for t in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    answer = year
    state = []
    one_month_stack = []
    three_month_stack = []
    for max_cnt in range(5):
        make_three_month(1, 0, max_cnt)

    print("#{} {}".format(t, answer))

"""
1     
10 40 100 300   
0 0 2 9 1 5 0 0 0 0 0 0
"""