from collections import deque

def get_expression():
    new_expression = []
    waiting = deque(init_operator)
    flag = False
    for i in range(N):

        if flag:
            flag = False
            continue

        char = init_expression[i]
        new_expression.append(char)
        if char == '+' or char == '-' or char == '*':
            if not waiting: continue
            if i == waiting[0]:
                waiting.popleft()
                new_expression.pop()
                new_expression.pop()
                value = operate(init_expression[i-1:i+2])
                new_expression.append(str(value))
                flag = True

    return new_expression

def operate(expression):

    value, idx = int(expression[0]), 1

    while idx < len(expression):
        next_value = int(expression[idx+1])
        
        if expression[idx] == '+': value += next_value
        elif expression[idx] == '-': value -= next_value
        elif expression[idx] == '*': value *= next_value

        idx += 2
    
    return value

def solve(start_idx):
    global N,answer

    expression = get_expression()
    value = operate(expression)
    answer = max(answer, value)

    for i in range(start_idx, N, 2):
        init_operator.append(i)    
        solve(i+4)
        init_operator.pop()

N = int(input())
init_expression = list(input())
init_operator = []
answer = operate(init_expression)

for i in range(1, N, 2):
    init_operator.append(i)
    solve(i+4)
    init_operator.pop()

print(answer)