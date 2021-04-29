from itertools import permutations

T = int(input())
for t in range(1, T+1):
    answer = 2e9
    N = int(input())
    input_list = list(map(int, input().split()))

    start_i, start_j, end_i, end_j = input_list[:4]
    node_info = [[] for _ in range(N+2)]
    for idx in range(0, (N+2)*2, 2):
        a, b = input_list[idx:idx+2]
        node_info[idx//2] = [a, b]

    weight = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for num1 in range(N+2):
        for num2 in range(N+2):
            num1_i, num1_j = node_info[num1]
            num2_i, num2_j = node_info[num2]

            distance = abs(num1_i - num2_i) + abs(num1_j - num2_j)
            weight[num1][num2] = distance
            weight[num2][num1] = distance

    for customer in permutations([i for i in range(2, N+2)], N):
        customer_order = [0] + list(customer) + [1]

        total_distance = 0
        for i in range(1, N+2):
            prev_node = customer_order[i-1]
            curr_node = customer_order[i]

            total_distance += weight[prev_node][curr_node]

        answer = min(answer, total_distance)

    print("#{} {}".format(t, answer))