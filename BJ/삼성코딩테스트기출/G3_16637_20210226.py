from itertools import combinations

def calculate(expression):
    
    result = 0
    num, waiting = '', ''
    start_idx = 0
    for idx, char in enumerate(expression):
        if char != '+' and char != '*' and char != '-':
            num += char     
        else:
            if num == '' and char == '-':
                num += char
                continue
            start_idx = idx+1
            result = int(num)
            waiting = char
            break
    
    num = ''
    for char in expression[start_idx:]:
        if char != '+' and char != '*' and char != '-':
            num += char
        else:
            if num == '' and char == '-':
                num += '-'
                continue
            if waiting == '+': result += int(num)
            elif waiting == '-': result -= int(num)
            elif waiting == '*': result *= int(num)
        
            if char == '+': waiting = '+'
            elif char == '-': waiting = '-'
            elif char == '*': waiting = '*'

            num = ''
    
    if waiting == '+': result += int(num)
    elif waiting == '-': result -= int(num)
    elif waiting == '*': result *= int(num) 

    return result

def check_bracket(l):
    for i in range(1,len(l)):
        if l[i] - l[i-1] == 2:
            return False
    return True

def change_expression(expression, comb_candidate):
    new_expression = ''
    tmp = 0
    for operator in comb_candidate:
        sub_expression = expression[operator-1:operator+2]
        new_expression += expression[tmp:operator-1]
        new_expression += str(calculate(sub_expression))
        tmp = operator + 2
    
    last_operator = comb_candidate[-1]
    new_expression += expression[last_operator+2:]
    return new_expression


N = int(input())
expression = input()
if N == 1:
    print(int(expression))
    exit()
if N == 3:
    print(int(calculate(expression)))
    exit()
answer = calculate(expression)
candidate = [i for i in range(1, N, 2)]

for M in range(1,N//2+1):
    total_comb_candidate = list(combinations(candidate, M))
    for comb_candidate in total_comb_candidate:
        if not check_bracket(comb_candidate): continue
        changed_expression = change_expression(expression, comb_candidate)
        answer = max(answer, calculate(changed_expression))

print(answer)