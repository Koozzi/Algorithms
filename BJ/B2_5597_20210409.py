submit = [False for _ in range(31)]

for _ in range(28):
    N = int(input())
    submit[N] = True

for n in range(1,31):
    if not submit[n]:
        print(n)