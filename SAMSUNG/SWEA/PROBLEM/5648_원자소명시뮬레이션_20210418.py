T = int(input())
for t in range(1, T+1):
    move = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]
    N = int(input())
    answer = 0

    atom_info = []
    for _ in range(N):
        atom_info.append(list(map(int, input().split())))

    while atom_info:
        atom_arrive_location = {}
        for atom_num, atom in enumerate(atom_info):
            x, y, d, amount = atom
            x += move[d][0]
            y += move[d][1]

            if -1000 <= x <= 1000 and -1000 <= y <= 1000:
                if (x, y) in atom_arrive_location:
                    atom_arrive_location[(x, y)].append([x, y, d, amount])
                elif not (x, y) in atom_arrive_location:
                    atom_arrive_location[(x, y)] = [[x, y, d, amount]]

        atom_info = []
        for location, atoms in atom_arrive_location.items():
            if len(atoms) == 1:
                atom_info.append(atoms[0])
            elif len(atoms) > 1:
                for x, y, d, amount in atoms:
                    answer += amount

    print("#{} {}".format(t, answer))

"""
1
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9


1
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9
"""