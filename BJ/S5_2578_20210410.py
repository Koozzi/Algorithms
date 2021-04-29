def check_by_list(l):
    for c in l:
        if not c: return False
    return True

def bingo():

    count = 0

    for row in check:
        if check_by_list(row):
            count += 1
    
    for j in range(5):
        col = []
        for i in range(5):
            col.append(check[i][j])
        if check_by_list(col):
            count += 1

    I = J = 0
    new_list = []
    while True:
        new_list.append(check[I][J])    
        I += 1 ; J += 1
        if I == 5 or J == 5:
            break
    
    if check_by_list(new_list):
        count += 1

    I, J = 0, 4
    new_list = []
    while True:
        new_list.append(check[I][J])    
        I += 1 ; J -= 1
        if I == 5 or J == -1:
            break    

    if check_by_list(new_list):
        count += 1        

    return count

def check_number(number):

    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                check[i][j] = True
                return

board = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]
check = [[False for _ in range(5)] for _ in range(5)]

answer = 0
for i in range(5):
    for j in range(5):
        answer += 1
        check_number(numbers[i][j])
        bingo_cnt = bingo()
        if bingo_cnt >= 3:
            print(answer)
            exit()