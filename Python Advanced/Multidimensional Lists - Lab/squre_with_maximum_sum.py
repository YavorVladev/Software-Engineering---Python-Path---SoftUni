import sys

rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)

max_sum = -sys.maxsize
max_matrix_sum = []

for i in range(rows - 1):
    for j in range(cols - 1):
        sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix_sum = sub_matrix.copy()

print(max_matrix_sum[0], max_matrix_sum[1])
print(max_matrix_sum[2], max_matrix_sum[3])
print(max_sum)
