size = int(input())
matrix = []


def is_valid(row, col, matrix):
    size = len(matrix)
    return 0 <= row < size and 0 <= col < size


for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()

    if command == "END":
        break

    params = command.split()
    action = params[0]
    if action == "Add":
        row = int(params[1])
        col = int(params[2])
        value = int(params[3])
        if is_valid(row, col, matrix):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif action == "Subtract":
        row = int(params[1])
        col = int(params[2])
        value = int(params[3])
        if is_valid(row, col, matrix):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

for el in matrix:
    print(*el)