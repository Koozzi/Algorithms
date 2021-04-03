l = [['.' for _ in range(15)] for _ in range(5)]
for i in range(5):
    input_string = input()
    for idx, item in enumerate(input_string):
        l[i][idx] = item

result = ''
for j in range(15):
    for i in range(5):
        if l[i][j] == '.': continue
        result += l[i][j]

print(result)