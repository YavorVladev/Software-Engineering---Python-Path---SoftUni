size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

prim = []
sec = []
for i in range(size):
    prim.append(matrix[i][i])
    sec.append(matrix[i][size - 1 - i])

print(abs(sum(prim) - sum(sec)))
