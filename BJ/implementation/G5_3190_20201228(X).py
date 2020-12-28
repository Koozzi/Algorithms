from collections import deque
from sys import stdin

def change_direction(C, D):
    if C == 'D':
        if D == 'E': return 'S'
        elif D == 'S': return 'W'
        elif D == 'W': return 'N'
        elif D == 'N': return 'E'

    elif C == 'L':
        if D == 'E': return 'N'
        elif D == 'N': return 'W'
        elif D == 'W': return 'S'
        elif D == 'S': return 'E'    

N = int(stdin.readline()) + 1
K = int(stdin.readline())

board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    I, J = map(int, stdin.readline().split())
    board[I][J] = 1

command = deque([])
L = int(stdin.readline())
for _ in range(L):
    T, C = stdin.readline().split()
    T = int(T)
    command.append([T,C])

time = 0
direction = 'E'
snake = deque([(1,1)])

while True:

    if command:
        if time == command[0][0]:
            direction = change_direction(command[0][1], direction) 
            command.popleft() 

    time += 1 
    
    head_i = snake[0][0]
    head_j = snake[0][1]
    next_i, next_j = 0, 0 

    if direction == 'E': next_i, next_j = head_i, head_j + 1
    elif direction == 'S': next_i, next_j = head_i + 1, head_j
    elif direction == 'W': next_i, next_j = head_i, head_j - 1
    elif direction == 'N': next_i, next_j = head_i - 1, head_j 

    if next_i < 1 or next_j < 1 or next_i == N or next_j == N:
        print("밖으로 나감")
        break
    if (next_i, next_j) in snake:
        print("[{0}][{1}]에 가려다가 자기 몸에 박음".format(next_i, next_j))
        break 
    
    if board[next_i][next_j] == 1:
        snake.appendleft((next_i, next_j))
        board[next_i][next_j] == 0
    elif board[next_i][next_j] == 0:
        snake.appendleft((next_i, next_j))
        snake.pop() 
        
print(time, snake, direction)

'''
5
0
5
4 D
8 D
12 D
15 D
20 L
-> 20

8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D
-> 21

8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L
-> 27


20
13
6 15
7 18
20 14
14 13
11 9
7 10
3 18
10 10
13 13
13 5
6 9
10 4
4 3
19
17 D
36 D
41 D
54 D
56 L
57 L
63 L
68 L
72 L
73 L
76 D
79 D
82 D
85 D
87 D
93 L
105 D
110 D
114 D
-> 90

10
4
5 6
1 4
4 9
8 4
10
1 D
2 L
3 L
4 D
5 D
6 L
7 L
8 L
9 L
10 L
-> 17

10
4
1 2
1 3
1 4
1 5
4 
8 D
10 D
11 D
13 L
-> 21
'''