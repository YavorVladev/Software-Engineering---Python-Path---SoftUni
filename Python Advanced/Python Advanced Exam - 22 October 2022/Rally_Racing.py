MATRIX_SIZE = int(input())  # square matrix
race_number = input()
matrix = []
tunnels = []
start_row, start_col = 0, 0
passed_kms = 0
finish_row, finish_col = 0, 0

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    if "T" in matrix[row]:
        tunnels.append([row, matrix[row].index('T')])
    if "F" in matrix[row]:
        finish_row, finish_col = row, matrix[row].index('F')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

tunnel_1_row, tunnel_1_col = tunnels[0][0], tunnels[0][1]
tunnel_2_row, tunnel_2_col = tunnels[1][0], tunnels[1][1]
a = 5


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


command = input()
while command != "End":
    direction = command
    start_row, start_col = movement(start_row, start_col, direction)
    where_it_went = matrix[start_row][start_col]

    if where_it_went == ".":
        passed_kms += 10
    elif where_it_went == "T":
        start_row, start_col = tunnel_2_row, tunnel_2_col
        matrix[tunnel_1_row][tunnel_1_col] = "."
        matrix[tunnel_2_row][tunnel_2_col] = "."
        passed_kms += 30
    elif where_it_went == "F":
        passed_kms += 10
        matrix[start_row][start_col] = 'C'
        print(f"Racing car {race_number} finished the stage!")
        print(f"Distance covered {passed_kms} km.")
        for row in matrix:
            print(*row, sep="")
        break

    command = input()
if command == "End":
    matrix[start_row][start_col] = "C"
    print(f"Racing car {race_number} DNF.")
    print(f"Distance covered {passed_kms} km.")
    for row in matrix:
        print(*row, sep="")