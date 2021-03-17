from itertools import permutations

N = int(input())
hit_info = [ list(map(int, input().split())) for i in range(N) ]
players = (permutations([i for i in range(9)], 9))
answer = 0

for player in players:
    if player[3] != 0: continue
    current_order, score = 0, 0
    for inning in range(N):
        out_count = 0
        B1, B2, B3 = 0, 0, 0
        while out_count < 3:
            current_player = player[current_order]
            current_order = (current_order + 1) % 9
        
            hit = hit_info[inning][current_player]

            if hit == 0:
                out_count += 1
            elif hit == 1:
                score += B3
                B1, B2, B3 = 1, B1, B2
            elif hit == 2:
                score += B3 + B2
                B1, B2, B3 = 0, 1, B1
            elif hit == 3:
                score += B3 + B2 + B1
                B1, B2, B3 = 0, 0, 1
            elif hit == 4:
                score += B3 + B2 + B1 + 1
                B1, B2, B3 = 0, 0, 0
    
    answer = max(answer, score)

print(answer)

