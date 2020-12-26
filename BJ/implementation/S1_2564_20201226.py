def get_distance(start, end, N, M):
    start_direction = start[0]
    start_location = start[1]
    end_direction = end[0]
    end_location = end[1]
    
    if start_direction == 1:
        if end_direction == 1:
            return abs(start_location - end_location)

        elif end_direction == 2:
            return N + min(start_location + end_location, M - start_location + M - end_location)

        elif end_direction == 3:
            return start_location + end_location

        else:
            return M - start_location + end_location

    elif start_direction == 2:
        if end_direction == 1:
            return N + min(start_location + end_location, M - start_location + M - end_location)

        elif end_direction == 2:
            return abs(start_location - end_location)

        elif end_direction == 3:
            return start_location + N - end_location

        else:
            return N - start_location + M - end_location

    elif start_direction == 3:
        if end_direction == 1:
            return start_location + end_location

        elif end_direction == 2:
            return N - start_location + end_location

        elif end_direction == 3:
            return abs(start_location - end_location)

        else:
            return M + min(start_location + end_location, N - start_location + N - end_location)
            
    elif start_direction == 4:
        if end_direction == 1:
            return start_location + M - end_location

        elif end_direction == 2:
            return N - start_location + M - end_location

        elif end_direction == 3:
            return M + min(start_location + end_location, N - start_location, N - end_location)

        else:
            return abs(start_location - end_location)

M, N = map(int, input().split())
shop_cnt = int(input())

shop_info = []
for _ in range(shop_cnt):
    shop_info.append(list(map(int, input().split())))
shop_info.insert(0, list(map(int, input().split())))

distance = 0
for idx in range(1, len(shop_info)):
    distance += get_distance(shop_info[0], shop_info[idx], N, M)

print(distance)