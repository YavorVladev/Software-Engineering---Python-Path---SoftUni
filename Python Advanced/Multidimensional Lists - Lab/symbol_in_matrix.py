n = int(input())
matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

wanted_symbol = input()

position = None
for i in range(n):
    for j in range(n):
        if matrix[i][j] == wanted_symbol:
            position = (i, j)
            print(position)
            break
    if position:
        break
if not position:
    print(f"{wanted_symbol} does not occur in the matrix")
