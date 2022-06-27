BINARY_LENGHT = 3
NODES = ([0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
         [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1])

def get_strings(arrange, already_seen):
    if len(arrange) == 2**BINARY_LENGHT and 2*arrange.count(0) == 2**BINARY_LENGHT:
        print(f"{''.join(map(str, arrange))}")

    for bit in (0, 1):
        new_seen = already_seen[:]
        new_arrange = arrange + [bit]

        string = ''.join(map(str, new_arrange[-BINARY_LENGHT:]))
        seen = int(string, 2)

        if not new_seen[seen]:
            new_seen[seen] = 1
            get_strings(new_arrange, new_seen)


if __name__ == '__main__':
    already_seen = []
    for _ in range(2**BINARY_LENGHT):
        already_seen.append(0)

    for node in NODES:
        get_strings(node, already_seen)
