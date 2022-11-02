rows, columns = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for j in range(columns):
    res = 0
    for i in range(rows):
        res += matrix[i][j]
    print(res)