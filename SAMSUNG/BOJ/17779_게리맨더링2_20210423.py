"""
기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
다음 칸은 경계선이다.
(x, y), (x+1, y-1), ..., (x+d1, y-d1)
(x, y), (x+1, y+1), ..., (x+d2, y+d2)
(x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
(x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
"""
from collections import deque


def make_section_five(x, y, d1, d2):
    # (x, y), (x + 1, y - 1), ..., (x + d1, y - d1)
    i, j = x, y
    for d in range(d1 + 1):
        section[i+d][j-d] = 5

    # (x, y), (x + 1, y + 1), ..., (x + d2, y + d2)
    i, j = x, y
    for d in range(d2 + 1):
        section[i+d][j+d] = 5

    # (x + d1, y - d1), (x + d1 + 1, y - d1 + 1), ...(x + d1 + d2, y - d1 + d2)
    i, j = x + d1, y - d1
    for d in range(d2 + 1):
        section[i+d][j+d] = 5

    # (x + d2, y + d2), (x + d2 + 1, y + d2 - 1), ..., (x + d2 + d1, y + d2 - d1)
    i, j = x + d2, y + d2
    for d in range(d1 + 1):
        section[i+d][j-d] = 5


def valid_section(num, r, c, x, y, d1, d2):
    if num == 1 and 0 <= r < x+d1 and 0 <= c <= y:
        return True
    elif num == 2 and 0 <= r <= x+d2 and y < c <= N-1:
        return True
    elif num == 3 and x+d1 <= r <= N-1 and 0 <= c < y-d1+d2:
        return True
    elif num == 4 and x+d2 < r <= N-1 and y-d1+d2 <= c <= N-1:
        return True
    return False


def make_section_rest(section_num, x, y, d1, d2):
    start_i, start_j = start_index[section_num]
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_i][start_j] = True
    q = deque([[start_i, start_j]])
    section[start_i][start_j] = section_num
    while q:
        current_i, current_j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = current_i + di
            next_j = current_j + dj
            if 0 <= next_i < N and 0 <= next_j < N:
                if section[next_i][next_j] == 0 and not visit[next_i][next_j]:
                    if valid_section(section_num, next_i, next_j, x, y, d1, d2):
                        visit[next_i][next_j] = True
                        q.append([next_i, next_j])
                        section[next_i][next_j] = section_num


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
start_index = [[], [0, 0], [0, N-1], [N-1, 0], [N-1, N-1]]
answer = 2e9

for x in range(N - 2):
    for y in range(1, N - 1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 <= N - 1 and y + d2 <= N - 1 and y - d1 >= 0:
                    section = [[0 for _ in range(N)] for _ in range(N)]
                    make_section_five(x, y, d1, d2)

                    for section_num in range(1, 5):
                        make_section_rest(section_num, x, y, d1, d2)

                    # print("After making all section")
                    # for s in section:
                    #     print(s)

                    people_count = [0 for _ in range(6)]
                    for i in range(N):
                        for j in range(N):
                            if section[i][j] == 0: section[i][j] = 5
                            people_count[section[i][j]] += board[i][j]

                    min_cnt = min(people_count[1:])
                    max_cnt = max(people_count[1:])

                    answer = min(answer, abs(min_cnt - max_cnt))

print(answer)
