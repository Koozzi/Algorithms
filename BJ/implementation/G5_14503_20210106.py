from sys import stdin

class Robot:
    def __init__(self, i, j, d):
        self.current_i = i
        self.current_j = j
        self.current_d = d

    def change_direction(self):
        if self.current_d == 0: self.current_d = 3
        elif self.current_d == 1: self.current_d = 0
        elif self.current_d == 2: self.current_d = 1
        elif self.current_d == 3: self.current_d = 2


def main(N, M, robot, board):
    clean_count = 1
    rotate_count = 0

    cleaned = [[False for _ in range(M)] for _ in range(N)]
    cleaned[robot.current_i][robot.current_j] = True

    next_location = [[0,-1],[-1,0],[0,1],[1,0]]
    back_location = [[1,0],[0,-1],[-1,0],[0,1]]

    while True:
        next_i = robot.current_i + next_location[robot.current_d][0]
        next_j = robot.current_j + next_location[robot.current_d][1]

        if board[next_i][next_j] == 0 and not cleaned[next_i][next_j]:
            cleaned[next_i][next_j] = True
            robot.change_direction()
            robot.current_i = next_i
            robot.current_j = next_j
            clean_count += 1
            rotate_count = 0
            continue

        robot.change_direction()
        rotate_count += 1

        if rotate_count == 4:
            back_i = robot.current_i + back_location[robot.current_d][0]
            back_j = robot.current_j + back_location[robot.current_d][1]

            if board[back_i][back_j] == 1:
                return clean_count

            robot.current_i = back_i
            robot.current_j = back_j
            rotate_count = 0


if __name__=="__main__":
    N, M = map(int, stdin.readline().split())
    I, J, D = map(int, stdin.readline().split())

    robot = Robot(I, J, D)

    board = []
    for i in range(N):
        row = list(map(int, stdin.readline().split()))
        board.append(row)

    print(main(N, M, robot, board))


'''

3 5
1 2 1
1 1 1 1 1
1 0 0 0 1
1 1 1 1 1

'''