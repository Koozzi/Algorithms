from itertools import combinations


def init_home_chicken(board):
    homes, chickens = [], []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                homes.append([i,j])
            elif board[i][j] == 2:
                chickens.append([i,j])
    return homes, chickens


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
homes, chickens = init_home_chicken(board)
answer = 2e9

for selected_chickens in combinations(chickens, M):

    city_chicken_distance = 0
    for home_i, home_j in homes:
        chicken_distance = 2e9
        for chicken_i, chicken_j in selected_chickens:
            chicken_distance = min(chicken_distance, abs(home_i - chicken_i) + abs(home_j - chicken_j))
        city_chicken_distance += chicken_distance

    answer = min(answer, city_chicken_distance)

print(answer)