def eat_cookie(presents, nice_kids_visited):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if the_neighborhood[r][c].isalpha():
            if the_neighborhood[r][c] == "V":
                nice_kids_visited += 1

            the_neighborhood[r][c] = '-'
            presents -= 1

        if not presents:
            break

    return presents, nice_kids_visited

presents_n = int(input())
size_neighborhood = int(input())
the_neighborhood = []
santa_pos = []
all_nice_kids = 0
nice_kids_visited = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size_neighborhood):
    line = input().split()
    the_neighborhood.append(line)

    if "S" in line:
        santa_pos = [row, line.index('S')]
        the_neighborhood[row][santa_pos[1]] = '-'
    all_nice_kids += line.count('V')

command = input()

while True:
    if command == "Christmas morning":
        break

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    house = the_neighborhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents_n -= 1
    elif house == "C":
        presents_n, nice_kids_visited = eat_cookie(presents_n, nice_kids_visited)

    the_neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not presents_n or nice_kids_visited == all_nice_kids:
        break

    command = input()

the_neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents_n and nice_kids_visited < all_nice_kids:
    print('Santa ran out of presents!')

print(*[' '.join(row)for row in the_neighborhood], sep='\n')

if nice_kids_visited == all_nice_kids:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {all_nice_kids - nice_kids_visited} nice kid/s.")