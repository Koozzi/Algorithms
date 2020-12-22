from itertools import permutations

N = int(input())
operand_list = list(map(int, input().split()))
operator = list(map(int, input().split()))

operator_list = []
for idx, num in enumerate(operator):
    for i in range(num):
        operator_list.append(idx)

min_answer = 2e9
max_answer = -2e9

permutes = list(permutations(operator_list, len(operand_list) - 1))

for permute in permutes:
    result = operand_list[0]
    for idx, num in enumerate(permute):
        if num == 0:
            result += operand_list[idx+1]
        elif num == 1:
            result -= operand_list[idx+1]
        elif num == 2:
            result *= operand_list[idx+1]
        else:
            result //= operand_list[idx+1]
    
    max_answer = max(max_answer, result)
    min_answer = min(min_answer, result)

print(max_answer)
print(min_answer)