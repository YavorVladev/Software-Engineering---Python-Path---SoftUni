rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

times = 0
for rows_idx in range(rows - 1):
    for col_idx in range(columns - 1):
        if matrix[rows_idx][col_idx] == matrix[rows_idx][col_idx + 1] == matrix[rows_idx + 1][col_idx]\
                == matrix[rows_idx + 1][col_idx + 1]:
            times += 1
print(times)
