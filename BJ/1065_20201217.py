# import sys
# A = int(sys.stdin.readline())

A = int(input())
ans = 0
for i in range(1,A+1):
    if i <  100:
        ans += 1
    else:
        new_list = list(map(int, str(i)))
        if new_list[0] - new_list[1] == new_list[1] - new_list[2]:
            ans += 1

print(ans)