'''
#1 numbers를 내림차순으로 정렬해서 가장 큰 수를 찾는다.
#2 1부터 가장 큰 수까지 소수인지 아닌지 체크한다.
#3 numbers로 permutation돌려서 하나하나씩 확인함
'''

import itertools

def get_prime_info(max_num):
    prime_info = [True] * (max_num + 1)

    prime_info[0] = False
    prime_info[1] = False

    a = int(max_num ** 0.5)

    for i in range(2, a+1):
        if prime_info[i] == False: continue
        for j in range(i*i, max_num+1, i):
            prime_info[j] = False

    return prime_info

def get_check_list(numbers):
    check = []

    for i in range(1, len(numbers) + 1):
        new_list = list(itertools.permutations(numbers, i))
        check.append(new_list)

    return check

def solution(numbers):
    max_num = int(''.join(sorted(list(numbers), reverse=True)))
    is_prime = get_prime_info(max_num)

    check_list = get_check_list(list(numbers))

    answer = 0
    new_check_list = []
    for check in check_list:
        for val in check:
            num = int(''.join(list(val)))
            if num not in new_check_list:
                new_check_list.append(num)
            
    for num in new_check_list:
        if is_prime[num] == True: answer += 1

    return answer

print(solution("17"))
print(solution("011"))


[
    [('0',), ('1',), ('1',)], 
    [('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1')], 
    [('0', '1', '1'), ('0', '1', '1'), ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]
]