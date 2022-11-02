n = int(input())
a = set()
for _ in range(n):
    element = input().split()
    if len(element) == 2:
        a.add(element[0])
        a.add(element[1])
    elif len(element) == 3:
        a.add(element[0])
        a.add(element[1])
        a.add(element[2])
    elif len(element) == 4:
        a.add(element[0])
        a.add(element[1])
        a.add(element[2])
        a.add(element[3])
    else:
        a.add(element[0])
print(*a, sep="\n")

