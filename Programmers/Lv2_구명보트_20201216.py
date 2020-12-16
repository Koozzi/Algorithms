def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1

    people.sort()

    while True:
        if left == right:
            answer += 1
            break
        if left > right:
            break

        answer += 1
        if people[left] + people[right] > limit:
            right -= 1
        else:
            right -= 1
            left += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))