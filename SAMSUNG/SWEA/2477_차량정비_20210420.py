from collections import deque


T = int(input())
for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    customer_accepted = [False for _ in range(K + 1)]

    accept_time = [0] + list(map(int, input().split()))
    repair_time = [0] + list(map(int, input().split()))
    arrive_time = [0] + list(map(int, input().split()))
    customer_arrive_time = [[-1, -1]]
    for num, time in enumerate(arrive_time[1:], start=1):
        customer_arrive_time.append([num, time])

    customer_arrive_time.sort(key=lambda x: (x[1], x[0]))
    customer_info = [[0, 0] for _ in range(K + 1)]

    accept_waiting_queue = deque([])
    repair_waiting_queue = deque([])
    accept = [[0, 0] for _ in range(N + 1)]
    repair = [[0, 0] for _ in range(M + 1)]

    count = 0
    # t = 1

    for i in range(K):
        if customer_arrive_time[i][1] == 0:
            customer_accepted[i] = True

            found_empty = False
            for sub_i in range(1, N + 1):
                if accept[sub_i][1] == 0:
                    accept[sub_i] = [i, accept_time[sub_i]]
                    customer_info[i][0] = sub_i
                    found_empty = True
                    break

            if not found_empty:
                accept_waiting_queue.append(i)

    while True:
        # 정비 창구
        for i in range(1, M + 1):
            if repair[i][1] > 0:
                repair[i][1] -= 1
                if repair[i][1] == 0:
                    repair[i][0] = 0
                    count += 1

        if count == K:
            break

        # 정비 대기 큐
        for i in range(1, M + 1):
            if repair[i][1] == 0 and repair_waiting_queue:
                customer_num = repair_waiting_queue.popleft()
                repair[i] = [customer_num, repair_time[i]]
                customer_info[customer_num][1] = i

        # 접수 창구
        for i in range(1, N + 1):
            if accept[i][1] > 0:
                accept[i][1] -= 1
                if accept[i][1] == 0:

                    found_empty = False
                    for sub_i in range(1, M + 1):
                        if repair[sub_i][1] == 0:
                            repair[sub_i] = [accept[i][0], repair_time[sub_i]]
                            customer_info[accept[i][0]][1] = sub_i
                            found_empty = True
                            break

                    if not found_empty:
                        repair_waiting_queue.append(accept[i][0])

                    accept[i][0] = 0

        # 접수 대기 큐
        for i in range(1, N + 1):
            if accept[i][1] == 0 and accept_waiting_queue:
                customer_num = accept_waiting_queue.popleft()
                accept[i] = [customer_num, accept_time[i]]
                customer_info[customer_num][0] = i

        # 정비소를 방문한 손님 처리
        for i in range(1, K + 1):
            if customer_accepted[i]: continue
            customer_arrive_time[i][1] -= 1
            if customer_arrive_time[i][1] <= 0:
                customer_accepted[i] = True

                found_empty = False
                for sub_i in range(1, N + 1):
                    if accept[sub_i][1] == 0:
                        accept[sub_i] = [i, accept_time[sub_i]]
                        customer_info[i][0] = sub_i
                        found_empty = True
                        break

                if not found_empty:
                    accept_waiting_queue.append(i)

    answer = 0
    for i in range(1, K + 1):
        if customer_info[i] == [A, B]:
            answer += i

    if answer == 0:
        answer = -1

    print("#{} {}".format(t, answer))

"""
1
4 1 10 3 1
4 6 4 8
1
0 3 4 4 5 6 9 9 9 10
"""