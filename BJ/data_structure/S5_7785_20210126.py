from sys import stdin

if __name__ == "__main__":
    N = int(stdin.readline())

    log = {}
    for i in range(N):
        name, act = stdin.readline().split()
        if act == 'enter':
            log[name] = act
        else:
            del log[name]

    print("\n".join(sorted(log.keys(), reverse=True)))