init_money = int(input())
price = [0] + list(map(int,input().split()))
jh_money, sm_money = 0, 0

# 준현이의 주식 투자
money = init_money
count = 0
for day in range(1, 15):
    if price[day] <= money:
        new_count = money // price[day]
        count += new_count
        money -= price[day] * new_count

jh_money = money + price[14] * count

# 성민이의 주식 투자
money = init_money
count = 0
for day in range(4, 15):
    if price[day-3] > price[day-2] > price[day-1]:
        if price[day] <= money:
            new_count = money // price[day]
            count += new_count
            money -= price[day] * new_count
    elif price[day-3] < price[day-2] < price[day-1]:
        if count > 0:
            money += price[day] * count
            count = 0
sm_money = money + price[14] * count

if jh_money > sm_money: print("BNP")
elif jh_money < sm_money: print("TIMING")
else: print("SAMESAME")