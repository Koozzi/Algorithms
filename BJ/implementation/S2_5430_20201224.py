from sys import stdin, stdout

def solve(funcs, num_list):
    left = True

    if len(num_list) < funcs.count('D'):
        return 'error\n'

    for func in funcs:
        if func == 'R':
            left = not left

        elif func == 'D':
            if left:
                num_list.pop(0)
            else:
                num_list.pop()

    if len(num_list) > 0:
        if left:
            return '['+ ','.join(num_list) +']\n'
        else:
            return '['+ ','.join(reversed(num_list)) +']\n'

    else:
        return '[]\n'

T = int(stdin.readline())
for _ in range(T):
    funcs = stdin.readline().rstrip()
    n = stdin.readline().rstrip()
    num_list = stdin.readline().rstrip()[1:-1].split(',')
    if n == '0': num_list = []

    stdout.write(solve(funcs, num_list))