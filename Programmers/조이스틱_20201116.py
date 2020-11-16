'''
#1 0번 째 자리 문자 변경
#2 i번 째 자리로 커서 이동
#3 i번 째 문자 변경
#4 name과 같은지 확인
    4-1 같을 때 -> return answer
    4-2 다를 때 -> go to #2
'''
# 현재 위치의 문자를 바꿔준 후, 다음 번의 최적의 위치를 찾아주는 함수
def next_location(name, new_name, idx):
    least_move = 25
    return_idx = 0

    for i, char in enumerate(new_name):
        # 이미 바꾼 문자 / 시작 위치 / 목표 문자가 'A'인 경우
        if char != 'A' or i == idx or name[i] == 'A': continue
        move_cnt = abs(i - idx)

        if len(new_name) - move_cnt < move_cnt:
            move_cnt = len(new_name) - move_cnt

        if move_cnt < least_move:
            least_move = move_cnt
            return_idx = i

    return return_idx, least_move

def get_change_time(current, dest):
    right_cnt = ord(dest) - ord(current)
    left_cnt = 26 - right_cnt

    if right_cnt < left_cnt: return right_cnt
    else: return left_cnt

def solution(name):
    answer = 0

    new_name = ["A"] * len(name)
    cursor_location = 0

    answer += get_change_time("A", name[cursor_location])
    new_name[cursor_location] = name[cursor_location]
    cursor_location, move_cnt = next_location(name, new_name, cursor_location)
    answer += move_cnt
    
    while True:
        answer += get_change_time("A", name[cursor_location])
        new_name[cursor_location] = name[cursor_location]
        cursor_location, move_cnt = next_location(name, new_name, cursor_location)

        if ''.join(new_name) == name:
            break

        answer += move_cnt

    return answer

print("#1", solution("JEROEN"))
print("#2", solution("JAN"))

