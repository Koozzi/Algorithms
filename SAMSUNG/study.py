a = [0,1,2,3,4,5,6]

fish_info = [[], [1,2],[13,3], ... ,[1,2]]

print(id(a))
print(id(enumerate(a[1:], start=1)))

for idx, num in enumerate(a[1:], start=1):

    if idx == 6:
        break

    a[2] = -1
    a[3] = -1
    a[4] = -1
    a[5] = -1
    a[6] = -1

    print(idx, num)

print(a)


