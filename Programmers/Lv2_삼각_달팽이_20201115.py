# 현재 가지고 있는 정보를 통해서 다음 위치를 구하는 함수
def get_next(N, current_i, current_j, new_list, dir):
    if dir == 'down':
        if current_i == N-1 or new_list[current_i+1][current_j] != 0:
            return current_i, current_j+1, 'right'
        return current_i+1, current_j, 'down'

    elif dir == 'right':
        if current_j == N-1 or new_list[current_i][current_j+1] != 0:
            return current_i-1, current_j-1, 'up'
        return current_i, current_j+1, 'right'

    else:
        if new_list[current_i-1][current_j-1] != 0:
            return current_i+1, current_j, 'down'
        return current_i-1, current_j-1, 'up'

def solution(N):
    answer = []
    new_list = [[0] * N for i in range(N)]
    visit = [[False] * N for i in range(N)]

    current_i, current_j, current_d = 0, 0, 'down'
    new_list[0][0] = 1 

    max_num = 0
    for i in range(1, N+1):
        max_num += i
    
    for i in range(2, max_num+1):
        current_i, current_j, current_d = get_next(N, current_i, current_j, new_list, current_d)
        new_list[current_i][current_j] = i   

    for i in range(N):
        for j in range(N):
            if new_list[i][j] != 0:
                answer.append(new_list[i][j])
    print(new_list)

    return answer

print(solution(4))
print(solution(5))
print(solution(6))