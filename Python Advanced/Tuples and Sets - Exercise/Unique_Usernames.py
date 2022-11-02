n = int(input())
a = set()
for _ in range(n):
    name = input()
    a.add(name)

print(*a, sep="\n")
