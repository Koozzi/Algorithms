from collections import deque


def solve():
    global answer

    new_person_info = []
    for _stair, person in zip(person_stair, person_info):
        stair_num, stair = _stair
        stair_i, stair_j, l = stair
        person_i, person_j = person
        distance = abs(stair_i - person_i) + abs(stair_j - person_j)
        new_person_info.append([distance, stair_num])

    stair_waiting_queue = [deque([]) for _ in range(len(stair_info))]
    stair_queue = [{} for _ in range(len(stair_info))]
    person_count = 0
    time = 0

    while True:
        time += 1

        for stair_idx in range(len(stair_info)):
            # 계단에 있는 사람들을 이동시킨다.
            delete_dictionary = []
            for person_idx, left_distance in stair_queue[stair_idx].items():
                stair_queue[stair_idx][person_idx] -= 1
                if stair_queue[stair_idx][person_idx] == 0:
                    delete_dictionary.append(person_idx)

            # 계단 이동을 완료한 사람들
            for idx in delete_dictionary:
                del stair_queue[stair_idx][idx]
                person_count += 1
                if person_count == len(person_info):
                    return time

            # 계단 대기 큐에 있는 사람들을 계단에 넣어준다.
            for _ in range(3 - len(stair_queue[stair_idx])):
                if stair_waiting_queue[stair_idx]:
                    next_person = stair_waiting_queue[stair_idx].popleft()
                    stair_queue[stair_idx][next_person] = stair_info[stair_idx][2]

        # 사람들을 이동시킨다.
        # 남은 거리가 0보다 크면 1 감소한다
        # 남은 거리가 0이면 그 사람이 가는 계단의 대기 큐에 들어간다.
        # 큐에 들어갈 때, 사람의 번호와 대기 큐에서 기다려야 하는 시간을 같이 넣어준다.
        for i in range(len(new_person_info)):
            if new_person_info[i][0] > 0:
                new_person_info[i][0] -= 1
                if new_person_info[i][0] == 0:
                    stair_waiting_queue[new_person_info[i][1]].append(i)


def person_stair_match(cnt):
    global answer

    if cnt == len(person_info):
        answer = min(answer, solve())
        return

    for stair_num, stair in enumerate(stair_info):
        person_stair.append((stair_num, stair))
        person_stair_match(cnt + 1)
        person_stair.pop()


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    person_stair = []
    person_info = []
    stair_info = []

    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                stair_info.append((i, j, board[i][j]))
            elif board[i][j] == 1:
                person_info.append((i, j))

    answer = 2e9
    person_stair_match(0)
    print("#{} {}".format(t, answer))