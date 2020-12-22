def solve(add, sub, mul, div, cnt, result):
    global max_result, min_result
    if cnt == N - 1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    else:
        if add < operator_list[0]:
            solve(add + 1, sub, mul, div, cnt + 1, result + operand_list[cnt + 1])
        if sub < operator_list[1]:
            solve(add, sub + 1, mul, div, cnt + 1, result - operand_list[cnt + 1])
        if mul < operator_list[2]:
            solve(add, sub, mul + 1, div, cnt + 1, result * operand_list[cnt + 1])
        if div < operator_list[3]:
            if result < 0:
                result = -result
                result //= operand_list[cnt + 1]
                result = -result
                solve(add, sub, mul, div + 1, cnt + 1, result)
            else:
                solve(add, sub, mul, div + 1, cnt + 1, result // operand_list[cnt + 1])


N = int(input())
operand_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

max_result = -2e9
min_result = 2e9

solve(0,0,0,0,0,operand_list[0])

print(max_result)
print(min_result)