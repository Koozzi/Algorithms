T = int(input())
for t in range(1, T+1):

    move = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]
    N = int(input())
    atom_info = []

    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atom_info.append([x, y, d, k, True])

    atom_conflict = 0
    for _ in range(4000):

        if not atom_info:
            break

        index_dictionary = {}
        for idx, atom in enumerate(atom_info):
            x, y, d, k, live = atom

            if not live:
                continue

            x += move[d][0]
            y += move[d][1]

            if x < -1000 or x > 1000 or y < -1000 or y > 1000:
                continue

            if (x, y) not in index_dictionary:
                index_dictionary[(x, y)] = [[idx, x, y, d, k, live]]
            elif (x, y) in index_dictionary:
                index_dictionary[(x, y)].append([idx, x, y, d, k, live])

        atom_info = []
        for index, value in index_dictionary.items():
            if len(value) > 1:
                for idx, x, y, d, k, live in value:
                    atom_conflict += k

            elif len(value) == 1:
                idx, x, y, d, k, live = value[0]
                atom_info.append([x, y, d, k, live])

    print("#{} {}".format(t, atom_conflict))