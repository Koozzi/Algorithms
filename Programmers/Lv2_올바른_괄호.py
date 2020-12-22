def solution(s):
    answer_list = []
    for item in s:
        if item == '(':
            answer_list.append(item)

        else:
            if len(answer_list) == 0:
                return False
            
            answer_list.pop()

    return len(answer_list) == 0

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))