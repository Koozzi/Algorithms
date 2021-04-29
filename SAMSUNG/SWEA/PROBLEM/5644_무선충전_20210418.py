T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    a_route = [0] + list(map(int, input().split()))
    b_route = [0] + list(map(int, input().split()))
    move = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
    answer = 0

    charger_info = []
    for _ in range(A):
        y, x, r, a = map(int, input().split())
        charger_info.append([x, y, r, a])

    ai, aj, bi, bj = 1, 1, 10, 10
    for ad, bd in zip(a_route, b_route):
        ai += move[ad][0]
        aj += move[ad][1]
        bi += move[bd][0]
        bj += move[bd][1]

        a_possible, b_possible = [], []
        for charger_num, charger in enumerate(charger_info):
            i, j, charge_range, charge_amount = charger

            a_distance = abs(i - ai) + abs(j - aj)
            if a_distance <= charge_range:
                a_possible.append([charger_num, charge_amount])

            b_distance = abs(i - bi) + abs(j - bj)
            if b_distance <= charge_range:
                b_possible.append([charger_num, charge_amount])

        if a_possible and not b_possible:
            a_possible.sort(key=lambda x: -x[1])
            answer += a_possible[0][1]

        elif not a_possible and b_possible:
            b_possible.sort(key=lambda x: -x[1])
            answer += b_possible[0][1]

        elif a_possible and b_possible:
            max_amount = 0
            for a_num, a_amount in a_possible:
                for b_num, b_amount in b_possible:
                    if a_num == b_num:
                        max_amount = max(max_amount, a_amount)
                    elif a_num != b_num:
                        max_amount = max(max_amount, a_amount + b_amount)
            answer += max_amount

    print("#{} {}".format(t, answer))

"""
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
"""