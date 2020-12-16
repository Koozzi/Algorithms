# 효율성 테스트 1 -> 3.24ms
# 효율성 테스트 2 -> 3.91ms
def solution(phone_book):

    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False


    return True

# 효율성 테스트 1 -> 1.29ms
# 효율성 테스트 2 -> 1.34ms
def solution_hash(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        tmp = ""
        for number in phone_number:
            tmp += number
            if tmp in hash_map and tmp != phone_number:
                return False
    
    return True

def solution_set(phone_book):
    set_phone_book = set(phone_book)
    print(set_phone_book)

solution_set(["119","97674223","1195524421"])

print(solution(["119","97674223","1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"])) 