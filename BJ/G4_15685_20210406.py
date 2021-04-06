'''
시작 00:00
제출 00:56
종료
'''
from copy import deepcopy

def get_next_location(I,J,last_i,last_j):

    sub_i = I - last_i
    sub_j = J - last_j

    next_i = last_i + sub_j
    next_j = last_j - sub_i

    return next_i, next_j

def make_dragon_curve(dragon_curve):

    next_dragon_curve = deepcopy(dragon_curve)
    last_i, last_j = dragon_curve[-1]
    init_length = len(next_dragon_curve)
    for idx in range(init_length-2, -1, -1):
        I, J = next_dragon_curve[idx]
        next_i, next_j = get_next_location(I,J,last_i,last_j)
        next_dragon_curve.append([next_i, next_j])    

    return next_dragon_curve
    
board = [[False for _ in range(101)] for _ in range(101)]
move = [[0,1],[-1,0],[0,-1],[1,0]]
N = int(input())

for _ in range(N):
    J,I,D,S = map(int, input().split())

    dragon_curve = [[I,J],[I+move[D][0], J+move[D][1]]]

    for _ in range(S):
        dragon_curve = make_dragon_curve(dragon_curve)
    
    for dragon_i, dragon_j in dragon_curve:
        board[dragon_i][dragon_j] = True

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            answer += 1

print(answer)