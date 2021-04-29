cow = {}
N = int(input())
answer = 0
for _ in range(N):
    cow_number, new_location = map(int,input().split())

    if cow_number in cow:
        current_location = cow[cow_number]
        if new_location != current_location:
            cow[cow_number] = new_location
            answer += 1  
    
    elif cow_number not in cow:
        cow[cow_number] = new_location

print(answer)