from sys import stdin

if __name__=="__main__":
    N = int(stdin.readline())

    ball_info = []
    for i in range(N):
        C, S = map(int, stdin.readline().split())
        ball_info.append([i, C, S])
    ball_info = sorted(ball_info, key=lambda x:(x[2], x[1]))
    
    A = [0 for i in range(200020)] # answer
    C = [0 for i in range(200020)] # color
    S = [0 for i in range(2020)] # size
    size_sum = 0

    for i, ball in enumerate(ball_info):
        idx = ball[0]
        color = ball[1]
        size = ball[2]

        size_sum += size
        C[color] += size
        S[size] += size
        A[idx] = size_sum - C[color] - S[size] + size

        if i != 0 and size == ball_info[i-1][2] and color == ball_info[i-1][1]:
            A[idx] = A[ball_info[i-1][0]]

    for i in range(N):
        print(A[i])
