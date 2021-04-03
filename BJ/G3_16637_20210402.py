'''
13:50
14:56
괄호를 칠 때, 조건을 제대로 생각 못함
'''

from copy import deepcopy

def operate(exp):

    value = int(exp[0])
    for idx in range(1, len(exp), 2):
        if exp[idx] == '+': value += int(exp[idx+1])
        elif exp[idx] == '-': value -= int(exp[idx+1])
        elif exp[idx] == '*': value *= int(exp[idx+1])
    
    return value

def make_new_expression(bracket):
    exp = deepcopy(expression)
    for idx in bracket:
        new_num = operate(exp[idx-1:idx+2])
        exp[idx-1] = '.'
        exp[idx] = str(new_num)
        exp[idx+1] = '.'
    
    new_expression = []
    for item in exp:
        if item != '.':
            new_expression.append(item)

    return new_expression

def possibel_bracket(bracket):
    for idx, num in enumerate(bracket[1:], start=1):
        if num - bracket[idx-1] <= 2:
            return False
    return True

def make_bracket(start_idx):
    global answer

    if possibel_bracket(bracket):
        new_expression = make_new_expression(bracket)
        answer = max(answer,  operate(new_expression))

    for idx in range(start_idx, N, 2):
        bracket.append(idx)
        make_bracket(idx+4)
        bracket.pop()

N = int(input())
expression = list(input())
answer = operate(expression)

bracket = []
make_bracket(1)

print(answer)