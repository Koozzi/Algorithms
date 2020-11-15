def solution(progresses, speeds):
    answer = []
    complete = [[False] * 2 for i in range(len(speeds))]
    deploy_num = 0 
    
    while True:
        for i in range(len(speeds)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    complete[i][0] = True
        deploy_now = 0
        for i in range(deploy_num, len(speeds)):
            if complete[i][0] == True:
                complete[i][1] = True
                deploy_num += 1
                deploy_now += 1
            else:
                break
        if deploy_now != 0:
            answer.append(deploy_now)
            
        if sum(answer) == len(speeds):
            break

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))