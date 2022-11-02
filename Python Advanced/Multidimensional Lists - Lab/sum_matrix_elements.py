rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

result = 0
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        result += matrix[row_index][col_index]


print(result)
print(matrix)
