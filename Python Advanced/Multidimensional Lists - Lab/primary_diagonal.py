n = int(input())
matrix = []

for _ in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

res = 0
for i in range(n):
    res += matrix[i][i]

print(res)