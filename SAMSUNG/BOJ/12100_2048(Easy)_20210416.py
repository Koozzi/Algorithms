from copy import deepcopy


# 리스트에 있는 숫자를 왼쪽으로 합치는 함수임
def combine_number(current_list):
    waiting_for_same_number = True

    _idx, new_list = 0, []
    for idx, number in enumerate(current_list):
        if number != 0:
            new_list.append(number)
            _idx = idx
            break

    for number in current_list[_idx+1:]:
        if number == 0: continue
        if new_list[-1] == number and waiting_for_same_number:
            new_list[-1] += number
            waiting_for_same_number = False
        else:
            new_list.append(number)
            waiting_for_same_number = True

    for _ in range(len(current_list) - len(new_list)):
        new_list.append(0)

    return new_list


def get_answer(current_board):
    global answer

    for i in range(N):
        for j in range(N):
            answer = max(answer, current_board[i][j])


def solve():
    new_board = deepcopy(board)
    for d in direction:
        if d == 0:      # 왼쪽으로
            for i in range(N):
                new_board[i] = combine_number(new_board[i])

        elif d == 1:    # 오른쪽으로
            for i in range(N):
                reversed_list = list(reversed(new_board[i]))
                combined_list = combine_number(reversed_list)
                new_board[i] = list(reversed(combined_list))

        elif d == 2:    # 위쪽으로
            new_board = list(map(list, zip(*new_board)))
            for i in range(N):
                new_board[i] = combine_number(new_board[i])
            new_board = list(map(list, zip(*new_board)))

        elif d == 3:    # 아래쪽으로
            new_board = list(map(list, zip(*new_board)))
            for i in range(N):
                reversed_list = list(reversed(new_board[i]))
                combined_list = combine_number(reversed_list)
                new_board[i] = list(reversed(combined_list))
            new_board = list(map(list, zip(*new_board)))

    get_answer(new_board)


def get_direction(cnt):

    if cnt == 5:
        solve()
        return

    for d in range(4):
        direction.append(d)
        get_direction(cnt+1)
        direction.pop()


answer = 0
direction = []
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
get_direction(0)
print(answer)