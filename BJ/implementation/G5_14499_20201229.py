from sys import stdin

def move_dice(dice, direction):

    new_dice = [0,0,0,0,0,0,0]
    if direction == 1:  # 동쪽
        new_dice[0] = 0
        new_dice[3] = dice[1]
        new_dice[2] = dice[2]
        new_dice[6] = dice[3]
        new_dice[1] = dice[4]
        new_dice[5] = dice[5]
        new_dice[4] = dice[6]

    elif direction == 2:  # 서쪽
        new_dice[0] = 0
        new_dice[1] = dice[3]
        new_dice[2] = dice[2]
        new_dice[3] = dice[6]
        new_dice[4] = dice[1]
        new_dice[5] = dice[5]
        new_dice[6] = dice[4]

    elif direction == 3:  # 북쪽
        new_dice[0] = 0
        new_dice[1] = dice[5]
        new_dice[2] = dice[1]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[6]
        new_dice[6] = dice[2]

    else:  # 남쪽
        new_dice[0] = 0
        new_dice[5] = dice[1]
        new_dice[1] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[6] = dice[5]
        new_dice[2] = dice[6]

    return new_dice

def main():
    N, M, I, J, K = map(int, stdin.readline().split())

    board = []

    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    dice = [0,0,0,0,0,0,0]
    
    commands = list(map(int, stdin.readline().split()))
    move_dir = [[],[0,1],[0,-1],[-1,0],[1,0]]

    current_i = I
    current_j = J

    for c in commands:
    
        next_i = current_i + move_dir[c][0]
        next_j = current_j + move_dir[c][1]

        if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
            continue

        current_i = next_i
        current_j = next_j

        dice = move_dice(dice, c)

        if board[next_i][next_j] == 0:
            board[next_i][next_j] = dice[6]
        else:
            dice[6] = board[next_i][next_j]
            board[next_i][next_j] = 0

        print(dice[1])


if __name__ == "__main__":
    main()