S = input()
S += ' '
tmp = ""
result = ""
check = True
# 문자열 뒤집기 
# print(S[::-1])

for char in S:
    if char == ' ':
        if check == False:
            result += char
            continue
        result += tmp[::-1]
        result += ' '
        tmp = ""

    elif char == '<':
        if len(tmp) > 0:
            result += tmp[::-1]
            tmp = ""
        result += '<'
        check = False

    elif char == '>':
        result += '>'
        check = True

    else:
        if check == False:
            result += char
        else:
            tmp += char

print(result)