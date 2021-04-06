'''
시작 00:21
제출 00:44
종료
'''

move_dic = {
    'R': [0,1],
    'L': [0,-1],
    'B': [1,0],
    'T': [-1,0],
    'RT': [-1,1],
    'LT': [-1,-1],
    'RB': [1,1],
    'LB': [1,-1]
}

K, R, T = input().split()
king_i, king_j = 9-int(K[1]), ord(K[0])-64 
rock_i, rock_j = 9-int(R[1]), ord(R[0])-64 
for _ in range(int(T)):
    C = input()
    di, dj = move_dic[C]
    next_i = king_i + di
    next_j = king_j + dj
    if 1 <= next_i <= 8 and 1 <= next_j <= 8:
        if next_i == rock_i and next_j == rock_j:
            rock_next_i = rock_i + di
            rock_next_j = rock_j + dj 
            if 1 <= rock_next_i <= 8 and 1 <= rock_next_j <= 8:
                king_i, king_j = next_i, next_j
                rock_i, rock_j = rock_next_i, rock_next_j
        else:
            king_i, king_j = next_i, next_j

print(chr(king_j+64) + str(9-king_i))
print(chr(rock_j+64) + str(9-rock_i))