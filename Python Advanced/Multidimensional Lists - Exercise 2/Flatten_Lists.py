text = input().split('|')

result = []
while text:
    subset = text.pop().split()
    for el in subset:
        result.append(el)
print(*result, end="")
