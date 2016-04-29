import sys

grid = [[c for c in line] for line in sys.stdin.readlines()]
Q, P = len(grid), len(grid[0])
seq_len = int(sys.argv[1])

paterns_found = 0

# Horizontal sequence
used = [[False]*P for _ in range(Q)]
for x in range(P - seq_len + 1):
    for y in range(Q):
        for x_mod in range(seq_len):
            if grid[y][x + x_mod] != 'x' or used[y][x + x_mod]:
                break
        else:
            for x_mod in range(seq_len):
                used[y][x + x_mod] = True

            paterns_found += 1

# Vertical sequence
used = [[False]*P for _ in range(Q)]
for x in range(P):
    for y in range(Q - seq_len + 1):
        for y_mod in range(seq_len):
            if grid[y + y_mod][x] != 'x' or used[y + y_mod][x]:
                break
        else:
            for y_mod in range(seq_len):
                used[y + y_mod][x] = True

            paterns_found += 1

# Diagonal sequence
used = [[False]*P for _ in range(Q)]
for x in range(P - seq_len + 1):
    for y in range(Q - seq_len + 1):
        for mod in range(seq_len):
            if grid[y + mod][x + mod] != 'x' or used[y + mod][x + mod]:
                break
        else:
            for mod in range(seq_len):
                used[y + mod][x + mod] = True

            paterns_found += 1

# Reverse diagonal sequence
used = [[False]*P for _ in range(Q)]
for x in range(seq_len - 1, P):
    for y in range(Q - seq_len + 1):
        for mod in range(seq_len):
            if grid[y + mod][x - mod] != 'x' or used[y + mod][x - mod]:
                break
        else:
            for mod in range(seq_len):
                used[y + mod][x - mod] = True

            paterns_found += 1

print(paterns_found)
