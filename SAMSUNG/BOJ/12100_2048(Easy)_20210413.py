from copy import deepcopy


def combine_number(l):
    new_list = []
    latest_num = l[0]

    for num in l[1:]:
        if num == 0:
            continue

        if latest_num == num:
            new_list.append(latest_num + num)
            latest_num = 0

        else:
            if latest_num == 0:
                latest_num = num
            else:
                new_list.append(latest_num)
                latest_num = num

    new_list.append(latest_num)

    for _ in range(N - len(new_list)):
        new_list.append(0)

    return new_list


def get_directions(cnt):
    global answer
    if cnt == 5:
        new_board = deepcopy(board)

        for d in directions:
            if d == 0:      # 오른쪽으로
                for i in range(N):
                    reversed_list = list(reversed(new_board[i]))
                    new_list = combine_number(reversed_list)
                    new_board[i] = list(reversed(new_list))

            elif d == 1:    # 왼쪽으로
                for i in range(N):
                    new_board[i] = combine_number(new_board[i])

            elif d == 2:    # 아래쪽으로
                for j in range(N):

                    new_list = []
                    for i in range(N-1, -1, -1):
                        new_list.append(new_board[i][j])

                    new_list = combine_number(new_list)

                    for i in range(N-1, -1, -1):
                        new_board[i][j] = new_list[i]

            elif d == 3:    # 위쪽으로

                for j in range(N):

                    new_list = []
                    for i in range(N):
                        new_list.append(new_board[i][j])

                    new_list = combine_number(new_list)

                    for i in range(N):
                        new_board[i][j] = new_list[i]

        for i in range(N):
            for j in range(N):
                answer = max(answer, new_board[i][j])

        return

    for i in range(4):
        directions.append(i)
        get_directions(cnt+1)
        directions.pop()


answer = 0
directions = []
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[0,1], [0,-1], [1,0], [-1,0]]

get_directions(0)

print(answer)