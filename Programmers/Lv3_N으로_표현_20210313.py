def solution(N, number):
    answer = 0
    if N == number:
        return 1

    s = [set() for i in range(9)]

    for i, x in enumerate(s):
        if i == 0: continue
        s[i].add(int(str(N)*i))

    for i in range(2, 9):
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        
        if number in s[i]:
            answer = i
            break
        else:
            answer = -1

    return answer

print(solution(5, 12))
print(solution(2, 11))