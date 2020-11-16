'''
#1 Stack을 사용해서 큰 수를 만들어주자
#2 https://eda-ai-lab.tistory.com/465?category=766271
'''
def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    
    return ''.join(stack)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("42", 1))