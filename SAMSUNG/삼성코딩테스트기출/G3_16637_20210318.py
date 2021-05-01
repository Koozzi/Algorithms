from collections import deque

def operate(expression):
    max_len = len(expression)
    value = int(expression[0])

    idx = 1
    while idx < max_len:
        
        if expression[idx] == '+': value += int(expression[idx+1])
        elif expression[idx] == '-': value -= int(expression[idx+1])
        elif expression[idx] == '*': value *= int(expression[idx+1])

        idx += 2
    
    return value

def operate_bracket():
    new_expression = []
    bracket_deque = deque(bracket)
    prev_operate = False
    for idx, item in enumerate(init_expression):
        if prev_operate:
            prev_operate = False
            continue
        if bracket_deque:
            if idx != bracket_deque[0] and not prev_operate:
                new_expression.append(item)
            else:
                bracket_deque.popleft()
                new_expression.pop()
                A = int(init_expression[idx-1])
                B = int(init_expression[idx+1])
                if item == '+': new_expression.append(str(A+B))
                elif item == '*': new_expression.append(str(A*B))
                elif item == '-': new_expression.append(str(A-B))
                prev_operate = True
        else:
            new_expression.append(item)

    return new_expression

def make_bracket(start_idx):
    global answer
    expression = operate_bracket()
    value = operate(expression)

    answer = max(answer, value)

    for i in range(start_idx, N, 2):
        bracket.append(i)
        make_bracket(i+4)
        bracket.pop()

N = int(input())
init_expression = list(input())
bracket = []
answer = operate(init_expression)
make_bracket(1)

print(answer)