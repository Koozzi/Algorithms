from itertools import combinations

def solution(N, M, board):
    chicken_location = []
    home_location = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                home_location.append([i,j])
            elif board[i][j] == 2:
                chicken_location.append([i,j])

    chicken_selected = list(combinations(chicken_location, M))
    
    city_distance = 2e9
    for chicken_comb in chicken_selected:
        sum_of_chicken_distance = 0
        for home in  home_location:
            chicken_distance = 2e9    
            for chicken in chicken_comb:
                chicken_distance = min(chicken_distance, abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
            sum_of_chicken_distance += chicken_distance
        city_distance = min(city_distance, sum_of_chicken_distance)

    return city_distance


if __name__=="__main__":
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    print(solution(N, M, board))