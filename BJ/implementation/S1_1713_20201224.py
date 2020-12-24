from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
recommend_list = list(map(int, stdin.readline().rstrip().split()))
recommended_info = []

for time, stu in enumerate(recommend_list):

    # stu 학생이 추천리스트에 등록되어 있으면
    stu_is_recommened = False
    for stud in recommended_info:
        if stud[0] == stu:
            stu_is_recommened = True
            stud[1] += 1
            break

    # stu 학생이 추천리스트에 등록되어 있지 않으면
    if not stu_is_recommened:
        # 추천리스트가 꽉 찼음
        if len(recommended_info) == N:
            # 추천수, 등록 시간 기준으로 정렬
            recommended_info.sort(key=lambda x: (x[1], x[2]))
            recommended_info[0] = [stu, 1, time]
        # 추천리스트가 비어있음
        else:
            recommended_info.append([stu, 1, time])

recommended_info.sort(key=lambda x:x[0])
for ans in recommended_info:
    print(ans[0], end=" ")


'''
3
14
2 1 4 3 5 6 2 7 2 100 100 54 54 50
-> 50 54 100

3
9
2 1 4 3 5 6 2 7 2
-> 2 6 7
'''