def reduced(str, token_len):
    reduced_string = ""

    idx = 0
    while idx < len(str):
        token = str[idx:idx+token_len]
        ...

    return reduced_string 

def solution(s):
    answer = 1000
    
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, len(reduced(s, i)))

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd")) 