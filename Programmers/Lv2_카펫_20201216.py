def solution(brown, yellow):

    half = brown // 2
    height = 2
    width = half - height

    while True:
        if (height - 1) * (width - 1) == yellow:
            return [width+1, height+1]
        height += 1
        width -= 1    

print(solution(10,2)) #[4,3]
print(solution(8,1))  #[3,3]
print(solution(24,24))#[8,6]