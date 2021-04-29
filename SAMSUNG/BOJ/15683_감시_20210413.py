cctv_watch_info = [
    [],
    [[[0,1]],[[1,0]],[[0,-1]],[[-1,0]]],
    [[[0,1],[0,-1]],[[1,0],[-1,0]],[[0,1],[0,-1]],[[1,0],[-1,0]]],
    [[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]],[[-1,0],[0,1]]],
    [[[0,-1],[1,0],[-1,0]],[[0,1],[1,0],[-1,0]],[[0,1],[0,-1],[-1,0]],[[0,1],[0,-1],[1,0]]],
    [[[0,1],[0,-1],[1,0],[-1,0]],[[0,1],[0,-1],[1,0],[-1,0]],[[0,1],[0,-1],[1,0],[-1,0]],[[0,1],[0,-1],[1,0],[-1,0]]],
]


def solve():
    s = set([])
    for cctv, d in zip(cctv_info, directions):
        cctv_num, i, j = cctv
        for di, dj in cctv_watch_info[cctv_num][d]:
            next_i, next_j = i, j
            while True:
                next_i += di
                next_j += dj
                if not 0 <= next_i < N or not 0 <= next_j < M:
                    break
                if board[next_i][next_j] == 6:
                    break
                if board[next_i][next_j] == 0:
                    s.add(''.join([str(next_i), str(next_j)]))

    return len(s)


def get_directions(cnt):
    global answer

    if cnt == len(cctv_info):
        watched_count = solve()
        answer = min(answer, safe_area-watched_count)
        return

    for i in range(4):
        directions.append(i)
        get_directions(cnt + 1)
        directions.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = []
cctv_info = []
safe_area, answer = 0, 2e9

for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv_info.append([board[i][j], i, j])
        elif board[i][j] == 0:
            safe_area += 1

get_directions(0)
print(answer)