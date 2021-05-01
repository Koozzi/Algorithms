from itertools import permutations

N = int(input())
player_hit_info = [list(map(int, input().split())) for i in range(N)]
permute_player = permutations([i for i in range(1,9)])
answer = 0

for player in permute_player:
    player = list(player)
    player = player[:3] + [0] + player[3:]
    score, current_order = 0, 0
    for inning in range(N):
        out_count = 0
        B1, B2, B3 = 0, 0, 0
        while out_count < 3:
            current_player = player[current_order]
            current_order = (current_order + 1) % 9
            hit = player_hit_info[inning][current_player]
            if hit == 0:
                out_count += 1
            elif hit == 1:
                score += B3
                B1, B2, B3 = 1, B1, B2
            elif hit == 2:
                score += B2 + B3
                B1, B2, B3 = 0, 1, B1
            elif hit == 3:
                score += B1 + B2 + B3
                B1, B2, B3 = 0, 0, 1
            elif hit == 4:
                score += 1 + B1 + B2 + B3
                B1, B2, B3 = 0, 0, 0
            
    answer = max(answer, score)
    
print(answer)