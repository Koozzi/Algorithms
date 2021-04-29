from collections import deque


def solve(matched_person_stair):

    stair_queue = [{} for _ in range(stair_count)]
    stair_waiting_queue = [deque([]) for _ in range(stair_count)]

    count, time = 0, 0
    while True:
        time += 1

        for i in range(stair_count):
            delete_stair = []
            for pi, d in stair_queue[i].items():
                stair_queue[i][pi] -= 1
                if stair_queue[i][pi] == 0:
                    delete_stair.append(pi)

            for di in delete_stair:
                del stair_queue[i][di]
                count += 1
                if count == person_count:
                    return time

            for _ in range(3 - len(stair_queue[i])):
                if stair_waiting_queue[i]:
                    next_person = stair_waiting_queue[i].popleft()
                    stair_queue[i][next_person] = stair_info[i][2]

        # 이동중인 사람들 계단으로
        for i in range(person_count):
            if matched_person_stair[i][1] > 0:
                matched_person_stair[i][1] -= 1
                if matched_person_stair[i][1] == 0:
                    stair_idx = matched_person_stair[i][0]
                    stair_waiting_queue[stair_idx].append(i)


def make_person_stair_match(cnt):
    global answer

    if cnt == person_count:

        matched_person_stair = []
        for person, stair in zip(person_info, stack):
            person_i, person_j, person_idx = person
            stair_i, stair_j, stair_length, stair_idx = stair
            distance = abs(person_i - stair_i) + abs(person_j - stair_j)
            matched_person_stair.append([stair_idx, distance])

        answer = min(answer, solve(matched_person_stair))
        return

    for stair in stair_info:
        stack.append(stair)
        make_person_stair_match(cnt + 1)
        stack.pop()


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    person_count, stair_count = 0, 0
    person_info, stair_info = [], []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                person_info.append([i, j, person_count])
                person_count += 1
            elif board[i][j] > 1:
                stair_info.append([i, j, board[i][j], stair_count])
                stair_count += 1

    answer = 2e9
    stack = []
    make_person_stair_match(0)

    print("#{} {}".format(t, answer))


"""
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
"""