from collections import deque


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    init_password = deque(list(input()))
    password_length = N // 4

    set_of_password = set([])
    for rotate_cnt in range(N):
        init_password.rotate(1)

        for i in range(1, 5):
            new_password = ''
            for j in range(password_length * (i-1), password_length * i):
                new_password += init_password[j]
            set_of_password.add(int(new_password, 16))

    print(set_of_password)

    list_of_password = list(set_of_password)
    list_of_password.sort(reverse=True)

    answer = list_of_password[K-1]

    print("#{} {}".format(t, answer))


"""
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
"""

