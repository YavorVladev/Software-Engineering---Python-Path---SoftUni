import sys

rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_number = -sys.maxsize
biggest_list = []
for row_idx in range(rows - 2):
    for col_idx in range(columns - 2):
        sub_matrix = [matrix[row_idx][col_idx], matrix[row_idx][col_idx + 1],
                      matrix[row_idx][col_idx + 2], matrix[row_idx + 1][col_idx], matrix[row_idx + 1][col_idx + 1],
                      matrix[row_idx + 1][col_idx + 2], matrix[row_idx + 2][col_idx], matrix[row_idx + 2][col_idx + 1],
                      matrix[row_idx + 2][col_idx + 2]]
        if sum(sub_matrix) > max_number:
            max_number = sum(sub_matrix)
            biggest_list = sub_matrix.copy()
print(f"Sum = {max_number}")
print(biggest_list[0], biggest_list[1], biggest_list[2])
print(biggest_list[3], biggest_list[4], biggest_list[5])
print(biggest_list[6], biggest_list[7], biggest_list[8])
