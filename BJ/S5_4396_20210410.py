N = int(input())

boom = [input() for _ in range(N)]
opened = [input() for _ in range(N)]
answer = [['0' for _ in range(N)] for _ in range(N)]
found_boom = False

for i in range(N):
    for j in range(N):
        if opened[i][j] == 'x':

            if boom[i][j] == '*':
                found_boom = True

            boom_count = 0
            for di, dj in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < N and 0 <= next_j < N:
                    if boom[next_i][next_j] == '*':
                        boom_count += 1

            answer[i][j] = str(boom_count)

        else:
            answer[i][j] = '.'

if found_boom:
    for i in range(N):
        for j in range(N):
            if boom[i][j] == '*':
                answer[i][j] = '*'

for row in answer:
    print(''.join(row))