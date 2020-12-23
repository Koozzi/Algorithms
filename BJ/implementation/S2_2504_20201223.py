S = input()

if len(S) == 1:
    print(0)
    exit()

stack = []

for item in S:
    if item == '[' or item == '(':
        stack.append(item)

    if len(stack) == 0:
        print(0)
        exit()
    elif item == ']' and stack[-1] == '[':
        stack.pop()

    elif item == ')' and stack[-1] == '(':
        stack.pop()

if len(stack) != 0:
    print(0)
    exit()

# 올바르지 않은 괄호열을 모두 제거 함

def new_stack(s, value, char):
    # 1. ['(','3','(','5','5'], 2, ')' 이 new_stack 함수에 들어옴
    # 2. ['(','20']을 return함

    num = 0
    cnt = 0

    for i in range(len(s)-1, -1, -1):
        cnt += 1
        if s[i] == char:
            for _ in range(cnt):
                s.pop()
            s.append(str(num * value))    
            break

        num += int(s[i])

    return s

for item in S:
    if item == '[' or item == '(':
        stack.append(item)

    elif item == ')':
        if stack[-1] == '(':
            stack.pop()
            stack.append('2')

        else: 
            stack = new_stack(stack, 2, '(')
            # stack top에 정수가 있는 경우 '('이 등장할 때까지의 모든 정수에 대해서 처리
            # 올바르지 않은 괄호열은 모두 처리했기 때문에 stack 리스트 뒤에서부터 탐색하면 '('은 무조건 등장할 것

    elif item == ']':
        if stack[-1] == '[':
            stack.pop()
            stack.append('3')

        else:
            stack = new_stack(stack, 3, '[')
            # stack top에 정수가 있는 경우 '['이 등장할 때까지의 모든 정수에 대해서 처리
            # 올바르지 않은 괄호열은 모두 처리했기 때문에 stack 리스트 뒤에서부터 탐색하면 '['은 무조건 등장할 것

answer = 0
for num in stack:
    answer += int(num)        

print(answer)