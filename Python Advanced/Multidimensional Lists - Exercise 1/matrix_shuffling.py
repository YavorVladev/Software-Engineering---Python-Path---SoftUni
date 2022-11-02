rows, columns = [int(x) for x in input().split()]
matrix = []


def is_outside(row, col, all_rows, all_columns):
    return row < 0 or col < 0 or row >= all_rows or col >= all_columns


for _ in range(rows):
    matrix.append(input().split())

while True:
    line = input()
    if line == "END":
        break

    params = line.split()

    if len(params) != 5 or params[0] != 'swap':
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in params[1:]]

    if is_outside(row1, col1, rows, columns) or is_outside(row2, col2, rows, columns):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=" ")