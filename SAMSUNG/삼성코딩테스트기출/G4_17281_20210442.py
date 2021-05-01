'''
16:10
16:29
'''

from itertools import permutations

answer = 0
N = int(input())
player_inning_hit = [list(map(int, input().split())) for _ in range(N)]
permute_player_order = permutations([i for i in range(1,9)], 8)

for p in permute_player_order:
    
    p = list(p)
    player_order = p[:3] + [0] + p[3:]
    score, current_order = 0, 0

    for inning in range(N):
    
        out_count = 0           # 새로운 이닝이 시작되면 아웃 카운트는 0
        B1, B2, B3 = 0, 0, 0    # 새로운 이닐이 시작되면 모든 베이스는 비워져있음

        while out_count < 3:
            
            current_player = player_order[current_order]
            player_hit = player_inning_hit[inning][current_player]

            if player_hit == 0:
                out_count += 1

            elif player_hit == 1:
                score += B3
                B1, B2, B3 = 1, B1, B2

            elif player_hit == 2:
                score += B3 + B2
                B1, B2, B3 = 0, 1, B1

            elif player_hit == 3:
                score += B3 + B2 + B1
                B1, B2, B3 = 0, 0, 1

            elif player_hit == 4:
                score += B3 + B2 + B1 + 1
                B1, B2, B3 = 0, 0, 0

            current_order = (current_order + 1) % 9

    answer = max(answer, score)

print(answer)

        