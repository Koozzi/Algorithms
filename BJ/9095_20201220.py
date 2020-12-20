T = int(input())

answer = [0, 1, 2, 4]
for i in range(4, 11):
    answer.append(answer[i-1] + answer[i-2] + answer[i-3])

for t in range(T):
    num = int(input())
    print(answer[num])