from sys import stdin
from itertools import permutations

def simulation(N, hitter_order, hitter_info):
    score = 0
    hitter_num = 0 

    for i in range(N): 

        out_count = 0
        b1, b2, b3 = 0, 0, 0
        while out_count < 3:

            hit = hitter_info[i][hitter_order[hitter_num]]
            if hit == 0:
                out_count += 1
            elif hit == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif hit == 2:
                score += (b2+b3)
                b1, b2, b3 = 0, 1, b1
            elif hit == 3:
                score += (b1+b2+b3)
                b1, b2, b3 = 0, 0, 1
            elif hit == 4:
                score += (1+b1+b2+b3)
                b1, b2, b3 = 0, 0, 0
            
            hitter_num = (hitter_num + 1) % 9

    return score

def solution(N, hitter_info):
    
    max_score = 0
    permute_lineup = permutations(range(1,9),8)
    for lineup in permute_lineup:
        lineup = list(lineup[0:3]) + [0] + list(lineup[3:])
        max_score = max(max_score, simulation(N, lineup, hitter_info))

    return max_score

if __name__ == "__main__":
    N = int(stdin.readline())
    hitter_info = [list(map(int, stdin.readline().split())) for _ in range(N)]

    print(solution(N, hitter_info))