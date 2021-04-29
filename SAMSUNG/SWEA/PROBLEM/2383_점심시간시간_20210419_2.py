from collections import deque


def solve(person_stair):

    stair_waiting_queue = [deque([]) for _ in range(total_stair_count)]
    stair_queue = [{} for _ in range(total_stair_count)]
    count, time = 0, 0

    while True:

        time += 1

        for stair_idx in range(total_stair_count):

            out_of_stair = []
            for person_idx in stair_queue[stair_idx].keys():
                stair_queue[stair_idx][person_idx] -= 1
                if stair_queue[stair_idx][person_idx] == 0:
                    out_of_stair.append(person_idx)

            for person_idx in out_of_stair:
                del stair_queue[stair_idx][person_idx]
                count += 1
                if count == total_person_count:
                    return time

            for _ in range(3 - len(stair_queue[stair_idx])):
                if stair_waiting_queue[stair_idx]:
                    next_person = stair_waiting_queue[stair_idx].popleft()
                    stair_queue[stair_idx][next_person] = stair_info[stair_idx][2]

        for person_idx in range(total_person_count):
            if person_stair[person_idx][1] > 0:
                person_stair[person_idx][1] -= 1
                if person_stair[person_idx][1] == 0:
                    stair_idx = person_stair[person_idx][0]
                    stair_waiting_queue[stair_idx].append(person_idx)


def make_person_stair_match(cnt):
    global answer

    if cnt == total_person_count:
        person_stair = []
        for person, stair in zip(person_info, stack):
            pi, pj = person
            si, sj, sl, sn = stair
            distance = abs(pi - si) + abs(pj - sj)
            person_stair.append([sn, distance])
        answer = min(answer, solve(person_stair))
        return

    for stair in stair_info:
        stack.append(stair)
        make_person_stair_match(cnt + 1)
        stack.pop()


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    total_person_count, total_stair_count = 0, 0
    person_info, stair_info = [], []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                person_info.append([i, j])
                total_person_count += 1
            elif 1 < board[i][j]:
                stair_info.append([i, j, board[i][j], total_stair_count])
                total_stair_count += 1

    stack = []
    answer = 2e9
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