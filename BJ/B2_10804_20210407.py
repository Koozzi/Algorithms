'''
시작 00:58
제출 01:07
종료 
'''

card = [i for i in range(1,21)]
for _ in range(10):
    A, B = map(int,input().split())
    sub_card = list(reversed(card[A-1:B]))
    for idx, num in enumerate(sub_card):
        card[idx+A-1] = num
print(*card)