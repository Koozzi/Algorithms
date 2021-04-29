from collections import deque


def make_section_five(x, y, d1, d2):
    section = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # (x, y), (x + 1, y - 1), ..., (x + d1, y - d1)
    section[x][y] = 5
    for d in range(1, d1+1):
        section[x+d][y-d] = 5

    # (x, y), (x + 1, y + 1), ..., (x + d2, y + d2)
    section[x][y] = 5
    for d in range(1, d2+1):
        section[x+d][y+d] = 5

    # (x + d1, y - d1), (x + d1 + 1, y - d1 + 1), ...(x + d1 + d2, y - d1 + d2)
    section[x+d1][y-d1] = 5
    for d in range(1, d2+1):
        section[x+d1+d][y-d1+d] = 5

    # (x + d2, y + d2), (x + d2 + 1, y + d2 - 1), ..., (x + d2 + d1, y + d2 - d1)
    section[x+d2][y+d2] = 5
    for d in range(1, d1+1):
        section[x+d2+d][y+d2-d] = 5

    return section


def section_condition(r, c, x, y, d1, d2, section_num):

    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    if section_num == 1:
        if 1 <= r < x+d1 and 1 <= c <= y:
            return True

    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    elif section_num == 2:
        if 1 <= r <= x+d2 and y < c <= N:
            return True

    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    elif section_num == 3:
        if x+d1 <= r <= N and 1 <= c < y-d1+d2:
            return True

    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    elif section_num == 4:
        if x+d2 < r <= N and y-d1+d2 <= c <= N:
            return True

    return False


def get_section_population(start_i, start_j, section, x, y, d1, d2, section_num):
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    section_sum = population[start_i][start_j]

    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 1 <= next_i <= N and 1 <= next_j <= N:
                if not visit[next_i][next_j]:
                    if section[next_i][next_j] != 5:
                        if section_condition(next_i, next_j, x, y, d1, d2, section_num):
                            visit[next_i][next_j] = True
                            q.append([next_i, next_j])
                            section_sum += population[next_i][next_j]

    return section_sum


answer = 2e9
N = int(input())
population = [[]]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    population.append(row)

start_idx = [[], [1, 1], [1, N], [N, 1], [N, N]]
for x in range(1, N-1):
    for y in range(2, N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                # d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
                if x+d1+d2 <= N and 1 <= y-d1 and y+d2 <= N:
                    section = make_section_five(x, y, d1, d2)

                    # get sum of section #1 ~ 4
                    visit = [[False for _ in range(N + 1)] for _ in range(N + 1)]
                    section_population = [0, 0, 0, 0, 0, 0]
                    for section_num, start in enumerate(start_idx[1:], start=1):
                        start_i, start_j = start
                        section_population[section_num] += get_section_population(start_i, start_j, section, x, y, d1, d2, section_num)

                    # get sum of section #5
                    for r in range(1, N+1):
                        for c in range(1, N+1):
                            if not visit[r][c]:
                                section_population[5] += population[r][c]

                    min_population = min(section_population[1:])
                    max_population = max(section_population[1:])
                    answer = min(answer, max_population - min_population)

print(answer)
