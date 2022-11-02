n = int(input())
even = set()
odd = set()
for row in range(1, n + 1):
    name = input()
    ascii_list = [ord(ch) for ch in name]
    ascii_sum = sum(ascii_list)
    result = ascii_sum // row
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

if sum(even) > sum(odd):
    final = odd ^ even
    print(*final, sep=", ")
elif sum(odd) > sum(even):
    final = odd - even
    print(*final, sep=", ")
else:
    final = odd | even
    print(*final, sep=", ")