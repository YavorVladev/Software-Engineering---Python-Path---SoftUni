rows = int(input())
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.extend(data)
print(matrix)