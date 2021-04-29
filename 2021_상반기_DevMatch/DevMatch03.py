relation = {}
profit = {}

def find_parent(child, my_profit):
    
    current_node = relation[child]
    
    if my_profit < 10:
        profit[current_node] += my_profit
        return
    
    if relation[current_node] == '-':
        parent_profit = int(my_profit * 0.1)
        next_my_profit = my_profit - parent_profit
        profit[current_node] += next_my_profit
        return
    
    parent_profit = int(my_profit * 0.1)
    next_my_profit = my_profit - parent_profit
    
    profit[current_node] += next_my_profit
    find_parent(current_node, parent_profit)
    
    
def solution(enroll, referral, seller, amount):
    answer = []

    for A, B in zip(enroll, referral):
        profit[A] = 0
        relation[A] = B
    
    for s, c in zip(seller, amount):
        
        if relation[s] == '-':
            profit[s] += (int((c * 100) * 0.9))
            continue
        
        parent_profit = int((c * 100) * 0.1)
        my_profit = c * 100 - parent_profit
        profit[s] += my_profit
        find_parent(s, parent_profit)
    
    for final_profit in profit.values():
        answer.append(final_profit)
        
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))