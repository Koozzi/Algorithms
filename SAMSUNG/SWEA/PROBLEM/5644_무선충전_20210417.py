def solve(ai, aj, bi, bj):
    global answer

    a_possible = []
    b_possible = []

    for charger_num, charger in enumerate(charger_info):
        I, J, charge_range, power = charger

        a_distance = abs(ai - I) + abs(aj - J)
        b_distance = abs(bi - I) + abs(bj - J)

        if a_distance <= charge_range:
            a_possible.append([charger_num, power])
        if b_distance <= charge_range:
            b_possible.append([charger_num, power])

    # A와 B 중 한 사람만 충전할 수 있는 경우
    # 본인이 선택할 수 있는 충전기 중 충전량이 가장 많은 충전기를 선택한다.
    if not a_possible and b_possible:
        b_possible = sorted(b_possible, key=lambda x: -x[1])
        answer += b_possible[0][1]

    elif a_possible and not b_possible:
        a_possible = sorted(a_possible, key=lambda x: -x[1])
        answer += a_possible[0][1]

    # A와 B 모두 선택할 수 있는 충전기가 있는 경우
    # 겹치는 충전기가 존재할 수 있기 떄문에 2중 for문을 사용해서 최대로 충전할 수 있는 값을 구해준다.
    elif a_possible and b_possible:
        max_charger_amount = 0
        for a, a_power in a_possible:
            for b, b_power in b_possible:
                if a == b: max_charger_amount = max(max_charger_amount, a_power)
                else: max_charger_amount = max(max_charger_amount, a_power + b_power)

        answer += max_charger_amount


T = int(input())
for t in range(1, T + 1):
    answer = 0
    M, A = map(int, input().split())
    move = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

    a_route = list(map(int, input().split()))
    b_route = list(map(int, input().split()))

    charger_info = []
    for _ in range(A):
        J, I, _range, power = map(int, input().split())
        charger_info.append([I, J, _range, power])

    ai, aj, bi, bj = 1, 1, 10, 10
    for ad, bd in zip([0] + a_route, [0] + b_route):
        ai, aj = ai + move[ad][0], aj + move[ad][1]
        bi, bj = bi + move[bd][0], bj + move[bd][1]
        solve(ai, aj, bi, bj)

    print("#{} {}".format(t, answer))