n, m = list(map(int, input().split()))
a = set()
b = set()
for n1 in range(n):
    number = int(input())
    a.add(number)
for n2 in range(m):
    number = int(input())
    b.add(number)

el_in_both = a & b
print(*el_in_both, sep="\n")
