from collections import deque
move_dir = [[0,1],[0,-1],[1,0],[-1,0]]

def down(puyo):
    for j in range(6):
        new_dq = deque([])
        for i in range(11,-1,-1):
            if puyo[i][j] != '.':
                new_dq.append(puyo[i][j])
        
        for i in range(12-len(new_dq)):
            new_dq.append('.')

        for i in range(11, -1, -1):
            puyo[11-i][j] = new_dq[i]

def pop(visit, puyo, I, J):
    q = deque([(I,J)])
    visit[I][J] = True
    original_color = puyo[I][J]
    puyo[I][J] = '#'
    cnt = 1
    while q:
        current_i = q[0][0]
        current_j = q[0][1]
        q.popleft()
        
        for i in range(4):
            next_i = current_i + move_dir[i][0]
            next_j = current_j + move_dir[i][1]
            
            if next_i < 0 or next_j < 0 or next_i == 12 or next_j == 6:
                continue

            if puyo[next_i][next_j] == original_color and not visit[next_i][next_j]:
                q.append((next_i, next_j))
                visit[next_i][next_j] = True
                puyo[next_i][next_j] = '#'
                cnt += 1
    
    for i in range(12):
        for j in range(6):
            if puyo[i][j] == '#':
                if cnt >= 4: puyo[i][j] = '.'
                else: puyo[i][j] = original_color

    return cnt

if __name__=="__main__":

    puyo = []
    for _ in range(12):
        puyo.append(list(input()))

    answer = 0
    while True:
        visit = [[False for _ in range(6)] for _ in range(12)]

        pop_cnt = 0
        for i in range(12):
            for j in range(6):
                if not visit[i][j] and puyo[i][j] != '.':
                    pop_cnt = max(pop_cnt, pop(visit, puyo, i, j))

        if pop_cnt < 4:
            print(answer)
            break

        answer += 1
        down(puyo)